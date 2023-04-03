import cv2
import numpy as np

PATH = "C:/Users/jehad/Desktop/WebBachelor/Program/samuel_filer/samuel_bilder/skyteSkive.jpg"
PATH2 = "C:/Users/jehad\Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/color_image.jpg"
PATH3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/skyteskive_ThreeMark.jpg"
PATH4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/resized_SS_RedMarks.jpg"
PATH5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/smallRedMarkers.jpg"
PATH6 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/virkeligObjekt.jpg"

PATH7 = "C:/Users/jehad/Desktop/WebBachelor/Program/samuel_filer/samuel_bilder/AxisCord.jpg"
PATH8 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/ref_bilder/ref_1.jpg"
PATH9 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/ref_bilder/accurateRef.jpg"


PATH_J = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/jehad_m.jpg"
PATH_O = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/olemarkus_m.jpg"
PATH_L = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/lars_m.jpg"

img = cv2.imread(PATH7)

# Standard resolution
new_width = img.shape[1]
new_height = img.shape[0]
resize_factor = 0.25

width = int(new_width * resize_factor)
height = int(new_height * resize_factor)

# Resize the picture for our standard resolution
resized_image = cv2.resize(img, (width, height))

# Change it to gray scale for contour detection algorithm to process faster. 
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# modifiy image with Gaussian Blur to lower the amount of noise in the image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply threshold to extract foreground target from background
_, threshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find contours where the foreground is black 
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour with the largest area, detecting shooting target
largestContour = max(contours, key=cv2.contourArea)

# Calculate the bounding rectangle around the contour
x_value, y_value, w, h = cv2.boundingRect(largestContour)

# Draw a rectangle around the contour
cv2.rectangle(resized_image, (x_value, y_value), (x_value+w, y_value+h), (0, 255, 0), 2)

# Coordination for center of the Contour
Contour_center_x = x_value + w//2
Contour_center_y = y_value + h//2

# Draw a circle at the center of the Contour
cv2.circle(resized_image, (Contour_center_x, Contour_center_y), 5, (0, 0, 255), -1)

# Get the values of pixel on the edges of horizontal line from the center of contour
left_edge_pixel = tuple(largestContour[largestContour[:,:,0].argmin()][0])
right_edge_pixel = tuple(largestContour[largestContour[:,:,0].argmax()][0])

# Get the values of pixel on the edges of vertical line from the center of contour
top_edge_pixel = tuple(largestContour[largestContour[:,:,1].argmin()][0])
bottom_edge_pixel = tuple(largestContour[largestContour[:,:,1].argmax()][0])

# Calculate from left most pixel to center and right most pixel, from the center of contour in a horizontal aspect
dist_left = Contour_center_x - left_edge_pixel[0]
dist_right = right_edge_pixel[0] - Contour_center_x

# Calculate from top most pixel to center and bottom most pixel, from the center of contour in a vertical aspect
dist_top = Contour_center_y - top_edge_pixel[1]
dist_bottom = bottom_edge_pixel[1] - Contour_center_y

# Draw lines from the center to the top-most and bottom-most pixels
cv2.line(resized_image, (Contour_center_x, Contour_center_y), (Contour_center_x, top_edge_pixel[1]), (255, 0, 0), 2)
cv2.line(resized_image, (Contour_center_x, Contour_center_y), (Contour_center_x, bottom_edge_pixel[1]), (255, 0, 0), 2)

# Draw lines from the center to the left-most and right-most pixels
cv2.line(resized_image, (Contour_center_x, Contour_center_y), (left_edge_pixel[0], Contour_center_y), (255, 0, 0), 2)
cv2.line(resized_image, (Contour_center_x, Contour_center_y), (right_edge_pixel[0], Contour_center_y), (255, 0, 0), 2)

# Display the image
cv2.imshow('Target', resized_image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

#Print Dimensions of the original and resized image
print("Picture resized: ", img.shape)
print("Picture resized: ", resized_image.shape)

print("\n")

# Print the coordination for the center of the contour
print(f"Center of target: ({Contour_center_x}, {Contour_center_y})")

# Print the coordination from left most pixel to center and the right most pixel to center.
print(f"Distance from center to left pixel: {dist_left} pixels")
print(f"Distance from center to right pixel: {dist_right} pixels")

# Print the coordination from top most pixel to center and the bottom most pixel to center.
print(f"Distance from center to top pixel: {dist_top} pixels")
print(f"Distance from center to bottom pixel: {dist_bottom} pixels")
print("\n")

