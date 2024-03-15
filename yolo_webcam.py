from ultralytics import YOLO
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

model = YOLO

while True :
    success , img = cap.read()
    cv2.imshow("webcam", img)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()