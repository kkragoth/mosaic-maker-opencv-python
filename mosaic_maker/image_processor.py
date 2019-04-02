import cv2
import numpy as np
from math import floor

# from config import SOBEL_BLUR_KERNEL_SHAPE, EDGES_LOWER_THRESHOLD
# from .patch import Patch

SOBEL_BLUR_KERNEL_SHAPE = (21, 21)
EDGES_LOWER_THRESHOLD = 0

class ImageProcessor:
    def __init__(self, image_name, source_image, patch_size):
        self.image_name = image_name
        self.source_image = source_image

        self.cropped_image = self._crop_to_square(source_image)
        self.sobel_magnitude_image = self.calculate_sobel_magnitude_image(self.cropped_image)

        rescaled_image = cv2.resize(self.cropped_image, (patch_size, patch_size))
        rescaled_sobel_magnitude_image = cv2.resize(self.sobel_magnitude_image, (patch_size, patch_size))

        self.processed_image = Patch(image_name, rescaled_image, rescaled_sobel_magnitude_image)

    @staticmethod
    def _crop_to_square(image):
        # ToDo return image cropped to center square
        # https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
        return image.copy()

    @staticmethod
    def calculate_sobel_magnitude_image(image):
        # ToDo convert image to grayscale and blur the result
        # https://docs.opencv.org/3.2.0/df/d9d/tutorial_py_colorspaces.html
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('gej', grey)


        blur = cv2.blur(grey, SOBEL_BLUR_KERNEL_SHAPE).astype('uint8')
        # cv2.imshow('blur', blur)

        # cv2.waitKey(0)

        # ToDo calculate gradients
        # https://docs.opencv.org/3.2.0/d5/d0f/tutorial_py_gradients.html
        sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=5)

        sobelxabs = np.absolute(sobelx)
        sobelyabs = np.absolute(sobely)

        # ToDo process gradients into one
        # https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#convertscaleabs
        # https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html?highlight=addweighted#addweighted

        combined = cv2.addWeighted(sobelxabs, 1/2, sobelyabs, 1/2, 0)

        # ToDo threshold edges to get most important ones
        ret, tresh1 = cv2.threshold(combined, 127, 255, cv2.THRESH_BINARY)

        cv2.imshow('tresh1', tresh1)

        # https://docs.opencv.org/3.1.0/d7/d4d/tutorial_py_thresholding.html

        cv2.waitKey(0)
        return image.copy()

a = cv2.imread('nemo.jpg')
ImageProcessor.calculate_sobel_magnitude_image(a)