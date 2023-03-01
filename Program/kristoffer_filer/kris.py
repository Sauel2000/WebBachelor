import cv2
from matplotlib import pyplot as plt
  
img = cv2.imread(r'C:\Users\krist\blinkny.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

down_width = 600
down_Height = 500
down_points = (down_width, down_Height)

resized_down = cv2.resize(img_gray, down_points, interpolation= cv2.INTER_LINEAR)


ret, thresh = cv2.threshold(resized_down, 150, 255, cv2.THRESH_BINARY)

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
                                      
# draw contours on the original image
image_copy = thresh.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

imageLine = image_copy()

pointA = (200,80)
pointB = (450,80)
cv2.line(img_gray, pointA, pointB, (255, 255, 0), thickness=3)
cv2.imshow('Image Line', imageLine)
cv2.waitKey(0)
                
# see the results
cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', image_copy)
cv2.destroyAllWindows()


'''
plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()
'''

