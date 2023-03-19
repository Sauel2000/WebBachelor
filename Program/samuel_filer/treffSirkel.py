import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image


path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"
img = cv.imread(path)
image = Image.open(path)
columnPixels = (img.shape[0])
widthPixels =(img.shape[1])
T = [[0,0],[0,0]]
#img[110,100] = [0,0,255]
#img[111,100] = [0,0,255]
shotValue = 0
for y in range(columnPixels):
    #print("y", y)
    for x in range(widthPixels):
        #print("x",x)
        if img[y,x,0] == 255 and img[y,x,1] == 0 and img[y,x,2] == 0:
            T.insert(shotValue,[y,x])
            shotValue += 1
            #img[y,x] = [255,255,255]
pixval = list(image.getdata()) 
for x in range(shotValue):
    print(T[x][0])
    print(x)
#print ("Y", T[0][0],"X",T[0][1])
#print(pixval)
#ball = img[T[0][0]:T[shotValue-1][shotValue-1],T[0][1]:T[shotValue-1][shotValue-1]]
#img[273:333, 100:160] = ball
cv.imshow("Image", img)
cv.waitKey(0)

cx = 0
cy = 0
center_px = img[cy,cx]
#print(center_px)
