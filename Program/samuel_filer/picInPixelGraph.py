from scipy import misc
import cv2 as cv
import imageio
path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ABCop.jpg"

import matplotlib.pyplot as plt


face = misc.face()
imageio.imsave('face.png', face) # First we need to create the PNG file

face = imageio.imread('face.png')
type(face)      

face.shape =(768,1024,3)
face.dtype = ('uint8')

plt.imshow(face)
plt.show()

