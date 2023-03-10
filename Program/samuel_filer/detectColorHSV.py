# Python program to identify
#color in images
  
# Importing the libraries OpenCV and numpy
import cv2 
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/babawat.png"

# Read the images
img = cv2.imread(path)
  
# Resizing the image
image = cv2.resize(img, (700, 600))
  
# Convert Image to Image HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  
#pixval = list(image.getdata())
# Defining lower and upper bound HSV values
lower = np.array([0, 0, 0])
upper = np.array([25, 25, 25])

#lower = np.array([0,0,0])
#upper = np.array([55, 55, 55])

# Defining mask for detecting color
mask = cv2.inRange(hsv, lower, upper)

#for row in range (0,700,1):
#    for col in range (0,600,1):
#        if 
# Display Image and Mask
cv2.imshow("Image", image)
cv2.imshow("Mask", mask)
  
# Make python sleep for unlimited time
cv2.waitKey(0)