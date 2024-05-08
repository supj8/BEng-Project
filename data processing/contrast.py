import cv2
import os
from natsort import natsorted
import numpy as np
from pylab import array, plot, show, axis, arange, figure, uint8

# # Image data
# image = cv2.imread('/Users/joshua/Desktop/Final Year Project/Code/failure_or_not_slice/gaussian data 2/3-2_2D/3-2_slice_0.png', -1) #-1 is for reading the image unchanged



image_dir = '/Users/joshua/Desktop/Final Year Project/Code/failure_or_not_slice/gaussian data 2/3-2_2D'

output_dir = '/Users/joshua/Desktop/Final Year Project/Code/failure_or_not_slice/gaussian data 2/3-2 2D intensity changed'

image_files = os.listdir(image_dir)
image_files = natsorted(image_files)
images_list = []

# # Print basic information about the image
# print("Image shape:", image.shape)
# print("Image data type:", image.dtype)

for filename in image_files:
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Check for image files
        filepath = os.path.join(image_dir, filename)
        image = cv2.imread(filepath, -1)

        maxIntensity = 65535  # Maximum intensity for 16-bit per pixel images

        # Parameters for manipulating image data
        a = 1
        b = 1

        # Decrease intensity such that
        # dark pixels become much darker,
        # bright pixels become slightly dark
        new_image = (image / (maxIntensity / a)) ** 2 * (maxIntensity / b)

        # a and b both equal 1. So the above line is normalizing the image pixels (divide by max intensity) and then squares it. Darker pixels will go to a much lower value where as brighter values wont lose as much.
        # then multiplied again by max intensity to scale up, otherwise all pixels will be completely dark for a uint16 image
        # might be interesting to graph x^2 curve to explain why darker pixels go darker

        # Convert to uint16 data type
        new_image_uint16 = new_image.astype(np.uint16)

        # Save the adjusted image
        cv2.imwrite(os.path.join(output_dir, filename), new_image_uint16)

