import numpy as np
from PIL import Image, ImageEnhance
import cv2 as cv
from matplotlib import pyplot as plt
#from PIL import Image


path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/Skyteskive.jpg"

img = cv.imread(path,0)
numFigures = 5
findColor = [255,255,255]

laplacian = cv.Laplacian(img,cv.CV_64F)
sobelx = cv.Sobel(img,cv.CV_16SC1,1,0,ksize=5)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
plt.subplot(2,2,numFigures-4),plt.imshow(img,cmap = 'candela')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,numFigures-3),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,numFigures-2),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,numFigures-1),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])



plt.show()
