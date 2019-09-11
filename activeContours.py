import sys

from PyQt5.QtCore import *

import matplotlib.pyplot as plt

from helperWindow import *
import snake
import skimage.data
import skimage.color
import numpy as np
import skimage.filters
import skimage.segmentation
import scipy.ndimage

# Name of the application, organization that created the application and current version of the application
applicationName = 'Active Contours Helper Window'
organizationName = 'Addison Elliott'
version = '0.1.0'


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


def runHelper():
    # Set application, organization name and version
    # This is used for the QSettings (when an empty constructor is given)
    QCoreApplication.setApplicationName(applicationName)
    QCoreApplication.setOrganizationName(organizationName)
    QCoreApplication.setApplicationVersion(version)

    # app = QApplication(sys.argv)

    # form = HelperWindow()
    # form.show()
    #
    # sys.exit(app.exec_())

    # TODO Create function that allows real time tracking of snakes
    # Include an update function to update the snake, then the class can also contain things such as
    # changing input image, edge image, alpha, beta, gamma, etc and updating in real time so a user can
    # see what changes it has.
    # Also, I have found that it is extremely hard to tune these parameters for an image, so I think a good
    # feature will be to have a loop option where it'll loop through a bunch of different parameters and save the
    # output to a folder so that you can view them all later.

    # TODO Remove this and make a unit test eventually somehow

    # xx, yy = np.mgrid[:256, :256]
    # circle = 50 + skimage.filters.gaussian(((xx - 128) ** 2 + (yy - 128) ** 2 > 85**2) * 100.0, 2)
    #
    # circle = np.random.normal(scale=20.0, size=circle.shape) + circle
    #
    # # edgeImage = np.sqrt(scipy.ndimage.sobel(circle, axis=0, mode='reflect') ** 2 +
    # #                     scipy.ndimage.sobel(circle, axis=1, mode='reflect') ** 2)
    # circle2 = skimage.filters.gaussian(circle, 30)
    #
    # theta = np.arange(0, 2 * np.pi, 0.1)
    # x = 120 + 50 * np.cos(theta)
    # y = 140 + 60 * np.sin(theta)
    # init = np.array([x, y]).T
    #
    # # snakeContour = snake.kassSnake(circle2, init, wEdge=1.0, alpha=0.001, beta=0.4, gamma=100, maxIterations=50,
    # #                                maxPixelMove=None)
    #
    # snakeContour = snake.kassSnake(circle2, init, wEdge=1.0, alpha=0.001, beta=0.4, gamma=0.01, maxIterations=50,
    #                                maxPixelMove=None)
    #
    # plt.imshow(circle, cmap='gray')
    # plt.plot(x, y, 'g')
    # plt.plot(snakeContour[:, 0], snakeContour[:, 1], '-b')
    # plt.show()

    # This is working but the main thing is that maxPixelMove HAS TO BE 1.0?
    # Anything larger and it stops working? Its weird
    image = skimage.data.astronaut()
    image = skimage.color.rgb2gray(image)

    image2 = skimage.filters.gaussian(image, 6.0)

    s = np.linspace(0, 2 * np.pi, 400)
    x = 220 + 100 * np.cos(s)
    y = 100 + 100 * np.sin(s)
    init = np.array([x, y]).T

    s = np.linspace(0, 2 * np.pi, 400)
    x = 220 + 100 * np.cos(s)
    y = 100 + 100 * np.sin(s)
    init = np.array([x, y]).T

    snakeContour = snake.kassSnake(image2, init, wLine=0, wEdge=1.0, alpha=0.1, beta=0.1, gamma=0.001,
                                   maxIterations=5, maxPixelMove=None, convergence=0.1)

    # snakeContour = skimage.segmentation.active_contour(image2,
    #                        init, alpha=0.015, beta=10, gamma=0.001)

    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.plot(init[:, 0], init[:, 1], '--r', lw=2)
    plt.plot(snakeContour[:, 0], snakeContour[:, 1], '-b', lw=2)
    plt.show()


if __name__ == '__main__':
    runHelper()