import cv2

img = cv2.imread("C:/Users/jehad/Desktop/WebBachelor/Program/samuel_filer/samuel_bilder/SkyteSkive.jpg")


# Load the image
img = cv2.imread('your_image.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges using Canny edge detector
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Detect lines using Hough transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# Find the angle of rotation needed to straighten up the picture
for line in lines:
    rho, theta = line[0]
    if abs(theta) > 0.1:
        angle = (theta * 180 / np.pi) - 90
        break

# Rotate the image by the calculated angle
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))

# Save the rotated image
cv2.imwrite('your_rotated_image.jpg', rotated)
