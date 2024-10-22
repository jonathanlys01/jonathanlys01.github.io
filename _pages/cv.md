---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Engineering degree, IMT Atlantique, 2021-present
  * Mathematical and Computational Engineering specialization
  * Machine Learning, Deep Learning, Computer Vision, Signal Processing, Optimization
* M.Sc. Engineering Sciences and Applications, University of Rennes 1, 2023-2024
* Academic exchange, University of Technology Sydney, 2023

Work experience
======
* April 2024 - Present: Research Intern
  * Criteo AI Lab, Paris
  * Studied diffusion models for image generation
  * Supervisor: Jaspreet Sandhu, Thibaut Issenhuth, Ludovic Dos Santos

* Summer 2023: Research Intern
  * BRAIn team, IMT Atlantique
  * Fine-tuned SAM, studied data augmentation techniques
  * Supervisor: Bastien Pasdeloup

* February 2022: Developer Intern
  * French Polynesia’s government IT Department
  * Development of a Web application for network management, automation of database migrations
  
Skills
======
* Computer Science
  * Python, SQL, Java, R, Julia, C++, Matlab, Jupyter
* Machine Learning
  * Numpy, Pandas, sklearn, statistical and probabilistic models
* Deep Learning
  * PyTorch, Tensorflow, Keras, CNNs and Vision Transformers training
* Distributed operations
  * Hadoop, Spark, multi-gpu training (PyTorch distributed, Accelerate, NCCL)
* Soft Skills
  * Agile methods, communication, applied research
* Languages
  * English (C1, IELTS 7.5), Mandarin (B2.1, HSK3 equivalent, intensive summer study at Beijing Language and Culture University), basic Spanish

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>