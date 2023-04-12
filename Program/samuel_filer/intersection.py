import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from intersect import intersection
import numpy as np
import cv2 as cv

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/AutenC.jpg"





img = cv.imread(path)


columnPixels = (img.shape[0])   #Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler

# Vector origin vertical position 
X = [289]
Y = [26]

XU = [289,26,0,-531]
#Vector origin horizontal position
X1 = [14]
Y1 = [292]
  
# Directional vector for vertical position
U = [0]                   # INTERSECTER MED HORISONTAL PÅ 289
V = [-531]  
test = [289,26,14,292]
# Direction vector for horizontal position
U1 = [550]
V1 = [-5]

#PUNKT = intersections.

# Creating plot
plt.quiver(X, Y, U, V, color='b', units='xy', scale=1)
plt.quiver(X1, Y1, U1, V1, color='g', units='xy', scale=1)

plt.title('Single Vector')


imgplot = plt.imshow(img)
plt.show()
