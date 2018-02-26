import skimage
import skimage.filters
import numpy as np
import scipy.ndimage

def snake(image, initialContour, edgeImage=None, alpha=0.01, beta=0.1, wLine=0, wEdge=1, gamma=0.01,
          maxIterations=2500):

    maxIterations = int(maxIterations)
    if maxIterations <= 0:
        raise ValueError('maxIterations should be greater than 0.')

    convergenceOrder = 10

    # valid_bcs = ['periodic', 'free', 'fixed', 'free-fixed',
    #              'fixed-free', 'fixed-fixed', 'free-free']
    # if bc not in valid_bcs:
    #     raise ValueError("Invalid boundary condition.\n" +
    #                      "Should be one of: " + ", ".join(valid_bcs) + '.')

    image = skimage.img_as_float(image)
    isMultiChannel = image.ndim == 3

    # If edge image is not given and an edge weight is specified, then get the edge of image using sobel mask
    # Otherwise set edge image to zero if it is none (it follows that wEdge must be 0)
    if edgeImage is None and wEdge != 0:
        # Reflect mode is used to minimize the values at the outer boundaries of the edge image
        # When applying a Sobel kernel, there are a few ways to handle border, reflect repeats the outside
        # edges which should return a small edge
        edgeImage = np.sqrt(scipy.ndimage.sobel(image, axis=0, mode='reflect') ** 2 +
                            scipy.ndimage.sobel(image, axis=1, mode='reflect') ** 2)
    elif edgeImage is None:
        edgeImage = 0

    # Calculate the external energy which is composed of the image intensity and ege intensity
    # TODO Add termination energy
    # TODO Add constraint energy
    if isMultiChannel:
        externalEnergy = wLine * np.sum(image, axis=2) + wEdge * np.sum(edgeImage, axis=2)
    else:
        externalEnergy = wLine * image + wEdge * edgeImage

    # TODO Determine if interpolation for smoothness is necessary
    # Interpolate for smoothness:
    # intp = RectBivariateSpline(np.arange(img.shape[1]),
    #                            np.arange(img.shape[0]),
    #                            img.T, kx=2, ky=2, s=0)
    #

    # Split initial contour into x's and y's
    x, y = initialContour[:, 0].astype(float), initialContour[:, 1].astype(float)

    # Create a matrix that will contain previous x/y values of the contour
    # Used to determine if contour has converged if the previous values are consistently smaller
    # than the convergence amount
    previousX = np.empty((convergenceOrder, len(x)))
    previousY = np.empty((convergenceOrder, len(y)))

    # Build snake shape matrix for Euler equation
    n = len(x)
    a = np.roll(np.eye(n), -1, axis=0) + \
        np.roll(np.eye(n), -1, axis=1) - \
        2 * np.eye(n)  # second order derivative, central difference
    b = np.roll(np.eye(n), -2, axis=0) + \
        np.roll(np.eye(n), -2, axis=1) - \
        4 * np.roll(np.eye(n), -1, axis=0) - \
        4 * np.roll(np.eye(n), -1, axis=1) + \
        6 * np.eye(n)  # fourth order derivative, central difference
    A = -alpha * a + beta * b

    # Impose boundary conditions different from periodic:
    sfixed = False
    if bc.startswith('fixed'):
        A[0, :] = 0
        A[1, :] = 0
        A[1, :3] = [1, -2, 1]
        sfixed = True
    efixed = False
    if bc.endswith('fixed'):
        A[-1, :] = 0
        A[-2, :] = 0
        A[-2, -3:] = [1, -2, 1]
        efixed = True
    sfree = False
    if bc.startswith('free'):
        A[0, :] = 0
        A[0, :3] = [1, -2, 1]
        A[1, :] = 0
        A[1, :4] = [-1, 3, -3, 1]
        sfree = True
    efree = False
    if bc.endswith('free'):
        A[-1, :] = 0
        A[-1, -3:] = [1, -2, 1]
        A[-2, :] = 0
        A[-2, -4:] = [-1, 3, -3, 1]
        efree = True

    # Only one inversion is needed for implicit spline energy minimization:
    inv = scipy.linalg.inv(A + gamma * np.eye(n))
    pass