import cv2
import numpy as np

PATH = "C:/Users/jehad/Desktop/WebBachelor/Program/samuel_filer/samuel_bilder/skyteSkive.jpg"
PATH2 = "C:/Users/jehad\Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/color_image.jpg"
PATH3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/skyteskive_ThreeMark.jpg"
PATH4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/resized_SS_RedMarks.jpg"
PATH5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/smallRedMarkers.jpg"
PATH6 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/virkeligObjekt.jpg"

# Load the image
img = cv2.imread(PATH)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply adaptive thresholding to segment the target
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the circular contour of the target
target_contour = None
for c in contours:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
    if len(approx) >= 8 and cv2.isContourConvex(approx):
        target_contour = approx

# If the circular contour is found, draw it on the image and detect shooting spots
if target_contour is not None:
    cv2.drawContours(img, [target_contour], -1, (0, 255, 0), 2)
    (x, y), r = cv2.minEnclosingCircle(target_contour)
    for c in contours:
        if cv2.contourArea(c) < 100:
            continue
        (cx, cy), _ = cv2.minEnclosingCircle(c)
        if cv2.norm(np.array([cx, cy]) - np.array([x, y])) < r:
            cv2.circle(img, (int(cx), int(cy)), 5, (0, 0, 255), -1)

# Display the result
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
