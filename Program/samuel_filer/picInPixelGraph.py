import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image


#path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/litenPX.jpg"
path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/Skyteskive.jpg"
path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/testbild.png"
img = cv.imread(path1)
#BGR
SearchColor = (255,0,0)
colorCircle = (0,255,0)
CircleRadius = 100
window_name = "Chil"
thickness=1
T = []
shotValue = 0
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        if img[y,x,0] == SearchColor[0] and img[y,x,1] == SearchColor[1] and img[y,x,2] == SearchColor[2]:
            #@param index,2D values y=height, x=width
            T.insert(shotValue,[x,y])
            
            img = cv.circle(img, (x,y), CircleRadius, colorCircle, thickness)
            shotValue += 1

cv.imwrite(savePath,img)
    
for x in range(shotValue):
    print(T[x])   
print(shotValue)
#print(img.shape[0],img.shape[1])
#print(T[0][1])
#print(img[T[0][1]])
#print(img[382,329])

cv.imshow(window_name, img)
cv.waitKey(0)

