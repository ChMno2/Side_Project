# -*- coding: utf-8 -*-
"""ANPR - Tutorial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jjtqfz4m9xO7Cfs2jqBkOWIEkTYyJ80z

## 0. Install and Import Dependencies
"""

!pip install easyocr
!pip install imutils

import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr

"""## 1. Read in Image, Grayscale and Blur"""

img = cv2.imread('image4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#to gray
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

from google.colab import drive
drive.mount('/content/drive')

"""## 2. Apply filter and find edges for localization"""

bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #應用雙邊濾波器以減少噪聲
edged = cv2.Canny(bfilter, 30, 200) #Edge detection
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

"""## 3. Find Contours and Apply Mask"""

keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# #cv2.RETR_TREE：輪廓檢索模式。cv2.RETR_TREE 表示檢索所有輪廓並重建輪廓之間的完整樹狀結構。
# cv2.CHAIN_APPROX_SIMPLE：輪廓近似方法。這個方法僅保存輪廓的端點，從而壓縮輪廓。
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
#選擇面積最大的前 10 個輪廓

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)#對輪廓進行多邊形逼近
    if len(approx) == 4:
        location = approx
        break

location

mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))

(x,y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray[x1:x2+1, y1:y2+1]

plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))

"""## 4. Use Easy OCR To Read Text"""

reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)
result

"""## 5. Render Result"""

text = result[0][-2]
font = cv2.FONT_HERSHEY_SIMPLEX
res = cv2.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))

