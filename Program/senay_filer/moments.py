import cv2
import numpy as np

# read image
img = cv2.imread("C:/Users/senay/OneDrive/Dokumenter/USN - 3/Bachelor oppgave/IMG_Processing_Testing/Skyteskive.jpg")

print("Image size:", img.shape[:2])


down_height = 720
down_width = 1280
down_points = (down_width, down_height)

img = cv2.resize(img, down_points, interpolation=cv2.INTER_CUBIC)
 
# convert to grayscale and apply Gaussian blur
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# apply threshold
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# find contours and filter out small ones
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]

# compute convex hull of largest contour
cnt = max(contours, key=cv2.contourArea)
hull = cv2.convexHull(cnt)

# compute moments of convex hull and centroid coordinates
M = cv2.moments(hull)
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])

# draw centroid and hull on image
cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)
cv2.drawContours(img, [hull], 0, (0, 255, 0), 2)

# get image dimensions
h, w, _ = img.shape

# print centroid coordinates from each corner
print("Centroid coordinates from each corner:")
print("Top-left: ({}, {}) pixels".format(cx, cy))
print("Top-right: ({}, {}) pixels".format(w - cx, cy))
print("Bottom-left: ({}, {}) pixels".format(cx, h - cy))
print("Bottom-right: ({}, {}) pixels".format(w - cx, h - cy))

print("Image size:", img.shape[:2])

# display image
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
