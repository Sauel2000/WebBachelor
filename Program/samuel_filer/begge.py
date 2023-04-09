import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/A.jpg"
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"

img = cv.imread(path)
#############################################################
#This part is not needed when Jehad part is finished
img[60,270]=(0,0,255) #Vertikale rød 
img[508,270]=(0,0,255) #Vertikale rød
img[273,43]=(255,0,0)  #Horizontal blå markeringer
img[273,500]=(255,0,0)  #Horizontal blå markeringer
#############################################################
columnPixels = (img.shape[0])   # Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler

#############################################################
#This part is only to demonstrate
VerticalAxisLengthColor = (255,0,0) #BGR -> BLUE    
HorisontalAxisLengtColor = (0,255,0) #BGR -> GREEN
#############################################################
'''
Activate this part only to mark hits
# Red color in BGR
colorCircle = (0,0,255)
radius = 2

Circlethickness=1
'''
window_name = "Demonstration Window"

verticalAxisPoint = []
horisontalAxisPoint = []
#Two colors to look for 
VerticalSearchColor = (0, 0, 255 ) #RED COLOR IN BGR(Blue,Green,Red)
HorisontalSearchColor = (255,0,0) #Blue COLOR 
vertAxisPixel = 0
horiAxisPixel = 0

for y in range(columnPixels):
    for x in range(widthPixels):
        if (img[y,x,0] == VerticalSearchColor[0]  and img[y,x,1] == VerticalSearchColor[1] and img[y,x,2] == VerticalSearchColor[2]):
            verticalAxisPoint.insert(vertAxisPixel,[x,y])
            vertAxisPixel += 1
            
        if (img[y,x,0] == HorisontalSearchColor[0]  and img[y,x,1] == HorisontalSearchColor[1] and img[y,x,2] == HorisontalSearchColor[2]):
            horisontalAxisPoint.insert(horiAxisPixel,[x,y])
            horiAxisPixel +=1
            
cv.imwrite(savePath,img)

shootingTargetCenterYCoord = int((verticalAxisPoint[-1][1]-verticalAxisPoint[0][1])/2 + verticalAxisPoint[0][1])
print ( shootingTargetCenterYCoord, "Pixel Y")

cmLen=0
cmLenHorizontal = 0

pixel= 40/(verticalAxisPoint[-1][1]-verticalAxisPoint[0][1]) #Piksel høyde i cm

pixelHorisontal= 40 / (horisontalAxisPoint[-1][0]-horisontalAxisPoint[0][0]) #Piksel bredde i cm


end = verticalAxisPoint[-1][1]
end1 = horisontalAxisPoint[-1][0]


for x in range(verticalAxisPoint[0][1], end,1):
    cmLen =cmLen + pixel
    img[x,verticalAxisPoint[0][0]]=VerticalAxisLengthColor
    
for x in range(horisontalAxisPoint[0][0], end1,1):
    cmLenHorizontal=cmLenHorizontal + pixelHorisontal
    img[horisontalAxisPoint[0][1],x]=HorisontalAxisLengtColor

print(cmLen,"Real cm in picture between the vertical axis coord")
print(cmLenHorizontal, "Real cm between horisontal points")

# Displaying the image 
cv.imshow(window_name, img)
cv.waitKey(0)

