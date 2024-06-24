import cv2
import numpy as np
from ultralytics import YOLO

path = input("Enter Video Path:\n")
cap = cv2.VideoCapture(path)

model = YOLO(r'C:\Users\chanmuen\Downloads\trash.v2i.yolov8\runs\detect\train8\weights\best.pt')
state = ['car', 'license', 'trash-RlAJ']


while True:
    ret, frame = cap.read()
    
    if ret == True:
        result = model.predict(frame, save=False)
        boxes = result[0].boxes.xyxy
        cls = result[0].boxes.cls
        n = 0

        for box in boxes:
            x1 = int(box[0])
            y1 = int(box[1])
            x2 = int(box[2])
            y2 = int(box[3])

            cv2.rectangle(frame ,(x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, '{}'.format(state[int(cls[n])]), (x1,y1), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            n = n + 1
        cv2.imshow(' ',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
    cv2.waitKey(1)
