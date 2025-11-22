---
custom_title: '<div style="display:flex; align-items:flex-start; font-family:sans-serif;">
  <div style="font-size:5.8em; font-weight:bold; line-height:1; margin-right:0.13em; min-width:0;">Optimiz</div>
  <div style="display:flex; flex-direction:column; justify-content:flex-start; line-height:1; padding-top:1.34em;">
    <span style="font-size:2em; font-weight:bold;">ing</span>
    <span style="font-size:2em; font-weight:bold;">ers</span>
  </div>
  </div>'
tags:
  - tech
  - deep-learning
  - optimization
excerpt: "ML and hardware improvements on optimizers"
---

{% include toc %}

**TL;DR** Technical notes on improving optimizers via machine learning and hardware advancements. Assumes familiarity with basic optimization concepts.
{: .notice--info}

## Algorithmic Improvements

### Preconditioning and Second-Order Methods

SGD, RMSProp, and Adam are essentially **first-order methods**, they only use information from the gradient. 
Second-order methods (like Newton’s method or L-BFGS) use or approximate the Hessian (curvature matrix) to precondition updates. True **second-order methods** are expensive in deep learning (Hessian is huge), but approximations can yield faster convergence without full Hessian computation.

**Preconditioning** means transforming the gradient by an approximate inverse curvature matrix so that the landscape is closer to isotropic (equal curvature in all directions). Adaptive gradient methods already do a simple diagonal preconditioning (RMSProp/Adam use the diagonal of the gradient covariance). More powerful preconditioners use matrix approximations:

### SOAP and Muon

Two cutting-edge optimizers that have gained attention are SOAP (2024) and Muon (2024/2025). Both aim to improve the convergence speed of large-model training by clever preconditioning, while addressing the shortcomings of naive second-order methods.

## Efficient implementations

### Fused and Foreach Optimizer steps in Pytorch

### Distribution with Sharding and ZeRO


## References

<div style="border: 1px solid #ccc; padding: 1em; border-radius: 8px; background: transparent;">
  <ul>
    <h3>Scaling laws</h3>
    <li><a href="https://arxiv.org/pdf/2001.08361">Scaling Laws for Neural Language Models</a></li>
    <li><a href="https://arxiv.org/pdf/2203.15556">Training Compute-Optimal Large Language Models</a></li>
    <h3>Pre-training and MFU</h3>
    <li><a href="https://arxiv.org/pdf/2204.02311">PaLM: Scaling Language Modeling with Pathways</a></li>
    <li><a href="https://huggingface.co/spaces/nanotron/ultrascale-playbook">The Ultra-scale Playbook</a></li>
    <h3>How to scale</h3>
    <li><a href="https://arxiv.org/pdf/2203.03466">muP: Zero-Shot HP Transfer</a></li>
    <li><a href="https://cloneofsimo.notion.site/What-to-do-to-scale-up-09e469d7c3444d6a90305397c38a46f5">What to do to scale up</a></li>
    <li><a href="https://www.cerebras.ai/blog/the-practitioners-guide-to-the-maximal-update-parameterization">The Practitioner's Guide to the Maximal Update Parameterization</a></li>
    <h3>Muon and its Applications</h3>
    <li><a href="https://kellerjordan.github.io/posts/muon/">Keller Jordan's blog on Muon</a></li>
    <li><a href="https://arxiv.org/pdf/2505.02222">Practical Efficiency of Muon for Pretraining</a></li>
    <li><a href="https://arxiv.org/pdf/2502.16982">Muon is scalable for LLM training</a></li>
    <li><a href="https://moonshotai.github.io/Kimi-K2/">Kimi K2 release</a></li>
  </ul>
</div>

---