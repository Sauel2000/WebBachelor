import cv2 as cv
import time
import matplotlib.pyplot as plt

P1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/lightMarks_top.jpg"
P2 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/lightMarks_bottom.jpg"


P3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/darkMarks_top.jpg"
P4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/darkMarks_bottom.jpg"

L1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/lights/standardLights.jpg"
L2 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/lights/darkLights.jpg"
L3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/lights/blitzLights.jpg"
L4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/lights/handOverLights.jpg"


# Function that reads the input image
img = cv.imread(L3)

# Image resolution
width = img.shape[1]
height = img.shape[0]

dim = (width, height)

# convert the image from BGR to RGB to not create issues between OpenCv and matplotlib libraries
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# display image
imgplot = plt.imshow(img)

# display image with a coordinate system
plt.xlim(0,width)
plt.ylim(height, 0)
plt.show()

# print to terminal the amount of time it takes to run the code
print("\n Process finished in:", np.ceil((time.time()- start_time)),"seconds")
