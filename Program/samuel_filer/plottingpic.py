import numpy as np
import matplotlib.pyplot as plt
import ipympl
import imageio as iio
import matplotlib.image as mpimg
import skimage
path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/AutenC.jpg"


img = mpimg.imread(path)
imgplot = plt.imshow(img)
#image = iio.imread(path)
plt.imshow(img)
plt.show()