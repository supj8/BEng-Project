import tifffile
from PIL import Image
import os
from scipy.ndimage import gaussian_filter

output_dir = '/Users/joshua/Desktop/Final Year Project/Code/failure_or_not_slice/ALL SLICE DATA/3-13_2D'

# sigma = 1


# Read the 3D TIFF file
with tifffile.TiffFile('/Users/joshua/Desktop/Final Year Project/Code/failure_or_not_slice/ALL SLICE DATA/3.13-Merged_Tiff.tif') as tif:
    array_3d = tif.asarray()

specimen = '3-13'

# Iterate over each slice
for i, slice_2d in enumerate(array_3d):
    # Apply Gaussian filter
    # filtered_slice = gaussian_filter(slice_2d, sigma=sigma)

    # Convert the slice to an image
    img = Image.fromarray(slice_2d)

    # Save the image
    img.save(os.path.join(output_dir, f'{specimen}_slice_{i}.png'))  # You can change the format to '.jpg', '.tiff', etc.
    print(f'slice {i} saved')