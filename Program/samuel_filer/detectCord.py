import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image
path = 'C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/babawat.png'
image = Image.open(path)
img = cv.imread(path)


#print(img.shape)
#print(type(img.shape))
#width, height = image.size
#print (width, height)
temp = np.asarray(image.open(path))
pixval = list(image.getdata()) #Gets all pixel colors GBR
color =(255,255,255)
width = image.width
height = image.height

print(width)
print(height)


#print(len(pixval))

#print(pixval[3])

#for x in range(0,len(pixval),1 ):
#        if (pixval[x] < (90,90,90) ):
#            print(pixval[x])

'''
temp = []
hexcolpix = []
for row in range(0, height, 1):
    for col in range(0, width, 1):
        index = row*width + col
        temp.append(pixval[index])
    hexcolpix.append(temp)
    temp = []
    
print(hexcolpix[100])
'''
'''    
print(len(hexcolpix))
for i in range (0, len(hexcolpix)):
    print(hexcolpix[1])
    if (hexcolpix[i] ==color):
        print("FANT HVIT")
'''




    
    