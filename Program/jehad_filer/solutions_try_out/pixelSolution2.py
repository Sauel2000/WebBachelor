import cv2
import numpy as np

PATH = "C:/Users/jehad/Desktop/WebBachelor/Program/samuel_filer/samuel_bilder/skyteSkive.jpg"
PATH2 = "C:/Users/jehad\Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/color_image.jpg"
PATH3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/skyteskive_ThreeMark.jpg"
PATH4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/resized_SS_RedMarks.jpg"
PATH5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/smallRedMarkers.jpg"
PATH6 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/virkeligObjekt.jpg"

# Load the image
img = cv2.imread(PATH3)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply adaptive thresholding to segment the target
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and detect shooting spots
for c in contours:
    # Compute the area of the contour
    area = cv2.contourArea(c)

    # If the area is too small, ignore the contour
    if area < 100:
        continue

    # Compute the centroid of the contour
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    # Draw a circle at the centroid of the contour
    cv2.circle(img, (cx, cy), 3, (0, 0, 255), -1)
    print(cx, cy)

# Display the result
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

|


