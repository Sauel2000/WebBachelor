from skimage import io
import cv2 
path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/frontTom.jpg"

# Read the images
img = cv2.imread(path)

def show(img):
    io.imshow(img)
    io.show()
    
cv2.imshow("Image", image)
cv2.waitKey(0)