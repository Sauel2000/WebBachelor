import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
import math 

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/AutenC.jpg"





img = cv.imread(path)


columnPixels = (img.shape[0])   #Bredden i bildet i piksler
widthPixels =(img.shape[1])     #Høyden i bilde i  piksler


plt.rcParams["figure.figsize"] = [widthPixels,columnPixels]
plt.rcParams["figure.autolayout"] = True
data = np.array([[0, -560], [0, -200]])
origin = np.array([[289, 26], [0, 150]])


test = data[0][0]
t1 = data[0][1]
print(test,t1)

print(columnPixels)
print(widthPixels)
#plt.xlim(0,columnPixels)
#plt.ylim(widthPixels,0)


plt.quiver(*origin, data[:, 0], data[:, 1], color=['black', 'red', 'green'], scale=columnPixels)


imgplot = plt.imshow(img)
plt.show()