---
title: "Residual Connections and the Causal Shift: Uncovering a Structural Misalignment in Transformers"
collection: publications
category: preprints
permalink: /publication/2026-residual
excerpt: "This paper identifies a residual-path input-output alignment shift in autoregressive Transformers and proposes residual attenuation to mitigate it."
date: 2026-02-16
venue: "arXiv"
paperurl: 'https://arxiv.org/abs/2602.14760'
bibtexurl: 'https://arxiv.org/bibtex/2602.14760'
citation: 'Lys, et al. (2026). &quot;Residual Connections and the Causal Shift: Uncovering a Structural Misalignment in Transformers.&quot; arXiv preprint arXiv:2602.14760.'
---

**Abstract**: Large Language Models (LLMs) are trained with next-token prediction, implemented in autoregressive Transformers via causal masking for parallelism. This creates a subtle misalignment: residual connections tie activations to the current token, while supervision targets the next token, potentially propagating mismatched information if the current token is not the most informative for prediction. In this work, we empirically localize this input-output alignment shift in pretrained LLMs, using decoding trajectories over tied embedding spaces and similarity-based metrics. Our experiments reveal that the hidden token representations switch from input alignment to output alignment deep within the network. Motivated by this observation, we propose a lightweight residual-path mitigation based on residual attenuation, implemented either as a fixed-layer intervention or as a learnable gating mechanism. Experiments on multiple benchmarks show that these strategies alleviate the representation misalignment and yield improvements, providing an efficient and general architectural enhancement for autoregressive Transformers.
