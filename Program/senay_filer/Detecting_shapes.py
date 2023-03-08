import cv2
import numpy as np
from matplotlib import pyplot as plt

# Reading image to be detected
img = cv2.imread('C:/Users/senay/OneDrive/Dokumenter/USN - 3/Bachelor oppgave/IMG_Processing_Testing/shapes.png')

down_height = 300
down_width = 350
down_points = (down_width, down_height)
img_2 = img
"""
img_2 = cv2.resize(img, down_points, interpolation= cv2.INTER_LINEAR)
"""

# converting image into grayscale image
gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)

# Converts image to binary image, where pixels are set to 0 or 255,
# If the intensity of the pixels is greater or equal to the lower threshold of value 127 then the pixels will be set to white,
# and if the pixels intensity is lower than 127 they will be set to black.
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# This function returns a list of contours and hierarchy (relationship between contours).
# Finding the countours around the black pixels, finds border around the the black pixels
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# Iterate over the contours list to detect each shape and put its name at its center.
for contour in contours:
    
    # Ignore the first contour, which represents the whole image.
    if i == 0:
        i = 1
        continue

    # Approximate the contour shape using cv2.approxPolyDP() function to get the number of vertices and thus find the shape.
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)

    # Draws the contour
    cv2.drawContours(img_2, [contour], 0, (0, 0, 255), 5)

    # Calculating the center point of the shape
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])

    # Puts the name of the shape at its center
    if len(approx) == 3:
        cv2.putText(img_2, '*', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    elif len(approx) == 4:
        cv2.putText(img_2, 'Quadrilateral', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    elif len(approx) == 5:
        cv2.putText(img_2, 'Pentagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    elif len(approx) == 6:
        cv2.putText(img_2, 'Hexagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    else:
            cv2.putText(img_2, '|', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

   


# displaying the image after drawing contours
cv2.imshow('shapes', img_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
