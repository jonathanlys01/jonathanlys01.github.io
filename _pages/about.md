---
layout: default
title: about
permalink: /
---

<div class="home-page">
  <header class="home-intro">
    <div class="home-intro-copy">
      <p class="eyebrow"><span class="ascii-mark" aria-hidden="true">[~]</span> Research / representations / generation</p>
      <h1>Jonathan Lys<span class="name-dot" aria-hidden="true">.</span></h1>
      <p class="home-lead">I study how masked models learn representations and generate diverse outputs.</p>
      <p class="home-bio">Third-year PhD candidate at <a href="https://www.imt-atlantique.fr/en">IMT Atlantique</a>, in the <a href="http://recherche.imt-atlantique.fr/brain/">BRAIN team</a>. Working on discrete diffusion, diversity-aware decoding, and EEG foundation models.</p>
      <p class="home-history">Previously Visiting Scientist at Sony Europe and Research Intern at Criteo AI Lab. <br/>Based in Brest, France.</p>
      <nav class="contact-links" aria-label="Find me online">
        <a href="mailto:{{ site.data.socials.email }}">Email <span aria-hidden="true">↗</span></a>
        <a href="https://github.com/{{ site.data.socials.github_username }}">GitHub <span aria-hidden="true">↗</span></a>
        <a href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}">Scholar <span aria-hidden="true">↗</span></a>
        <a href="{{ '/cv/' | relative_url }}">CV <span aria-hidden="true">↗</span></a>
      </nav>
    </div>
    <figure class="home-portrait">
      <img src="{{ '/assets/img/profile.jpeg' | relative_url }}" alt="Jonathan Lys" width="400" height="400">
    </figure>
  </header>

  <section class="home-work" aria-labelledby="selected-work">
    <div class="section-heading"><h2 id="selected-work">Selected work</h2><a class="quiet-link" href="{{ '/publications/' | relative_url }}">All publications <span aria-hidden="true">↗</span></a></div>
    <div class="reve-feature">
      <div class="reve-overview">
        <svg class="research-glyph reve-glyph" viewBox="0 0 64 64" fill="none" aria-hidden="true" focusable="false"><g stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13C9 13 9 9 12 10S16 17 19 14L23 11L26 14L29 5L32 20L35 10C39 9 39 16 43 14S48 9 51 12S55 15 59 12" stroke-opacity=".65"/><path d="M5 33C9 33 10 28 13 30S17 37 20 33L24 30L28 34L31 25L34 40L37 30C40 27 42 35 46 33S50 29 53 31S56 35 59 32"/><path d="M5 53C9 49 10 55 14 52S19 47 22 51L26 54L29 46L32 59L36 50C40 48 42 56 46 52S51 50 54 53S57 53 59 51" stroke-opacity=".45"/></g></svg>
        <div><p class="eyebrow">EEG foundation model / NeurIPS 2025</p><h3><a class="sweep-underline" href="https://brain-bzh.github.io/reve/">REVE</a></h3><p>A foundation model for EEG that adapts to different recording setups. Pretrained on data from 25,000 subjects.</p><a class="quiet-link" href="https://arxiv.org/abs/2510.21585">Read the paper <span aria-hidden="true">↗</span></a></div>
      </div>
      <div class="reve-contributions">
        <p class="eyebrow">From model to tools</p>
        <div class="contribution"><span class="contribution-index" aria-hidden="true">01</span><div><h4><a href="{{ '/projects/reve-atlas/' | relative_url }}">Embedding Atlas</a></h4><p>Interactive explorer for over a million EEG and MEG windows.</p></div></div>
        <div class="contribution"><span class="contribution-index" aria-hidden="true">02</span><div><h4><a href="https://huggingface.co/collections/brain-bzh/reve">Hugging Face release</a></h4><p>Release of the pretrained models and open pretraining data. <a href="https://huggingface.co/datasets/brain-bzh/reve-dataset">Explore the dataset</a></p></div></div>
        <div class="contribution"><span class="contribution-index" aria-hidden="true">03</span><div><h4><a href="https://braindecode.org/stable/generated/braindecode.models.REVE.html">Braindecode integration</a></h4><p>REVE compatibility with the Braindecode open-source ecosystem.</p></div></div>
      </div>
    </div>
    <div class="research-pair">
      <a class="research-note" href="https://arxiv.org/abs/2603.19146"><div class="research-glyph" aria-hidden="true">░░ ▒▒ ░░<br>▒▒ ▓▓ ▒▒<br>▓▓ ██ ▓▓</div><div><p class="eyebrow">Discrete diffusion / 2026</p><h3><span class="sweep-underline">D5P4</span></h3><p>Balancing quality and diversity in parallel discrete diffusion decoding.</p></div></a>
      <a class="research-note" href="https://arxiv.org/abs/2602.14759"><svg class="research-glyph loop-glyph" viewBox="0 0 64 64" fill="none" aria-hidden="true" focusable="false"><g stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M48 18A22 22 0 1 1 32 10"/><path d="M25 4L32 10L25 16"/></g></svg><div><p class="eyebrow">Inference / 2026</p><h3><span class="sweep-underline">Inner Loop Inference</span></h3><p>Extending computation in frozen Transformers by revisiting their inner layers.</p></div></a>
    </div>
  </section>

</div>
