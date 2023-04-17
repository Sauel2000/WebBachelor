import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image
import matplotlib.image as mpimg

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/refGrad.jpg"
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"


img = mpimg.imread(path)


heightPixels = (img.shape[0])   # Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler



imgplot = plt.imshow(img)

x = [337.5]
y = [96]
u = [-24.5]
v = [-386]


x2 = [196]
y2 = [213]
u2 = [304.5]
v2 = [-300]






plt.quiver(x2,y2,u2,v2, color='r', units='xy', scale=1, width=0.5)

plt.quiver(x,y,u,v, color='r', units='xy', scale=1, width=0.5)

# Displaying the image 
plt.xlim(0,widthPixels)
plt.ylim(heightPixels,0)

plt.savefig('books_read.png')
plt.show()

