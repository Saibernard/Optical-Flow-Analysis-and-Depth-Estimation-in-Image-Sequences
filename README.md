# Optical-Flow-Analysis-and-Depth-Estimation-in-Image-Sequences
This repository holds a computer vision solution analyzing optical flow. It calculates spatiotemporal derivatives, employs Lucas-Kanade for flow computation, visualizes flow vectors with confidence metrics, determines epipole using RANSAC, and estimates pixel depth. Also handles motion equations for planar scenes.


# Optical Flow Analysis in Image Sequences

This repository showcases an advanced analysis of optical flow within image sequences, diving deep into the intricacies of spatiotemporal derivatives. By utilizing the provided Python functions, we compute gradients to identify motion and change within a sequence.

## Key Features

- **Spatiotemporal Derivatives Computation:** Extract motion insights from the image based on its sequence.
- **Optical Flow Field Creation:** A meticulous approach to compute optical flow vectors (u, v) for each pixel, underpinned by a confidence metric `smin`.
- **Vector Field Visualization:** Dynamic plotting functions catering to varying thresholds to ensure precision and clarity.
- **Epipole Calculation:** Incorporating the RANSAC algorithm, we discern the epipole's pixel position to assess optical flow and its associated motion dynamics.


### Threshold = 1:
![epipole_1](https://github.com/Saibernard/Optical-Flow-Analysis-and-Depth-Estimation-in-Image-Sequences/assets/112599512/17680eb5-762b-4e36-8dc1-7a583fd32f5a)

### Threshold = 10:
![epipole_10](https://github.com/Saibernard/Optical-Flow-Analysis-and-Depth-Estimation-in-Image-Sequences/assets/112599512/937286e7-2b82-49f5-9215-4853bb93aa14)

### Threshold = 30:
![epipole_30](https://github.com/Saibernard/Optical-Flow-Analysis-and-Depth-Estimation-in-Image-Sequences/assets/112599512/11a5ce9b-356d-4e14-ad24-4b047e415669)

- **Depth Mapping:** Transform pixel flow data, confidence metrics, and epipole values into depth insights at each pixel, visualized through a comprehensive depth map.
- 
### Threshold = 1:
![depth_1](https://github.com/Saibernard/Optical-Flow-Analysis-and-Depth-Estimation-in-Image-Sequences/assets/112599512/73d1a393-825c-4876-955b-3c026ad360f8)

### Threshold = 10:
![depth_10](https://github.com/Saibernard/Optical-Flow-Analysis-and-Depth-Estimation-in-Image-Sequences/assets/112599512/c864498a-ce7c-4522-a7ff-7abc3471c6b1)

### Threshold = 30:
![depth_30](https://github.com/Saibernard/Optical-Flow-Analysis-and-Depth-Estimation-in-Image-Sequences/assets/112599512/6d3fa2a8-ac53-48f5-9e10-0dba0354791e)



- **Planar Scene Motion Analysis:** Advanced exploration of the motion exhibited by planar segments within the scene.

### Threshold = 1:
![Figure_1](https://github.com/Saibernard/Optical-Flow-Analysis-and-Depth-Estimation-in-Image-Sequences/assets/112599512/fff13362-6694-4138-86d2-5305c58f0f41)

### Threshold = 10:
![Figure_10](https://github.com/Saibernard/Optical-Flow-Analysis-and-Depth-Estimation-in-Image-Sequences/assets/112599512/4c948582-88cb-4b68-a92a-c258779bcb5b)

### Threshold = 30:
![Figure_30](https://github.com/Saibernard/Optical-Flow-Analysis-and-Depth-Estimation-in-Image-Sequences/assets/112599512/9663d077-46db-4f5f-8daf-bd2c4243e340)


## Overview

This project amalgamates the foundations of optical flow analysis with advanced computational techniques to provide a holistic view of image sequence motions and associated depths. It is ideal for researchers, computer vision enthusiasts, and developers keen on harnessing the power of motion analysis.
