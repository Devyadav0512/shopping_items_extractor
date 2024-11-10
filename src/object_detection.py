# src/object_detection.py

import torchvision.models.detection as models
import torch
from PIL import Image
from torchvision import transforms

def load_detection_model():
    # Use the weights parameter instead of pretrained
    model = models.fasterrcnn_resnet50_fpn(weights=models.FasterRCNN_ResNet50_FPN_Weights.DEFAULT)
    model.eval()
    return model

def detect_objects_on_frames(frames, model):
    detections = []
    for frame_path in frames:
        # Open and convert image to RGB
        image = Image.open(frame_path).convert("RGB")
        
        # Transform the image to tensor and add a batch dimension
        image_tensor = transforms.ToTensor()(image).unsqueeze(0)
        
        # Perform object detection
        with torch.no_grad():
            output = model(image_tensor)

        # Store detections in a dictionary
        frame_detections = {
            'boxes': output[0]['boxes'],
            'labels': output[0]['labels'],
            'scores': output[0]['scores']
        }

        detections.append((frame_path, frame_detections))
    
    return detections
