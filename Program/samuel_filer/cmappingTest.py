import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from PIL import Image

path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/bright-image.png"
path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"
img = cv.imread(path)


#print(img.size[0])
#BGR
SearchColor = (255, 0, 0)
colorCircle = (0,255,0)
CircleRadius = 10
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

for x in range(shotValue):
    print(T[x])   
print(shotValue)

print(img[812,527])
print(float(img.shape[1]/img.shape[0]))

#plt.rcParams["figure.figsize"] = [img.shape[0],img.shape[1]]
#print(img.shape[0],img.shape[1])
#print(img[236,544])
plt.imshow(img, origin='upper', extent=[0,5,0,5], aspect=float(img.shape[1]/img.shape[0]),filternorm=True )
plt.show()
#cv.imshow("test",img)
#cv.waitKey(0)