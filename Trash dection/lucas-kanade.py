import numpy as np
import cv2
from ultralytics import YOLO

model = YOLO('best.pt')

feature_params = dict(maxCorners=100,
                      qualityLevel=0.3,
                      minDistance=7,
                      blockSize=7)


lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


color = np.random.randint(0, 255, (100, 3))


path = input("Enter Video Path:\n")
cap = cv2.VideoCapture(path)

ret, old_frame = cap.read()
if not ret:
    print("Cannot read video file")
    exit()

old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

mask = np.zeros_like(old_frame)

def detect_objects(frame):
    centers = []
    result = model.predict(frame, save=False)
    boxes = result[0].boxes.xywh
    cls = result[0].boxes.cls

    for box in boxes:
        x = int(box[0])
        y = int(box[1])
        centers.append((x, y))
    return centers, len(cls)


centers, clslen = detect_objects(old_frame)
if len(centers) == 0:
    print("No objects detected in the first frame")
    exit()

oldclslen = clslen
p0 = np.array(centers, dtype=np.float32).reshape(-1, 1, 2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    new_centers, clslen = detect_objects(frame)



    for center in new_centers:
        if not any(np.linalg.norm(center - old_center) < 100 for old_center in p0.reshape(-1, 2)) and clslen != oldclslen:
            p0 = np.vstack((p0, np.array(center, dtype=np.float32).reshape(-1, 1, 2)))


    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    oldclslen = clslen


    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
            frame = cv2.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)

        img = cv2.add(frame, mask)
    else:
        img = frame

    cv2.imshow('frame', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2) if p1 is not None else p0

cv2.destroyAllWindows()
cap.release()
