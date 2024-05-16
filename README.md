## Getting set up
Install requirements.txt to a local venv to retrieve required modules

## Data Processing
1) 3d_image_extract_2d.py - extracts individual slices from a .tiff file
2) contrast.py - changes the contrast of images
3) squashing_gaussian.py - applies the gaussian compression across slices
4) squashing_average.py - applies the average compression across slices

## Classification
1) train.py - trains YOLOv8s-cls on your data. Also contains comet_ml integration for tracking analytics
2) detect.py - allows user to deploy a trained classification model and test it on images

