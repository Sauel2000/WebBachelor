import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from PIL import Image

path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/Skyteskive.jpg"
img = cv.imread(path,0)
#print(img.size[0])

plt.rcParams["figure.figsize"] = [5, 5]
plt.imshow(img, origin='upper', extent=[0, 40, 0, 40], aspect=1, )
plt.show()

