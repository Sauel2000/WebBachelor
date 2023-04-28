'''
##General CV2 library
'''
import cv2 as cv
from ImagInfoClass import*
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/lin.jpg"
PATH1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/linjal_L.jpg"


img = mpimg.imread(PATH1)


heightPixels = (img.shape[0])   #Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler
print(heightPixels, widthPixels)


#img[23,465]=(255,0,0) # IMG[Y X] #297-273.5= Y, 288,5+274,5=X
#img[0,0] = (255,0,0)
#img[266,33]


#X PIXEL total between points
XW = [50]
YW = [130]
UW = [415/15]
VW = [0]

#Y PIXEL TOTAL between points
XH = [465]
YH = [130]
UH = [0]
VH = [107]

#XY pixels total
X1 = [50]
Y1 = [130]
U1 = [415]  #415/15
V1 = [107]  #107/15

# 10 mm 1 cm
X2 = [50]
Y2 = [130]
U2 = [33]
V2 = [9]


# 20 mm 2 cm
X4 = [50]
Y4 = [130]
U4 = [64.5]
V4 = [16.5]


# 30 mm -> 3 cm 
X6 = [50]
Y6 = [130]
U6 = [95.5]
V6 = [24.5]

# Y = X 
X3 = [50]
Y3 = [130]
U3 = [415*0.07]
V3 = [107*0.07]



cmInPixel = math.sqrt(U1[0]/15**2 + V1[0]/15**2)

irl = (15/(U1[0]-X1[0])) * (24.3333333333333)*15
print (irl)



#Px between horizontal
#339-266,5
#648,5-33




plt.title('Single Vector')

plt.quiver(XW, YW, UW, VW, color='r', units='xy', scale=1, width=0.5)
plt.quiver(XH, YH, UH, VH, color='b', units='xy', scale=1, width=0.5)
plt.quiver(X1, Y1, U1, V1, color='g', units='xy', scale=1, width=0.5)
plt.quiver(X2, Y2, U2, V2, color='g', units='xy', scale=1, width=0.5)
plt.quiver(X4, Y4, U4, V4, color='red', units='xy', scale=1, width=0.5)
plt.quiver(X4, Y4, U4, V4, color='r', units='xy', scale=1, width=0.5)
plt.quiver(X6, Y6, U6, V6, color='y', units='xy', scale=1, width=0.5)
plt.quiver(X3, Y3, U3, V3, color='r', units='xy', scale=1, width=0.5)
imgplot = plt.imshow(img)

plt.xlim(0,widthPixels)
plt.ylim(0,heightPixels)

plt.savefig('books_read.png')
plt.show()

