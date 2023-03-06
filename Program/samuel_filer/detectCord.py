import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image

image = Image.open('C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/frontDistanseSkruer.jpg')
width, height = image.size

pixval = list(image.getdata())

temp = []
hexcolpix = []
for row in range(0, height, 1):
    for col in range(0, width, 1):
        index = row*width + col
        temp.append(pixval[index])
    hexcolpix.append(temp)
    temp = []
    print (len(hexcolpix))
    print(len(temp))
    
    
    