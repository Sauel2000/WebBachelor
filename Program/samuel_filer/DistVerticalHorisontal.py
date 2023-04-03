import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image

path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/bright-image.png"
path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"

path2= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ABCop.jpg"

savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"

img = cv.imread(path1)

columnPixels = (img.shape[0])
widthPixels =(img.shape[1]) 

realDistanceBetweenHorizontalAxis = 40  #Cm
img[503,33]=(0,255,0)
img[503,1016]=(0,255,0)
VerticalAxisLengthColor = (255,0,0) #BGR -> BLUE 
HorisontalAxisLengtColor = (0,255,0) #BGR -> GREEN

# Red color in BGR
colorCircle = (0,0,255)
radius = 90
window_name = "Chil"
Circlethickness=1
verticalAxisPoint = []
#RGB = (27,41,7)
color = (0, 255, 0 )
vertAxisPixel = 0
indexControl=0
j = 0

for y in range(columnPixels):
    for x in range(widthPixels):
        if (img[y,x,0] == color[0]  and img[y,x,1] == color[1] and img[y,x,2] == color[2]):
            verticalAxisPoint.insert(vertAxisPixel,[x,y])
            print(x,y)
            vertAxisPixel += 1
            j = x
            
cv.imwrite(savePath,img)
print(len(verticalAxisPoint),"Coords")

cmLen=0
pixel= realDistanceBetweenHorizontalAxis/(verticalAxisPoint[-1][0]-verticalAxisPoint[0][0]) #Piksel høyde i cm
print(pixel,"PIXEL")
end = verticalAxisPoint[-1][0]

print(verticalAxisPoint[0][1])

for x in range(verticalAxisPoint[0][0], end,1):
    #print(x)
    cmLen =cmLen + pixel
    img[verticalAxisPoint[0][1],x]=[0,255,0]

print(cmLen,"Real cm in picture between the vertical axis coord")
print(end)
print(verticalAxisPoint[-1][1])
shootingTargetCenterYCoord = int((verticalAxisPoint[-1][0]-verticalAxisPoint[0][0])/2 + verticalAxisPoint[0][1])
img = cv.circle(img, (525,503), 495 , (255,0,0), Circlethickness)
# Displaying the image 
cv.imshow(window_name, img)
cv.waitKey(0)

