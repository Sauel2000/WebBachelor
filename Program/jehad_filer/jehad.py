import cv2
import numpy as np

img = cv2.imread("C:/Users/jehad/Desktop/WebBachelor/Program/samuel_filer/samuel_bilder/SkyteSkive.jpg")

pixel_center = img[(160,650)]

print(pixel_center)
print(pixel_center[2])
width = 1280
height = 720
dim = (width, height)

resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
resized_img[(160,650)] = [0,255,0]
resized_img[(160,655)] = [0,255,0]

#cv2.rectangle(resized_img, (650,160), (660,170), (0, 255, 0), 1)



cv2.imshow('detect holes', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()