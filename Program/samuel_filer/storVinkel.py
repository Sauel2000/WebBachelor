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

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ACop.jpg"


img = mpimg.imread(path)
img[25,350]=(255,0,0)

heightPixels = (img.shape[0])   #Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler
print(heightPixels, widthPixels)


img[23,564]=(255,0,0) # IMG[Y X] #297-273.5= Y, 288,5+274,5=X
img[0,0] = (255,0,0)
img[266,33]


#Veritcal
X = [350]
Y = [25]
U = [-13]
V = [-718.5]

#Horizontal
X1 = [33]
Y1 = [266.5]
U1 = [648.5]
V1 = [-339]

#Px between horizontal
#339-266,5
#648,5-33


X2= [342.5] #(743,5 - 25)/2+25
Y2 = [428.5] #()
 
U2 = [120]
V2 = [0]



plt.title('Single Vector')

plt.quiver(X, Y, U, V, color='b', units='xy', scale=1, width=0.5)
plt.quiver(X1, Y1, U1, V1, color='b', units='xy', scale=1, width=0.5)
plt.quiver(X2, Y2, U2, V2, color='g', units='xy', scale=1, width=0.5)
imgplot = plt.imshow(img)

plt.xlim(0,widthPixels)
plt.ylim(heightPixels,0)

plt.savefig('books_read.png')
plt.show()

