import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/AutenC.jpg"
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"

img = cv.imread(path)

img[26,289]=(0,0,255) #Vertikale rød 
img[557,289]=(0,0,255) #Vertikale rød
img[292,14]=(255,0,0)  #Horizontal blå markeringer
img[297,564]=(255,0,0)  #Horizontal blå markeringer 


'''
#############################################################
#This part is not needed when Jehad part is finished
img[12,291]=(0,0,255) #Vertikale rød 
img[569,291]=(0,0,255) #Vertikale rød
img[292,5]=(255,0,0)  #Horizontal blå markeringer
img[292,574]=(255,0,0)  #Horizontal blå markeringer
#############################################################
'''
columnPixels = (img.shape[0])   # Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler
print(columnPixels,widthPixels)
#############################################################
#This part is only to demonstrate
VerticalAxisLengthColor = (255,0,0) #BGR -> BLUE    
HorizontalAxisLengthColor = (0,255,0) #BGR -> GREEN
#############################################################


window_name = "Demonstration Window"

verticalAxisPoint = []
horizontalAxisPoint = []
#Two colors to look for 
VerticalSearchColor = (0, 0, 255 ) #RED COLOR IN BGR(Blue,Green,Red)
HorisontalSearchColor = (255 , 0, 0) #Blue COLOR 
vertAxisPixel = 0
horiAxisPixel = 0

for x in range(columnPixels):
    for y in range(widthPixels):
        if (img[x,y,0] == VerticalSearchColor[0]  and img[x,y,1] == VerticalSearchColor[1] and img[x,y,2] == VerticalSearchColor[2]):
            verticalAxisPoint.insert(vertAxisPixel,[x,y])
            vertAxisPixel += 1
            
        if (img[x,y,0] == HorisontalSearchColor[0]  and img[x,y,1] == HorisontalSearchColor[1] and img[x,y,2] == HorisontalSearchColor[2]):
            horizontalAxisPoint.insert(horiAxisPixel,[x,y])
            horiAxisPixel +=1
cv.imwrite(savePath,img)

pixelHeightLen=0
pixelWidthLen = 0
print(verticalAxisPoint[-1][0],"Vertical", verticalAxisPoint[0][1], "Vertical2", horizontalAxisPoint[-1][1], "Horsontal", horizontalAxisPoint[0][0])
pixelVertically= 48 /(verticalAxisPoint[-1][0]-verticalAxisPoint[0][0]) #Piksel høyde i cm

pixelHorisontal= 48 / (horizontalAxisPoint[-1][1]-horizontalAxisPoint[0][1]) #Piksel bredde i cm
print(pixelHorisontal,"PIXELS")

startVerticalCoord = verticalAxisPoint[0][0]
startHorizontalCoord = horizontalAxisPoint[0][1]
endVerticalCoord = verticalAxisPoint[-1][0]

endHorizontalCoord = horizontalAxisPoint[-1][1]
print(endVerticalCoord,endHorizontalCoord,)

print(startVerticalCoord,endVerticalCoord,"Vertical",startHorizontalCoord,endHorizontalCoord)
#round((566-9)/2)+9
for x in range(startVerticalCoord,round(endVerticalCoord) ,1):
    pixelHeightLen =pixelHeightLen + pixelVertically
    img[x,verticalAxisPoint[0][1]]=VerticalAxisLengthColor

#

for y in range(startHorizontalCoord,round(endHorizontalCoord),1):
    pixelWidthLen=pixelWidthLen + pixelHorisontal
    img[horizontalAxisPoint[0][0],y]=HorizontalAxisLengthColor
centerVertical = pixelHeightLen
centerHorizontal = pixelWidthLen
print(centerVertical,centerHorizontal)
print(pixelHeightLen/2,"Real cm in picture between the vertical axis coord")
print(pixelWidthLen/2, "Real cm between horisontal points")
cv.imwrite('test.png',img)
# Displaying the image 
cv.imshow(window_name, img)

cv.waitKey(0)

