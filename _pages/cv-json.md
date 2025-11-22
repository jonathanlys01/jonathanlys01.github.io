---
layout: archive
title: "CV"
permalink: /cv-json/
author_profile: false
redirect_from:
  - /resume-json
---

{% include base_path %}

<link rel="stylesheet" href="{{ base_path }}/assets/css/cv-style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<style>
  .archive {
    width: 80%;
    margin: 0 auto;
    float: none;
    padding-right: 0;
  }
  
  @media (min-width: 80em) {
    .archive {
      width: 70%;
    }
  }
</style>

{% include cv-template.html %}

<div class="cv-download-links" align="center" style="margin-top: 20px;">
  <button onclick="window.print();" class="cv-download-link" style="display: flex; align-items: center; gap: 8px; padding: 8px 16px; font-size: 1rem; border: none; background-color:rgb(13, 34, 55); color: #fff; border-radius: 4px; cursor: pointer;">
    <i class="fas fa-print"></i>
    Print CV
  </button>
</div>
