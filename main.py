from ultralytics import YOLO
import cv2

model = YOLO(r"C:\Users\jalal\yolov8n.pt")

results = model(r"C:\Users\jalal\Pictures\persons.jpg",show=True)

print(results)

cv2.waitKey(0)