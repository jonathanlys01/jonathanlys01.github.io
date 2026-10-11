---
layout: post
title: "Torch Tips: RoPE Buffers After Checkpoint Loading"
date: 2026-10-11 00:01:00
description: "Debugging uninitialized rotary frequencies in a loaded model."
tags: [tech, pytorch, gpu]
categories: postmortem
toc:
  beginning: true
---

**TL;DR:** A model can load its weights successfully while a non-persistent RoPE buffer is still wrong. If identical inference runs differ across process launches, inspect load-time state before changing the sampler or precision.

## The incident

In a Dream diffusion sampler, some launches produced almost empty or nonsensical completions; others failed in `torch.multinomial` after the model produced non-finite probabilities. The same failure occurred through Dream's own generation path, bypassing our sampler. Switching between `bf16` and `fp32` did not reliably fix it.

The clue was that repeated forwards behaved consistently **within** a process, but results differed **between** fresh launches. That pointed toward state established during model loading. In the affected setup (PyTorch 2.10.0, Transformers 5.12.1, A100), the loaded RoPE `inv_freq` values varied between processes and sometimes contained enormous or negative numbers. Recomputing them from the model configuration restored the expected frequency range and finite forwards.

## What went wrong?

Dream's rotary embedding registers `inv_freq` as a non-persistent buffer:

```python
self.register_buffer("inv_freq", inv_freq, persistent=False)
```

In PyTorch, [non-persistent buffers are omitted from `state_dict`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_buffer). The checkpoint therefore cannot restore this frequency table; model construction or a post-load step must supply its value. In this Dream loading path, the table was not reliably materialized after `from_pretrained`, even though the checkpoint weights loaded. Some bad values were finite, so a simple NaN check on the buffer would not have caught them.

The [current Dream loader](https://github.com/jonathanlys01/d3p2/blob/main/src/d5p4/dream_ref/modeling_dream.py) calls `reset_rope_parameters()` before returning the loaded model. It rebuilds the RoPE buffers from the configuration, including the per-layer tables. A first-forward finiteness check in the sampler catches a remaining failure before sampling can turn it into a misleading probability error. This is a model-specific fix, not a reason to reset every buffer in every Transformers model.

## Debug the loading path

1. Run the same forward several times in one process, then repeat in fresh processes. A cross-launch difference suggests load-time state, although it does not prove uninitialized memory by itself.
2. Inspect raw logits and the buffers used in the failing operation. For RoPE, compare `inv_freq` with values computed from the model's own configuration; finiteness alone is insufficient.
3. Check whether the buffer is excluded from the checkpoint with `persistent=False`. If so, verify that the loader reconstructs it **after** weight loading and before the first forward.
4. Test the load path, not just direct model construction. Avoid `nan_to_num` or sampler-side probability guards until the source of non-finite values is understood; they can hide the failure while leaving model outputs wrong.

A [similar report for MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano/issues/28) shows why this diagnostic is useful beyond Dream. It was reported with a different Transformers version, so the lesson is to **verify each model's load path**, not to assume one library version breaks every non-persistent buffer.
