import torch

# Model
from models.common import Detections

model = torch.hub.load('ultralytics/yolov5', 'yolov5l')  # or yolov5n - yolov5x6, custom

# Images
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results: Detections = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
