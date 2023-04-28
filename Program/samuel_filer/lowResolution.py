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

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/A190.jpg"


img = mpimg.imread(path)

heightPixels = (img.shape[0])   #Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler
print(heightPixels, widthPixels)


#X PIXEL total between points
X = [292.75]
Y = [1430]
U = [(2680-292.72)/485*242.5] #7320-1600
V = [(1430-1435)/485*242.5]   #7060-7150



plt.title('Single Vector')

plt.quiver(X, Y, U, V, color='r', units='xy', scale=1, width=0.5)
#plt.quiver(X1, Y1, U1, V1, color='g', units='xy', scale=1, width=0.5)


imgplot = plt.imshow(img)

plt.xlim(0,widthPixels)
plt.ylim(heightPixels,0)

plt.savefig('books_read.png')
plt.show()

