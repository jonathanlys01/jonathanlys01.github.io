---
layout: page
title: Wrong Pose
description: "From video to 3D pose: assessing movement and ergonomics."
img: assets/img/portfolio/wp-demo.gif
importance: 4
category: computer vision
---

_Collaborative project developed for the Deep Learning & CNNs course at the University of Technology Sydney (UTS). Code and documentation available on [GitHub](https://github.com/joanvelja/WrongPose-42028)._

Workplace musculoskeletal disorders (MSDs) and repetitive strain injuries are strongly correlated with prolonged poor posture. **Wrong Pose** is an automated computer vision service that processes continuous video streams to detect body posture, reconstruct 3D joint configurations, and score ergonomic correctness in real time.

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0 text-center">
    {% include figure.liquid loading="eager" path="assets/img/portfolio/wp-demo.gif" title="Wrong Pose Demo" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Real-time keypoint extraction and frame-wise pose assessment.
</div>

### Technical Pipeline

1. **Person Detection & 2D Keypoint Regression**: Employs Detectron2 (Faster R-CNN with ResNeXt-101 backbone) to localize persons and regress 17 body keypoints per frame.
2. **Temporal 3D Kinematics**: Passes 2D keypoint trajectories into VideoPose3D (strided 1D dilated convolutions) to resolve depth ambiguities and reconstruct full 3D body motion.
3. **Ergonomic Quality Regressor**: Computes 8 joint angle metrics and feeds scale-invariant feature vectors into a calibrated Multi-Layer Perceptron (MLP) regressor achieving 98% test accuracy against ground-truth ergonomics guidelines.

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0 text-center">
    {% include figure.liquid loading="eager" path="assets/img/portfolio/wp-score.png" title="Pose Quality Scoring" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Ergonomic posture score breakdown across monitored joint angles.
</div>

### Links

- **Source Code**: [github.com/joanvelja/WrongPose-42028](https://github.com/joanvelja/WrongPose-42028)
