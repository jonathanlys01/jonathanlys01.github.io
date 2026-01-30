---
title: "TENSLORA: Tensor Alternatives for Low-Rank Adaptation"
collection: publications
category: conferences
permalink: /publication/2026-tenslora
excerpt: 'This paper introduces TensLoRA, a unified framework for tensor-based low-rank adaptations in Transformers.<br><img src="/images/paper_figs/tenslora.png" width="90%">'
date: 2026-01-16
venue: "ICASSP"
paperurl: 'https://arxiv.org/pdf/2509.19391'
bibtexurl: '/files/tenslora.bib'
citation: 'Marmoret, et al. (2025). &quot;TensLoRA: Tensor Alternatives for Low-Rank Adaptation.&quot; In 2026 IEEE International Conference on Acoustics, Speech and Signal Processing <i>(ICASSP)</i>. IEEE.'
---

**Abstract**: Low-Rank Adaptation (LoRA) is widely used to efficiently adapt Transformers by adding trainable low-rank matrices to attention projections. While effective, these matrices are considered independent for each attention projection (Query, Key, and Value) and each layer. Recent extensions have considered joint, tensor-based adaptations, but only in limited forms and without a systematic framework. We introduce TensLoRA, a unified framework that aggregates LoRA updates into higher-order tensors and models a broad family of tensor-based low-rank adaptations. Our formulation generalizes existing tensor-based methods and enables mode-specific compression rates, allowing parameter budgets to be tailored according to the modality and task. Experiments on vision and language benchmarks reveal that the tensor construction directly impacts performance, sometimes better than standard LoRA under similar parameter counts.
