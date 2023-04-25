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

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/108mp.jpg"


img = mpimg.imread(path)

heightPixels = (img.shape[0])   #Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler
print(heightPixels, widthPixels)


#X PIXEL total between points
X = [1221.5]
Y = [5723]
U = [6896.5/485*200]      #6995-2226
V = [-19/485*200]        #6335-6280


X1 = [4585]
Y1 = [3810]
U1 = [0] 
V1 = [-1000]   


X3 = X
Y3 = Y
U3 = (524/50)*25
V3 = (15/50)*25
print(X3,Y3,U3,V3)


plt.title('Single Vector')

plt.quiver(X, Y, U, V, color='r', units='xy', scale=1, width=0.5)
plt.quiver(X1, Y1, U1, V1, color='g', units='xy', scale=1, width=0.5)


imgplot = plt.imshow(img)

plt.xlim(0,widthPixels)
plt.ylim(heightPixels,0)

plt.savefig('books_read.png')
plt.show()

