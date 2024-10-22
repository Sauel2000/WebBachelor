import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image
import matplotlib.image as mpimg

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ref.jpg"
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"


img = mpimg.imread(path)


heightPixels = (img.shape[0])   # Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler



imgplot = plt.imshow(img)

x = [121]
y = [426]
u = [636]
v = [-7]

y1 = [104]
x1 = [438]
v1 = [-634]
u1 = [-5]


plt.quiver(x,y,u,v, color='r', units='xy', scale=1, width=0.5)
plt.quiver(x1,y1,u1,v1, color='r', units='xy', scale=1, width=0.5)


# Displaying the image 
plt.xlim(0,widthPixels)
plt.ylim(heightPixels,0)

plt.savefig('books_read.png')
plt.show()

