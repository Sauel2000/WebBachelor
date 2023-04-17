d=30 #Enter The distance between Chess pieces here to Calibrate


import math
import numpy as np
import cv2
import time
from matplotlib import pyplot as plt
import imutils
from imutils import perspective

def getmp(image):
    global low_H
    global high_H
    gra = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = gra[:,:,2]
    gray = cv2.GaussianBlur(gray, (7,7), 0)
    gray = cv2.GaussianBlur(gray, (7,7), 0)
    edged = cv2.inRange(gray, low_H, high_H)
    edged = cv2.dilate(edged, None, iterations=10)
    edged = cv2.erode(edged, None, iterations=5)
    edged = cv2.dilate(edged, None, iterations=10)
    edged = cv2.erode(edged, None, iterations=30)
    edged = cv2.dilate(edged, None, iterations=40)
    ff=np.where(edged>50)
    a1=np.mean(ff[1])  
    return a1

lo=cv2.imread('a30.jpg')
ro=cv2.imread('b30.jpg')
lp=getmp(lo)
lr=getmp(ro)
p=abs(lp-lr)
dpp=d*p
with open("DoNotDelete.txt",'w') as f:
   s=str(dpp)
   f.write(s)



      
      
