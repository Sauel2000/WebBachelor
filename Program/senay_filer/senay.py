import cv2


path = "blackdot.jpg"

#Loading an image in grayscale
gray = cv2.imread(path, 0)

#Converts image to binary image, where pixels are set to 0 or 255 
th, threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV|cv2.THRES_OTSU)


