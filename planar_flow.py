import numpy as np

def compute_planar_params(flow_x, flow_y, K,
                                up=[256, 0], down=[512, 256]):
    """
    params:
        @flow_x: np.array(h, w)
        @flow_y: np.array(h, w)
        @K: np.array(3, 3)
        @up: upper left index [i,j] of image region to consider.
        @down: lower right index [i,j] of image region to consider.
    return value:
        sol: np.array(8,)
    """
    """
    STUDENT CODE BEGINS
    """
    K_inverse = np.linalg.inv(K)
    # print(K_inverse)
    x = np.arange(up[1],down[1])
    y = np.arange(up[0], down[0])

    xx, yy = np.meshgrid(x,y)
    calib_x = np.array([])
    calib_y = np.array([])
    p = 0

    for i in range(up[0], down[0]):
        for j in range(up[1], down[1]):
            calibrated_points = K_inverse @ np.array([j,i,1])
            # print(calibrated_points)
            calibrated_points = calibrated_points/calibrated_points[2]
            calib_x = np.append(calib_x, calibrated_points[0])
            calib_y = np.append(calib_y, calibrated_points[1])

            p = p+1

    # print(np.shape(calib_x))
    # print(calib_x)
    x_2 = calib_x ** 2
    y_2 = calib_y**2
    # print(x_2)
    xy = calib_x * calib_y

    A_up = np.hstack((x_2.reshape(-1,1), xy.reshape(-1,1), calib_x.reshape(-1,1),
                       calib_y.reshape(-1,1),np.ones((p,1)), np.zeros((p,3))))
    A_down = np.hstack((xy.reshape(-1,1),y_2.reshape(-1,1), np.zeros((p,3)),
                          calib_y.reshape(-1,1), calib_x.reshape(-1,1), np.ones((p,1))))

    A = np.vstack((A_up, A_down))

    flow_x_calibrated = flow_x[yy,xx]
    flow_y_calibrated = flow_y[yy,xx]
    # print(flow_x_calibrated)
    # print(flow_x_calibrated.shape)
    # f = flow_x_calibrated.flatten()
    # print(f.shape)
    flow_x_flatten = flow_x_calibrated.flatten()
    flow_y_flatten = flow_y_calibrated.flatten()

    b = np.vstack((flow_x_flatten, flow_y_flatten, np.zeros(flow_x_calibrated.size)))
    b_calib = K_inverse@b
    b_calib = b_calib[0:2, :]
    b = np.vstack((b_calib[0].reshape(-1,1), b_calib[1].reshape(-1,1)))
    A_values = np.linalg.lstsq(A,b, rcond=None)[0]
    sol = A_values.flatten()



    """
    STUDENT CODE ENDS
    """
    return sol
    
