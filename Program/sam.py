import numpy as np
import sys
import cv2 as cv
img = cv.imread('skyteskive.jpg',0)
img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)



