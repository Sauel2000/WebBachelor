
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
  

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/AutenC.jpg"
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"

img = cv.imread(path)

columnPixels = (img.shape[0])   #Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler


# Vector origin location
X = [289]
Y = [26]

X1 = [14]
Y1 = [292]
  
# Directional vectors
U = [0]  
V = [-450]  

U1 = [564]
V1 = [0]
  
# Creating plot
plt.quiver(X, Y, U, V, color='b', units='xy', scale=1)
plt.quiver(X1, Y1, U1, V1, color='g', units='xy', scale=1)
plt.title('Single Vector')
  
# x-lim and y-lim
plt.xlim(0,columnPixels)
plt.ylim(widthPixels,0)


# Show plot with grid
plt.grid()
plt.show()