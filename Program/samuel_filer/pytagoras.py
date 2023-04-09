import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math
from ImagInfoClass import*


path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ABCop.jpg"

savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"

img = cv.imread(path1)

#############################################################
#This part is not needed when Jehad part is finished
img[8,291]=(0,0,255) #Vertikale rød 
img[565,291]=(0,0,255) #Vertikale rød
img[292,5]=(255,0,0)  #Horizontal blå markeringer
img[292,574]=(255,0,0)  #Horizontal blå markeringer
#############################################################

img[9,291]=(0,255,0)
img[566,292]=(0,255,0)
img[100,100]=(0,255,0)
img[50,50]=(0,255,0)

test = PixelSizeSys()
pixelInfo = test.getAxisCoords(img)
pixelHor = pixelInfo[0]
pixelVert = pixelInfo[1]
pixelDiagonal = pixelInfo[2]

print(pixelInfo, "Diagonal")

HitCalibSys = PixelSizeSys()

pixel = HitCalibSys.getAxisCoords(img)

 
print (pixel)




columnPixels = (img.shape[0])
widthPixels =(img.shape[1]) 
#print(columnPixels, widthPixels)

VerticalAxisLengthColor = (255,0,0) #BGR -> BLUE 
HorisontalAxisLengtColor = (0,255,0) #BGR -> GREEN
LengthAxis = 40     #Length between axis in reality


# Red color in BGR
colorCircle = (0,0,255)
radius = 2
window_name = "Chil"
thickness=1
shotCoord = []
color = (0, 255, 0 )
vertAxisPixel = 0

for y in range(columnPixels):
    #print("y", y)
    for x in range(widthPixels):
        #print("x",x)
        if (img[y,x,0] == color[0]  and img[y,x,1] == color[1] and img[y,x,2] == color[2]):
            shotCoord.insert(vertAxisPixel,[x,y])
            #print(x,y)
            vertAxisPixel += 1


for x in range(len(shotCoord)):
    img = cv.circle(img, (shotCoord[x][0],shotCoord[x][1]), 10 , colorCircle, thickness)

cmLen=0
#pixel= 11.27897350993377
print(shotCoord, "Coords")



shotCoordinates = shotCoord 



a = []
listIndex = 0
j = 0
pixelCountDia = 0

distListHor =[]
distList =[]
listIndex = 0
h=1

for index , s in reversed(list(enumerate(shotCoord))):
     #print(index,"index", s[0],"Shoots",s[1])
     for x in range(0,len(shotCoord)-h,1):
         #print(shotCoord[x][0],shotCoord[x][1],"X",s)
         distVert = abs(s[0]-shotCoord[x][0])**2
         distHor = abs(s[1]-shotCoord[x][1])**2
         distDia =((distVert+distHor)**(1/2))
         if (x == (len(shotCoord)-h)-1):
            h+=1
         for j in range(0, round(distDia)):
            pixelCountDia += pixelDiagonal
            
            if (j == round(distDia)-1):
                distList.insert(listIndex,pixelCountDia)
                print("Virkelige distansen fra skudd",x,"til skudd",index,"er:", distList[listIndex],shotCoord[x],s )
                listIndex += 1
                pixelCountDia = 0

cv.imshow(window_name, img)
cv.waitKey(0)

