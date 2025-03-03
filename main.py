from ultralytics import YOLO
from ultralytics.nn.tasks import DetectionModel
from phone_call import call_to_number
import torch
import cv2

model = DetectionModel()
torch.load('best.pt', weights_only=False)
called = False


model = YOLO('best.pt')

model.overrides['conf'] = 0.25  # NMS confidence threshold
model.overrides['iou'] = 0.45  # NMS IoU threshold
model.overrides['max_det'] = 1000  # maximum number of detections per image


cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model(frame)

        if results[0].boxes.shape[0] > 0:
            if not called:
                call_to_number(phone_number="77767301903")
                called = True

        annotated_frame = results[0].plot()

        cv2.imshow("YOLOv8 Inference", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

