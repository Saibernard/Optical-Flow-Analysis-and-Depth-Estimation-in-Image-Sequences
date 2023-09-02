import numpy as np
import pdb

def flow_lk_patch(Ix, Iy, It, x, y, size=5):
    """
    params:
        @Ix: np.array(h, w)
        @Iy: np.array(h, w)
        @It: np.array(h, w)
        @x: int
        @y: int
    return value:
        flow: np.array(2,)
        conf: np.array(1,)
    """
    """
    STUDENT CODE BEGINS
    """
    # print(Ix)
    h,w = Ix.shape
    row = np.array([x-2,x-1,x,x+1,x+2])
    row = row[(row>=0) & (row<w)]

    col = np.array([y-2,y-1,y,y+1,y+2])
    col = col[(col>=0) & (col<h)]

    xx,yy = np.meshgrid(col, row)

    A = np.hstack((Ix[xx, yy].reshape(-1,1), Iy[xx, yy].reshape(-1,1)))

    b = -1*It[xx,yy].reshape(-1,1)

    least_squares = np.linalg.lstsq(A,b, rcond=None)
    flow = np.array(least_squares[0].flatten())
    # print(least_squares[3])

    conf = np.min(least_squares[3])



    """
    STUDENT CODE ENDS
    """
    return flow, conf


def flow_lk(Ix, Iy, It, size=5):
    """
    params:
        @Ix: np.array(h, w)
        @Iy: np.array(h, w)
        @It: np.array(h, w)
    return value:
        flow: np.array(h, w, 2)
        conf: np.array(h, w)
    """
    image_flow = np.zeros([Ix.shape[0], Ix.shape[1], 2])
    confidence = np.zeros([Ix.shape[0], Ix.shape[1]])
    for x in range(Ix.shape[1]):
        for y in range(Ix.shape[0]):
            flow, conf = flow_lk_patch(Ix, Iy, It, x, y)
            image_flow[y, x, :] = flow
            confidence[y, x] = conf
    return image_flow, confidence

    

