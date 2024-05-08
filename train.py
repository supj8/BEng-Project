from ultralytics import YOLO
from comet_ml import Experiment, ExistingExperiment

## Create an experiment with your api key
# experiment = ExistingExperiment(

experiment = Experiment(
    api_key="bTv8M3OrADs1YmZWK5sdJxuD5",
    project_name="final-project-classification",
    workspace="supj8",
    #experiment_key="4e93f441389a4295afc78fc03d855177"
)

experiment.set_name("test1")

model = YOLO('yolov8l-cls.pt')

# save_path = '/Users/joshua/Desktop/Final Year Project/Code/yolo classification/Experiments/Test/Results'

data_path = '/Users/joshua/Desktop/Final Year Project/Code/yolo classification/Experiments/SETTING 2 EXPERIMENTS/Experiment 16 1to1/data'

# model.train(data="/Users/joshua/Desktop/Final Year Project/Code/yolov8/main/EXPERIMENTS/EXPERIMENT 1 (ALL SLICES) (CORRECT DATA)/TRAIN DATA/data.yaml", epochs=300, imgsz = 640, project = save_path, patience = 100)

model.train(data = data_path, epochs = 150, imgsz = 640, patience=0)

#metrics = model.val()




