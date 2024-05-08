import tifffile
from PIL import Image, ImageEnhance
import os
from scipy.ndimage import gaussian_filter
import numpy as np
from natsort import natsorted
import cv2
import matplotlib.pyplot as plt

output_dir = '/Users/joshua/Desktop/test folder'

image_dir = '/Users/joshua/Desktop/Final Year Project/Code/failure_or_not_slice/gaussian data 2/3-13 2D intensity changed'

# Read the 3D TIFF file
# with tifffile.TiffFile('/Users/joshua/Desktop/Final Year Project/Code/failure_or_not_slice/ALL SLICE DATA/3.2-Merged_Tiff.tif') as tif:
#     array_3d = tif.asarray()

specimen_number = '3.13'

sigma = 3
squash_factor = 11 # Number of slices to be squashed
counter = 0

def load_images_to_array(image_dir):
    images_list = []

    image_files = os.listdir(image_dir)
    image_files = natsorted(image_files)

    for filename in image_files:
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Check for image files
            filepath = os.path.join(image_dir, filename)
            image = Image.open(filepath)
            image_array = np.array(image)
            images_list.append(image_array)

    # Stack images along the first axis to create a 3D array
    if images_list:
        images_array = np.stack(images_list, axis=0)
    else:
        raise ValueError("No image files found in the directory.")

    return images_array

def gaussian_squash(squash_factor, sigma):
    r = np.arange(-(squash_factor // 2), squash_factor // 2 + 1)
    weights = np.exp(-0.5 * (r / sigma) ** 2)
    weights /= weights.sum()  # Normalization to preserve original intensity

    return weights

def gaussian_squash_images(array_3d, squash_factor, sigma):
    squashed_images = []
    center_slices = range(squash_factor // 2, len(array_3d), (squash_factor // 2) + 1)

    num_groups_to_visualize = 3

    # Iterate over the first few squash groups
    for i in range(num_groups_to_visualize):
        center_slice = center_slices[i]
        print(center_slice)

        start = max(0, center_slice - squash_factor // 2)  # Calculate the starting index for the group
        end = min(len(array_3d), center_slice + squash_factor // 2 + 1)  # Calculate the ending index for the group
        print(start)
        print(end)

        # Calculate weights for the current group
        weights = gaussian_squash(end - start, sigma)

        # Plot the weights
        plt.plot(range(start, end), weights, label=f'Squash Group {i + 1}')

    # Customize the plot
    plt.title('Gaussian Squash Distribution for the First 3 Squash Groups')
    plt.xlabel('Slice Number')
    plt.ylabel('Weight')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

    for center_slice in center_slices:
        start = max(0, center_slice - squash_factor // 2)
        end = min(len(array_3d), center_slice + squash_factor // 2 + 1)

        group_size = end - start  # Calculate the actual size of the current group
        weights = gaussian_squash(group_size, sigma)  # Calculate weights based on the group size

        weighted_slices = array_3d[start:end] * weights[:group_size, np.newaxis, np.newaxis]
        squashed_image = np.sum(weighted_slices, axis=0)
        squashed_images.append(squashed_image)

    return squashed_images

    img = Image.fromarray(squashed_slice.astype(np.uint8))
    img.save(os.path.join(output_dir, f'squashed_slice_{counter}_filtered.png'))
    print(f'squashed_slice_{counter} filtered and saved')

images_array = load_images_to_array(image_dir)

squashed_images = gaussian_squash_images(images_array, squash_factor, sigma)

for i, img_array in enumerate(squashed_images):

    img = Image.fromarray(img_array.astype(np.uint32))  # Convert to PIL Image

    img.save(os.path.join(output_dir, f'{specimen_number}_squashed_image_{i+1}.png'))
    print(f'{specimen_number} Squashed image {i+1} saved.')


def plot_gaussian_weights(r, weights):
    plt.plot(r, weights, marker='o', linestyle='-')
    plt.title('Gaussian Weights')
    plt.xlabel('r')
    plt.ylabel('Weight')
    plt.grid(True)
    plt.show()


def visualize_squash_distribution(array_3d, squash_factor, sigma, num_groups_to_visualize=3):
    """
    Visualize the distribution of weights for the first few squash groups.

    Parameters:
        array_3d (ndarray): The 3D array of image slices.
        squash_factor (int): The number of slices to squash together.
        sigma (float): The standard deviation for the Gaussian distribution.
        num_groups_to_visualize (int, optional): The number of squash groups to visualize. Default is 3.
    """


    center_slices = [squash_factor // 2 + i * (squash_factor//2 + 1) for i in range(num_groups_to_visualize)]

    # Iterate over the first few squash groups
    for i in range(num_groups_to_visualize):
        center_slice = center_slices[i]
        print(center_slice)

        start = max(0, center_slice - squash_factor // 2)  # Calculate the starting index for the group
        end = min(len(array_3d), center_slice + squash_factor // 2 + 1)  # Calculate the ending index for the group
        print(start)
        print(end)

        # Calculate weights for the current group
        weights = gaussian_squash(end - start, sigma)

        x_values = np.arange(start, end)  # Generate x-values for the current group
        plt.plot(x_values, weights, label=f'Squash Group {i + 1}')

    # Customize the plot
    plt.title('Gaussian Squash Distribution for the First Few Squash Groups')
    plt.xlabel('Slice Offset')
    plt.ylabel('Weight')
    plt.legend()


    # Set x-axis ticks to have intervals of 1
    x_ticks = np.arange(0, len(array_3d), 1)  # Generate x-ticks for the entire range
    plt.xticks(x_ticks)

    # Show the plot
    plt.show()

# weights = gaussian_squash(squash_factor, sigma)

# visualize_squash_distribution(images_array, squash_factor, sigma)

# Call the function to plot Gaussian weights
# plot_gaussian_weights(np.arange(-(squash_factor // 2), squash_factor // 2 + 1), weights)











