import cv2
import numpy as np

img = cv2.imread('C:/Users/jehad/Desktop/WebBachelor/Program/samuel_filer/samuel_bilder/skyteSkive.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_bound = np.array[(50, 20, 20)]
upper_bound = np.array[(100, 255, 255)]
mask = cv2.inRange(hsv, lower_bound, upper_bound)

#define kernel size  
kernel = np.ones((7,7),np.uint8)

# Remove unnecessary noise from mask

mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

segmented_img = cv2.bitwise_and(img, img, mask=mask)

contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)

cv2.imshow('detect holes', output)
cv2.waitKey(0)
cv2.destroyAllWindows()