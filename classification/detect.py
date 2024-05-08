from ultralytics import YOLO

# Load a model
model = YOLO('/Users/joshua/Desktop/Final Year Project/Code/yolo classification/runs/classify/experiment 6/weights/last.pt')  # load a custom model

inference_source = '/Users/joshua/Desktop/Final Year Project/Code/failure_or_not_slice/gaussian data 2/3-3 average squash'
#
# # Predict with the model
results = model(inference_source)  # predict on an image
failure_counter = 0
total_counter = 0
#
for result in results:
    top_class = result.probs.top1
    top_confidence = result.probs.top1conf
    image_path = result.path
    total_counter = total_counter+1

    if top_class == 0:  # Assuming 'failure' is the class label for failure images
        print(f"Image {image_path} was predicted as a failure with confidence {top_confidence:.2f}")
        failure_counter = failure_counter+1

print(failure_counter)
print(total_counter)


# Export the model
# model.export(format='onnx')

# metrics = model.val(source='/Users/joshua/Desktop/Final Year Project/Code/failure_or_not_slice/gaussian data 2/3-11 intensity changed squashed')
