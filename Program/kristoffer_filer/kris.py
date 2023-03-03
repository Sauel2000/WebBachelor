import cv2
from matplotlib import pyplot as plt
  
img = cv2.imread('samuel_filer\samuel_bilder\Skyteskive.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# convert the grayscale image to binary image
ret,thresh = cv2.threshold(img_gray,127,255,0)

contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

 
# calculate moments of binary image
M = cv2.moments(thresh)
image_copy = img.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
# Kalkulerer x og y koordinater av senter 
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
 
# put text and highlight the center
midtpunkt = cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

down_width = 600
down_Height = 500
down_points = (down_width, down_Height)

resized_down = cv2.resize(image_copy, down_points, interpolation= cv2.INTER_LINEAR)

# display the image
cv2.imshow("Image", resized_down)
cv2.waitKey(0)

'''
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, -1, (0, 255, 0), thickness=3 )


# see the results
cv2.imshow('None approximation', img)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', img_gray)
cv2.destroyAllWindows()
'''

'''
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
                
circle_center = (415,190)
radius = 100

cv2.circle(image_copy, circle_center, radius, (0, 0, 255), thickness=3, lineType = cv2.LINE_AA)

cnt = image_copy[0]
M = cv2.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

im2 = cv2.cvtColor(hierarchy, cv2.COLOR_GRAY2RGB)

cv2.polylines(im2, cnt, True, (0, 0, 255), 2)

cv2.circle(im2, (cx, cy), 5, (0, 0, 255), 1)

# see the results
cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', image_copy)
cv2.destroyAllWindows()



plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()
'''

