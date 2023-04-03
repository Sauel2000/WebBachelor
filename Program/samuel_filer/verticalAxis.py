import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image



path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/bright-image.png"
path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"

path2= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/A.jpg"

savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"

img = cv.imread(path2)
image = Image.open(path)

columnPixels = (img.shape[0])
widthPixels =(img.shape[1]) 

VerticalAxisLengthColor = (255,0,0) #BGR -> BLUE 
HorisontalAxisLengtColor = (0,255,0) #BGR -> GREEN
LengthAxis = 40     #Length between axis in reality


# Red color in BGR

colorCircle = (0,0,255)
radius = 2
window_name = "Chil"
thickness=1
shotCoord = []
T = [[0,0],[0,0]]
#RGB = (27,41,7)
color = (20, 100, 20 )
tempX = 0
tempY = 0
vertAxisPixel = 0
indexControl=0
j = 0

for y in range(columnPixels):
    #print("y", y)
    for x in range(widthPixels):
        #print("x",x)
        if (img[y,x,0] <= color[0]  and img[y,x,1] <= color[1] and img[y,x,2] >= color[2]):
            shotCoord.insert(vertAxisPixel,[x,y])
            print(x,y)
            vertAxisPixel += 1
            j = x
            #print(j,x)

#print(vertAxisPixel)
#print(shotCoord[vertAxisPixel][0])
cv.imwrite(savePath,img)
print(len(shotCoord),"Coords")

#print(shotCoord[0][1],shotCoord[1][1])
#print(shotCoord[0][2],shotCoord[1][2])
for x in range(len(shotCoord)):
    img = cv.circle(img, (shotCoord[x][0],shotCoord[x][1]), 10 , colorCircle, thickness)

#img[34,594]= [0,255,0]

#print(img[34,594])
cmLen=0
pixel= 11.27897350993377
print(shotCoord[0][1])
for x in range(15, 465,11):
    #print(x)
    cmLen+=1
    img[x,270]=[0,255,0]
print(cmLen)
#img = cv.circle(img, (34,97), 3 , colorCircle, thickness)

#print(vertAxisPixel)
img = cv.circle(img, (270,226), 229 , (255,0,0), thickness)
# Displaying the image 
cv.imshow(window_name, img)
cv.waitKey(0)

