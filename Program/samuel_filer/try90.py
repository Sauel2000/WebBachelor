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

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/young.jpg"


img = mpimg.imread(path)

heightPixels = (img.shape[0])   #Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler
print(heightPixels, widthPixels)


#X Horizontal linjal
X = [2452.5]
Y = [4210]
U = [9792.5-2452.5] #7320-1600
V = [4205-4210]   #7060-7150



#X Horizontal linjal2
X = [1922.5]
Y = [4143]
U = [7340] #7320-1600
V = [-2]   #7060-7150


X1 = [1595]
Y1 = [7030]
U1 = [5724] #7320-1600
V1 = [-70]   #7060-7150
#Vertical Aksekors
X2 = [6081.5]
Y2 = [490]
U2 = [6081.5-6080]
V2 = [-7370]


#SKUDD 
X3 = [6082.25]         #origo
Y3 = [4165.5]         #origo
U3 = [92]  #7330-1580
V3 = [835.5]   #(-1)*(5530-7065)


X4 = []
Y4 = []
U4 = []
V4 = []


AmountPixelPermmX = 484/7340.5
AmountPixelPermmY = 484/7370


pixelRealX = U3[0]*AmountPixelPermmX
pixelRealY = V3[0]*AmountPixelPermmY
hyp  = math.sqrt(pixelRealX**2+pixelRealY**2)

print(hyp,pixelRealX,pixelRealY)





plt.title('Single Vector')

plt.quiver(X, Y, U, V, color='r', units='xy', scale=1, width=0.5)
plt.quiver(X2, Y2, U2, V2, color='r', units='xy', scale=1, width=0.5)
plt.quiver(X3, Y3, U3, V3, color='r', units='xy', scale=1, width=0.5)
plt.quiver(X1, Y1, U1, V1, color='g', units='xy', scale=1, width=0.5)


imgplot = plt.imshow(img)

plt.xlim(0,widthPixels)
plt.ylim(heightPixels,0)

plt.savefig('books_read.png')
plt.show()

