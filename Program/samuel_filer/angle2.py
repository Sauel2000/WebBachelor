import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from intersect import intersection
import numpy as np

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/AutenC.jpg"





img = mpimg.imread(path)


columnPixels = (img.shape[0])   #Høyden i bildet i piksler # Y
widthPixels =(img.shape[1])     #Bredden i bilde i  piksler # X
img[572,0] = (255,0,0) #Y X
print(img.shape)
# Vector origin vertical position 
X = [289]
Y = [26]

#Vector origin horizontal position
X1 = [14]
Y1 = [292]
  
# Directional vector for vertical position
U = [0]  
V = [-531]  

# Direction vector for horizontal position
U1 = [550]
V1 = [-5]
U2 = [550]
V2 = [0]

X2 = [572]
Y2 = [588]

UT = [-573]
YT = [0]


# Creating plot
plt.quiver(X, Y, U, V, color='b', units='xy', scale=1)

plt.quiver(X1, Y1, U1, V1, color='g', units='xy', scale=1)
plt.quiver(X1, Y1, U2, V2, color='yellow', units='xy', scale=1)
plt.quiver(X2, Y2, UT, YT, color='yellow', units='xy', scale=1)

plt.title('Single Vector')
  
# x-lim and y-lim
#plt.xlim(0,columnPixels-1)
#plt.ylim(widthPixels-1,0)

plt.xlim(0,widthPixels-1)
plt.ylim(columnPixels-1,0)

imgplot = plt.imshow(img)
plt.show()
