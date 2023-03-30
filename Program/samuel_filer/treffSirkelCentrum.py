import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image



path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/bright-image.png"
path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"
path2= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/RedMarkPaper.jpg"
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"

img = cv.imread(path2)
image = Image.open(path)
#img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print(img[236,544])
columnPixels = (img.shape[0])
widthPixels =(img.shape[1]) 

VerticalAxisLengthColor = (255,0,0) #BGR -> BLUE 
HorisontalAxisLengtColor = (0,255,0) #BGR -> GREEN
LengthAxis = 40     #Length between axis in reality

# Red color in BGR

colorCircle = (0,255,0)
radius = 2
window_name = "Chil"
thickness=1
T = [[0,0],[0,0]]



#T1=[(467),(287)]
#img[110,100] = [0,0,255]
#img[111,100] = [0,0,255]

color = (120, 120, 150)
#if(img[236,544,0] <= color[0] and img[236,544,1] <= color[1] and img[236,544,2] <= color[2]):
#    print("HEI", color[0])



shotValue = 0
for y in range(columnPixels):
    #print("y", y)
    for x in range(widthPixels):
        #print("x",x)
        if (img[y,x,0] <= color[0]  and img[y,x,1] <= color[1] and img[y,x,2] >= color[2]):
            T.insert(shotValue,[y,x])
            if (img[T[shotValue]]-img[T[shotValue-1]] > 10):
                img = cv.circle(img, (x,y), radius, colorCircle, thickness)
                print(T[shotValue],"Shot",y,x)
                shotValue += 1
            

#img = cv.circle(img, T1, radius, colorCircle, thickness)
#pixval = list(image.getdata())
#print(img[236,544],)
cv.imwrite(savePath,img)
    


#print(color[0])
#print (center_coord[0])
for x in range(shotValue):
    #img = cv.circle(img, T[x], radius, colorCircle, thickness)
    print(img[T[x][0],T[x][1]])
print(shotValue)
   
# Displaying the image 
cv.imshow(window_name, img)
cv.waitKey(0)
#print ("Y", T[0][0],"X",T[0][1])
#print(pixval)
#ball = img[T[0][0]:T[shotValue-1][shotValue-1],T[0][1]:T[shotValue-1][shotValue-1]]
#img[273:333, 100:160] = ball



#cv.imshow("Image", img)
#cv.waitKey(0)

#cx = 0
#cy = 0
#center_px = img[cy,cx]
#print(center_px)
