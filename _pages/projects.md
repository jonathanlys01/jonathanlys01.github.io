---
layout: page
title: projects
permalink: /projects/
description: Models, experiments, and things you can explore.
nav: true
nav_order: 2
---

<div class="project-grid">
  {% assign sorted_projects = site.projects | sort: 'importance' %}
  {% for project in sorted_projects %}
    <article class="project-tile{% if forloop.first %} project-featured{% endif %}">
      <a class="project-image" href="{{ project.url | relative_url }}" tabindex="-1" aria-hidden="true"><img src="{{ project.img | relative_url }}" alt="" loading="{% if forloop.first %}eager{% else %}lazy{% endif %}" width="1200" height="750"></a>
      <div class="project-copy"><p class="eyebrow">{{ project.category }}</p><h2><a href="{{ project.url | relative_url }}">{{ project.title }} <span aria-hidden="true">↗</span></a></h2><p>{{ project.description }}</p>
        {% if forloop.first %}<a class="text-action" href="https://jonathanlys01.github.io/reve-atlas/">Open explorer <span aria-hidden="true">↗</span></a>{% endif %}
      </div>
    </article>
  {% endfor %}
  <a class="project-tile project-more" href="https://github.com/{{ site.data.socials.github_username }}"><span class="research-glyph" aria-hidden="true">{ ... }</span><div><p class="eyebrow">Work in progress</p><h2>More on GitHub <span aria-hidden="true">↗</span></h2><p>Source code, experiments, and smaller explorations.</p></div></a>
</div>
