import numpy as np
def epipole(u,v,smin,thresh,num_iterations = 1000):
    ''' Takes flow (u,v) with confidence smin and finds the epipole using only the points with confidence above the threshold thresh
    (for both sampling and finding inliers)
    params:
        @u: np.array(h,w)
        @v: np.array(h,w)
        @smin: np.array(h,w)
    return value:
        @best_ep: np.array(3,)
        @inliers: np.array(n,) 
    
    u, v and smin are (h,w), thresh is a scalar
    output should be best_ep and inliers, which have shapes, respectively (3,) and (n,) 
    '''

    """
    You can do the thresholding on smin using thresh outside the RANSAC loop here. 
    Make sure to keep some way of going from the indices of the arrays you get below back to the indices of a flattened u/v/smin
    STUDENT CODE BEGINS
    """
    # print(np.shape(u))
    x= np.arange(u.shape[0])
    y = np.arange(u.shape[1])

    x,y = np.where(smin>thresh)

    threshold_actual = np.where(smin.flatten() > thresh)

    valid_u = u[x,y]
    valid_v = v[x,y]

    x = x-256
    y = y - 256

    # print('x,y', x,y)


    # raise TypeError('stop')

    x_p = np.hstack((y.reshape(-1,1), x.reshape(-1,1), np.ones((len(x),1)))).T
    u_v = np.hstack((valid_u.reshape(-1,1), valid_v.reshape(-1,1), np.zeros((len(valid_u),1)))).T





    """ 
    STUDENT CODE ENDS
    """

    sample_size = 2

    eps = 10**-2

    best_num_inliers = -1
    best_inliers = None
    best_ep = None

    for i in range(num_iterations): #Make sure to vectorize your code or it will be slow! Try not to introduce a nested loop inside this one
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(0,np.sum((smin>thresh))))
        sample_indices = permuted_indices[:sample_size] #indices for thresholded arrays you find above
        test_indices = permuted_indices[sample_size:] #indices for thresholded arrays you find above

        """
        STUDENT CODE BEGINS
        """
        x_p_sample = x_p[:, sample_indices]
        u_v_sample = u_v[:, sample_indices]

        Matrix_A = np.cross(x_p_sample, u_v_sample, axis=0)
        Matrix_A = Matrix_A.T
        # print(Matrix_A)

        U,S, Vt = np.linalg.svd(Matrix_A)
        ep = Vt[-1,:] # taking last row of Vt
        x_p_test = x_p[:, test_indices]
        u_v_test = u_v[:, test_indices]

        u_v_test_cross = np.cross(x_p_test, u_v_test, axis=0)
        dist = abs(np.dot(ep, u_v_test_cross))

        test_inliers = np.argwhere(dist<eps).reshape(-1)
        # print(test_inliers)
        inliers = np.hstack((threshold_actual[0][sample_indices], threshold_actual[0][test_indices[test_inliers]]))




        """
        STUDENT CODE ENDS
        """

        #NOTE: inliers need to be indices in flattened original input (unthresholded), 
        #sample indices need to be before the test indices for the autograder
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_ep = ep
            best_inliers = inliers

    return best_ep, best_inliers
