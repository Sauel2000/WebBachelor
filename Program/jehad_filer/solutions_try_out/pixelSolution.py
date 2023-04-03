import cv2
import numpy as np

PATH = "C:/Users/jehad/Desktop/WebBachelor/Program/samuel_filer/samuel_bilder/skyteSkive.jpg"
PATH2 = "C:/Users/jehad\Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/color_image.jpg"
PATH3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/skyteskive_ThreeMark.jpg"
PATH4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/resized_SS_RedMarks.jpg"
PATH5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/smallRedMarkers.jpg"
PATH6 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/virkeligObjekt.jpg"

PATH_J = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/jehad_m.jpg"
PATH_O = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/olemarkus_m.jpg"
PATH_L = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/lars_m.jpg"

import cv2
import numpy as np

# Load the image of the target
img = cv2.imread(PATH)

# Resize the image to 1280 x 720
img = cv2.resize(img, (1280, 720))

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the image to remove noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold the image to create a binary image
_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour with the largest area (assumed to be the target)
largest_contour = max(contours, key=cv2.contourArea)

# Get the bounding rectangle of the contour
x, y, w, h = cv2.boundingRect(largest_contour)

# Draw a rectangle around the target
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Get the center of the target
cx = x + w/2
cy = y + h/2

# Draw a circle at the center of the target
cv2.circle(img, (int(cx), int(cy)), 5, (0, 0, 255), -1)

# Get the left and right edges of the target
left_edge = None
right_edge = None
for i in range(x, int(cx)):
    if np.any(thresh[y:y+h, i]):
        left_edge = i
        break
for i in range(x+w-1, int(cx)-1, -1):
    if np.any(thresh[y:y+h, i]):
        right_edge = i
        break

# Calculate the distance from the center to the left and right edges of the target
if left_edge is not None and right_edge is not None:
    dist_left = cx - left_edge
    dist_right = right_edge - cx
else:
    dist_left = None
    dist_right = None

# Display the image with the target, center, and distance measurements
cv2.putText(img, 'Center: ({}, {})'.format(int(cx), int(cy)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
if dist_left is not None and dist_right is not None:
    cv2.putText(img, 'Left edge distance: {}'.format(dist_left), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(img, 'Right edge distance: {}'.format(dist_right), (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
else:
    cv2.putText(img, 'Unable to determine distance to edges', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
cv2.imshow('Target', img)
cv2.waitKey(0)
cv2.destroyAllWindows