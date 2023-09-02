import numpy as np
import cv2
import pdb
import matplotlib.pyplot as plt
from tqdm import tqdm


def plot_flow(image, flow_image, confidence, threshmin=10):
    """
    params:
        @img: np.array(h, w)
        @flow_image: np.array(h, w, 2)
        @confidence: np.array(h, w)
        @threshmin: confidence must be greater than threshmin to be kept
    return value:
        None
    """

    """
    STUDENT CODE BEGINS
    """
    confidence_threshold = np.where(confidence > threshmin)
    # print(threshmin)
    # print(confidence_threshold)
    x = confidence_threshold[1]
    y = confidence_threshold[0]

    flow = flow_image[confidence_threshold]
    flow_x = flow[:,0]
    flow_y = flow[:,1]

    plt.imshow(image, cmap = 'gray')
    plt.quiver(x, y, (flow_x * 10).astype(int), (flow_y * 10).astype(int),
               angles='xy', scale_units='xy', scale=1., color='red', width=0.001)
    # plt.plot(image)

    """
    STUDENT CODE ENDS
    """
    return
