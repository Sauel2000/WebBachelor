import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt

start_time = time.time()                
                         


PATHT_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/w8_h6.jpg"

PATHS_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/1m.jpg"
PATHS_3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/0.65m.jpg"

PATHS_4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/1.5m.jpg"
PATHS_5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/2m.jpg"
PATHS_6 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/2.5m.jpg"
PATHS_7 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/3m.jpg"

blue = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/lightbla_tag.jpg"



# Function that reads the input image
img = cv.imread(blue)

# Image scale
width = img.shape[1] 
height = img.shape[0]

dim = (width, height)

#print(marks)

resized_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

imgplot = plt.imshow(resized_img)


plt.xlim(0,width)
plt.ylim(height, 0)
plt.show()

print("\n Process finished in:", np.ceil((time.time()- start_time)),"seconds")
