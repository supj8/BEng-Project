import tifffile
from PIL import Image
import os
from scipy.ndimage import gaussian_filter
import numpy as np
from natsort import natsorted

output_dir = '/Users/joshua/Desktop/Final Year Project/Code/yolo classification/Experiments/SETTING 2 EXPERIMENTS/Experiment 15 Baseline/3-10 centre slices'

image_dir = '/Users/joshua/Desktop/Final Year Project/Code/yolov8_test/main/runs/detect/predict'

squash_factor = 11  # Number of slices to be squashed
counter = 0


# Read the 3D TIFF file
# with tifffile.TiffFile('/Users/joshua/Desktop/Final Year Project/Code/failure_or_not_slice/average data/3.5-Merged_Tiff.tif') as tif:
#     array_3d = tif.asarray()

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

specimen_number = '3.10'

squashed_images = []

images_array = load_images_to_array(image_dir)

# for i in range (0, len(images_array), squash_factor):
#     counter = counter + 1
#     end = i + squash_factor
#
#     # if end > len(images_array):
#     #     break
#

center_slices = range(squash_factor // 2, len(images_array), (squash_factor // 2) + 1)

for center_slice in center_slices:
    squash_slice = images_array[center_slice]
    squashed_images.append(squash_slice)

# for center_slice in center_slices:
#     start = max(0, center_slice - squash_factor // 2)
#     end = min(len(images_array), center_slice + squash_factor // 2 + 1)
#
#     group_size = end - start  # Calculate the actual size of the current group
#
#     squash_slice = np.mean(images_array[start:end], axis=0)
#     squashed_images.append(squash_slice)

# for i, img_array in enumerate(squashed_images):
#     img = Image.fromarray(img_array.astype(np.uint32))  # Convert to PIL Image
#     img.save(os.path.join(output_dir, f'{specimen_number}_squashed_image_{i+1}.png'))
#     print(f'{specimen_number} Squashed image {i+1} saved.')

for i, img_array in enumerate(squashed_images):
    img = Image.fromarray(img_array.astype(np.uint32))  # Convert to PIL Image
    img.save(os.path.join(output_dir, f'{specimen_number}_squashed_image_{i+1}.png'))
    print(f'{specimen_number} Squashed image {i+1} saved.')


