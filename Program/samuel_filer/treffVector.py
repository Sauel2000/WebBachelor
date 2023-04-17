'''
##General CV2 library
'''
import cv2 as cv
from ImagInfoClass import*
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from intersect import intersection
import numpy as np
import math
from sympy import Point3D, Line3D, Plane
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/AutenC.jpg"



img = mpimg.imread(path)
img[0,0]=(255,0,0)

heightPixels = (img.shape[0])   #Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler
print(heightPixels, widthPixels)

# Vector origin vertical position 
X = [288.5]
Y = [25.5]
#Vector origin horizontal position
X1 = [15.5] 
Y1 = [292.5]    
  
# Directional vector for vertical position
U = [0] 
V = [-530]  

# Direction vector for horizontal position
U1 = [547] #GÅTT 564
V1 = [-5.5] 
#DIRECTION vector for vertical position
U2 = [550]  
V2 = [0]    




cmPXwidth = 48 / U1[0]
cmPXheight = 48 / U2[0]
IRL_x_width = 0
IRL_y_heigh = 0

print(cmPXheight, cmPXwidth)

#ORIGIN FOR VECTOR FOR NORMAL TO HIT
#SECOND HORIZONTAL POINT TO HIT
X3 = [564]
Y3 = [297]
UH3 = [0]
VH3 = [273.5]

#FIRST VERTICAL POINT TO HIT
X4 = [288.5]
Y4 = [25.5]
UH4 =[274.5]
VH4 =[2]

img[23,564]=(255,0,0) # IMG[Y X] #297-273.5= Y, 288,5+274,5=X
img[0,0] = (255,0,0)
#img[297,550+14]=(255,0,0)

#Origin intersection point between horizontal and vertical axis
#Origo
XS = [288.5]
YS = [295.25]    #Horizontal vector origin y start + half of horizontal vector end. 292,5 + 5,5/2



#Directional vector for hit
US = [275]          #550-289=          #400-291.5=108 DIRECTIONAL COORD FOR X POSITION
VS = [278.5-7]      #abs(26-291.5)         #200-289=-89 DIRECITONAL COORD FOR Y POSITION



endHitCordX =  [276]         #[550-289]
endHitCordY =  272       #[291,5-26]
for x in range(0,round(endHitCordX[0]),1):
    IRL_x_width = IRL_x_width + cmPXwidth 
    if (round(endHitCordX[0]) < endHitCordX[0] and x == endHitCordX[0]-1):
        IRL_x_width = IRL_x_width+(endHitCordX[0]-(round(endHitCordX[0]*cmPXwidth)))
        print(IRL_x_width+(endHitCordX[0]-(round(endHitCordX[0]*cmPXwidth))))
    if (round(endHitCordX[0])>endHitCordX[0] and x == endHitCordX[0]-1):
        IRL_x_width = IRL_x_width - (round(endHitCordX[0])-endHitCordX[0])*cmPXwidth
        print(IRL_x_width - (round(endHitCordX[0])-endHitCordX[0])*cmPXwidth)
for y in range(0,endHitCordY,1):
    IRL_y_heigh = IRL_y_heigh + cmPXheight 
    #if (round(endHitCordY[0]) < endHitCordY[0] and y == endHitCordY[0]-1):
    #    IRL_y_heigh = IRL_y_heigh+(endHitCordY[0]-(round(endHitCordY[0]*cmPXheight)))
    #    print(IRL_y_heigh+(endHitCordY[0]-(round(endHitCordY[0]*cmPXheight))))
    #if (round(endHitCordY[0])>endHitCordY[0] and y == endHitCordY[0]-1):
    #   IRL_y_heigh = IRL_y_heigh - (round(endHitCordY[0])-endHitCordY[0])*cmPXheight
    #    print(IRL_y_heigh - (round(endHitCordY[0])-endHitCordY[0])*cmPXheight)
print(IRL_x_width, "width", IRL_y_heigh, "height")

test= float(endHitCordY) 
print(endHitCordY,round(endHitCordY))
print(math.ceil(0.4))
if (test< endHitCordY):
    IRL_y_heigh = IRL_y_heigh+(endHitCordY-(round(endHitCordY*cmPXheight)))
    print(IRL_y_heigh+(endHitCordY-(round(endHitCordY*cmPXheight))))
               
               

hyptonus = math.sqrt(IRL_x_width**2+IRL_y_heigh**2)
print(hyptonus, "HYP")


# Creating plot
plt.quiver(X, Y, U, V, color='b', units='xy', scale=1, width=0.5)

plt.quiver(X1, Y1, U1, V1, color='g', units='xy', scale=1,width = 0.5)
#plt.quiver(X1, Y1, U2, V2, color='yellow', units='xy', scale=1,width =1)
plt.quiver(XS, YS, US, VS, color='green', units='xy', scale=1, width = 0.5)
plt.quiver (X3, Y3, UH3, VH3, color = 'green', units='xy', scale=1,width=0.5)
plt.quiver(X4,Y4, UH4, VH4, color = 'blue', units='xy', scale=1, width= 0.5)

plt.title('Single Vector')

# Color we search for, blue in this case.
SearchColor = (255, 0, 0)

# Color of the the circle to be drawn, red in this case. 
colorCircle = (0,0,255)

# Variable representing the size of the radius of the circle
CircleMarkingRadius = 2

window_name = "Chil"

# Thickness of the circle
thickness=1

# A list to store the coordinates of the shots
shotCoords = []

# Value of each shot
shotValue = 0

# Check every pixel in each row to match the searching color
# Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        # @param img[heightPixel coord, rowPixel coord, indexColorPixel], SearchColor[index(B=0,G,1,R,2)]
        # if statement which compares the color of the current pixel with the specified color of SearchColor.
        if img[y,x,0] == SearchColor[0] and img[y,x,1] == SearchColor[1] and img[y,x,2] == SearchColor[2]:
            # @param index,2D values (y=height, x=width)
            shotCoords.insert(shotValue,[x,y])
            # Marking the shotpixel with circle
            img = cv.circle(img, (x,y), CircleMarkingRadius, colorCircle, thickness)
            shotValue += 1


cv.imwrite(savePath,img)
    
# Prints all shot coordinates 
for x in range(shotValue):
    print(shotCoords[x])   
print("Number of hits",shotValue)

imgplot = plt.imshow(img)

plt.xlim(0,widthPixels)
plt.ylim(heightPixels,0)

plt.savefig('books_read.png')
plt.show()

