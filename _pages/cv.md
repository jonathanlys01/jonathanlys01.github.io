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
* Ph.D. student, IMT Atlantique, 2024-2027
  * Research on language models
  * Supervisor: Vincent Gripon, Bastien Pasdeloup, Axel Marmoret

* Engineering degree, IMT Atlantique, 2021-2024
  * Mathematical and Computational Engineering specialization
  * Machine Learning, Deep Learning, Computer Vision, Signal Processing, Optimization

* M.Sc. Engineering Sciences and Applications, University of Rennes 1, 2023-2024
  * Signal and image processing major

* Academic exchange, University of Technology Sydney, 2023

Work experience
======

* November 2024: Visiting Scientist
  * Sony Europe, Stuttgart, Germany
  * Research on discrete diffusion models for text generation

* April 2024 - October 2024: Research Intern
  * Criteo AI Lab, Paris, France
  * Studied diffusion models, trained large diffusion models for image background generation
  * Supervisor: Jaspreet Sandhu, Thibaut Issenhuth, Ludovic Dos Santos

* Summer 2023: Research Intern
  * BRAIn team, IMT Atlantique, Brest, France
  * Studied parameter-efficient fine-tuning methods for SAM and attention-based data augmentation techniques
  * Supervisor: Bastien Pasdeloup

* February 2022: Developer Intern
  * French Polynesia’s government IT Department, Papeete, French Polynesia
  * Development of a Web application for network management, automation of database migrations
  
Skills
======
* Computer Science
  * Python, SQL, Java, R, Julia, C++, Matlab, Jupyter
* Machine Learning
  * Numpy, Pandas, sklearn, statistical and probabilistic models
* Deep Learning
  * PyTorch, Tensorflow, Keras, CNNs and Vision Transformers training
* Hugging Face 🤗
  * tranformers, diffusers, tokenizers, datasets, accelerate
* Distributed operations
  * Hadoop, Spark, multi-gpu/multi-node training (PyTorch distributed, Accelerate, NCCL), SLURM
* Soft Skills
  * Agile methods, communication, applied research
* Languages
  * English (C1, IELTS 7.5), Chinese (B2.1, HSK3 equivalent, intensive summer study at Beijing Language and Culture University), basic Spanish

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>