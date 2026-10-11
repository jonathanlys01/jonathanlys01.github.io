---
layout: post
title: "Torch Tips: Debugging CUDA Indexing"
date: 2026-10-11 00:00:00
description: "Choosing between tensor indexing and index_select."
tags: [tech, pytorch, gpu]
categories: postmortem
toc:
  beginning: true
---

**TL;DR:** Use `torch.index_select` when you want to select along one dimension with a 1-D integer index. If indexing fails on CUDA, first locate the failing operation and inspect the index bounds; changing the indexing API alone does not establish the root cause.

## The incident

In a diffusion sampler, a subsampling step expanded row indices and then used them to re-index several state tensors. The line `log_p_x0[expanded_idx]` was associated with `CUDA error: invalid configuration argument`. The [subsequent code change](https://github.com/jonathanlys01/d3p2/commit/23cb960) replaced row indexing with `torch.index_select` for those tensors:

```python
expanded_idx = slice_idx.repeat_interleave(self.config.group_size)
log_p_x0 = torch.index_select(log_p_x0, 0, expanded_idx)
```

That change makes the intended operation explicit: select rows along dimension 0. It does **not**, by itself, prove that an out-of-bounds index caused the CUDA error, or that `index_select` will always produce a clearer error. CUDA operations can report errors asynchronously, so the line in a traceback may not be the operation that failed.

## Which indexing operation?

[`torch.index_select`](https://docs.pytorch.org/docs/stable/generated/torch.index_select.html) takes a dimension and a 1-D integer index tensor. It returns a new tensor, not a view. It fits cases such as selecting a batch of rows or a set of columns:

```python
rows = torch.index_select(matrix, 0, row_indices)
columns = torch.index_select(matrix, 1, column_indices)
```

Square brackets remain useful for other indexing patterns: `matrix[mask]` for a boolean mask, `matrix[row_indices, column_indices]` for paired coordinates, and `matrix[:, 2:5]` for a slice. [Basic slicing returns a view, whereas advanced indexing returns a copy](https://docs.pytorch.org/docs/stable/tensor_view.html). Do not replace slicing with `index_select` merely for consistency, or assume either integer-indexing form is faster without measuring it.

## Debug the index before changing the API

First, rerun the failing case with `CUDA_LAUNCH_BLOCKING=1` to make CUDA calls synchronous and obtain a more useful traceback:

```bash
CUDA_LAUNCH_BLOCKING=1 python your_script.py
```

Then inspect the index's shape, dtype, and range against the dimension being selected. For a 1-D row index, a temporary check can make the bounds explicit:

```python
if expanded_idx.ndim != 1:
    raise ValueError("expected a 1-D row index")
if expanded_idx.numel():
    minimum = expanded_idx.min().item()
    maximum = expanded_idx.max().item()
    if minimum < 0 or maximum >= log_p_x0.size(0):
        raise IndexError(f"row indices [{minimum}, {maximum}] for {log_p_x0.size(0)} rows")
```

The `.item()` calls synchronize GPU values with the CPU, so keep this check for debugging rather than a performance-sensitive loop. If the bounds are valid, inspect the preceding CUDA operations too; the original error does not identify an invalid index on its own. See PyTorch's [CUDA semantics](https://docs.pytorch.org/docs/stable/notes/cuda.html) and [`CUDA_LAUNCH_BLOCKING` documentation](https://docs.pytorch.org/docs/stable/cuda_environment_variables.html) for the reason this helps.
