# Optical-Flow-Analysis-and-Depth-Estimation-in-Image-Sequences
This repository holds a computer vision solution analyzing optical flow. It calculates spatiotemporal derivatives, employs Lucas-Kanade for flow computation, visualizes flow vectors with confidence metrics, determines epipole using RANSAC, and estimates pixel depth. Also handles motion equations for planar scenes.


# Optical Flow Analysis in Image Sequences

This repository showcases an advanced analysis of optical flow within image sequences, diving deep into the intricacies of spatiotemporal derivatives. By utilizing the provided Python functions, we compute gradients to identify motion and change within a sequence.

## Key Features

- **Spatiotemporal Derivatives Computation:** Extract motion insights from the image `insight23.png` based on its sequence.
- **Optical Flow Field Creation:** A meticulous approach to compute optical flow vectors (u, v) for each pixel, underpinned by a confidence metric `smin`.
- **Vector Field Visualization:** Dynamic plotting functions catering to varying thresholds to ensure precision and clarity.
- **Epipole Calculation:** Incorporating the RANSAC algorithm, we discern the epipole's pixel position to assess optical flow and its associated motion dynamics.
- **Depth Mapping:** Transform pixel flow data, confidence metrics, and epipole values into depth insights at each pixel, visualized through a comprehensive depth map.
- **Planar Scene Motion Analysis:** Advanced exploration of the motion exhibited by planar segments within the scene.

## Overview

This project amalgamates the foundations of optical flow analysis with advanced computational techniques to provide a holistic view of image sequence motions and associated depths. It is ideal for researchers, computer vision enthusiasts, and developers keen on harnessing the power of motion analysis.
