import cv2
import numpy as np
from matplotlib import pyplot as plt

# Reading image to be detected
img = cv2.imread('C:/Users/senay/OneDrive/Dokumenter/USN - 3/Bachelor oppgave/IMG_Processing_Testing/shapes.png')

cv2.imshow('Grayscale', img)
cv2.waitKey(0)

# Converting the image to a grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray)
cv2.waitKey(0)

# Press + to stop process 
cv2.destroyAllWindows()

# Converts image to binary image, where pixels are set to 0 or 255, 
# If the intensity of the pixels is greater or equal to the lower threshold of value 127 then the pixels will be set to white,
# and if the pixels intensity is lower than 127 they will be set to black. 
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Thresholded', threshed)
cv2.waitKey(0)

# Finding the countours around the black pixels, finds border around the the black pixels
contours = cv2.findContours(threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

for contour in contours:
    if i == 0:
        i = 1
        continue
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
    
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m10']/M['m00'])
        
    if len(approx) == 3:
        cv2.putText(img, 'Triangle' , (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    elif len(approx) == 4:     
        cv2.putText(img, 'Quadrilateral', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    elif len(approx) == 5:     
        cv2.putText(img, 'Pentagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    elif len(approx) == 6:     
        cv2.putText(img, 'Hexagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    else:
        cv2.putText(img, 'Circle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
      
                    
                              
                    
cv2.imshow('Shapes', img)
cv2.waitKey(0)
# Press + to stop process   
cv2.destroyAllWindows()
