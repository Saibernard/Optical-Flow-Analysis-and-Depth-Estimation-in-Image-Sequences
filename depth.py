import numpy as np

def depth(flow, confidence, ep, K, thres=10):
    """
    params:
        @flow: np.array(h, w, 2)
        @confidence: np.array(h, w, 2)
        @K: np.array(3, 3)
        @ep: np.array(3,) the epipole you found epipole.py note it is uncalibrated and you need to calibrate it in this function!
    return value:
        depth_map: np.array(h, w)
    """
    depth_map = np.zeros_like(confidence)

    """
    STUDENT CODE BEGINS
    """
    # print(confidence.shape)
    confidence_threshold = np.where(confidence>thres)
    u_flattened = (flow[:,:,0][confidence_threshold]).reshape(-1,1)
    v_flattened = (flow[:,:,1][confidence_threshold]).reshape(-1,1)

    zero_arrays = np.zeros(u_flattened.shape).reshape(-1,1)
    u_v = np.hstack((u_flattened, v_flattened, zero_arrays))
    K_inverse = np.linalg.inv(K)
    p_translation = K_inverse@u_v.T
    X_p = np.hstack((confidence_threshold[1].reshape(-1,1), confidence_threshold[0].reshape(-1,1),
                     np.ones(confidence_threshold[0].shape[0]).reshape(-1,1))).T
    X_calibrated = K_inverse@X_p

    calibrated_ep = K_inverse@ep
    # print(calibrated_ep.shape)
    calibrated_ep = calibrated_ep.reshape(1,3)

    p_trans_difference = np.linalg.norm((X_calibrated.T - calibrated_ep),axis = 1)

    p_den = np.linalg.norm(p_translation.T, axis=1)

    depth = p_trans_difference/p_den

    depth_map[confidence_threshold] = depth

    # print(depth_map)


    """
    STUDENT CODE ENDS
    """

    truncated_depth_map = np.maximum(depth_map, 0)
    valid_depths = truncated_depth_map[truncated_depth_map > 0]
    # You can change the depth bound for better visualization if your depth is in different scale
    depth_bound = valid_depths.mean() + 10 * np.std(valid_depths)
    # print(f'depth bound: {depth_bound}')

    truncated_depth_map[truncated_depth_map > depth_bound] = 0
    truncated_depth_map = truncated_depth_map / truncated_depth_map.max()
    

    return truncated_depth_map
