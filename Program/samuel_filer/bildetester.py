import cv2
import numpy as np
from PIL import Image
path = 'C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/bright-image.png'
## Read
image = Image.open(path)
img = cv2.imread(path)

pixval = list(image.getdata())
for x in pixval:
    print(pixval[x])
print (pixval[0])
## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([235, 235, 235])
upper = np.array([255, 255, 255])
## mask of green (36,25,25) ~ (86, 255,255)
# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
mask = cv2.inRange(hsv, lower, upper)

## slice the green
# Display Image and Mask
cv2.imshow("Image", img)
cv2.imshow("Mask", mask)

# Make python sleep for unlimited time
cv2.waitKey(0)