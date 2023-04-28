import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt

#Path to pictures
PATHJ_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/jehad_tele/W27H27.jpg"
PATHT_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/w8_h6.jpg"


start_time = time.time()

# Function that reads the input image
img = cv.imread(PATHT_1)

#flipped_image = cv.flip(img, 0)


# Image scale
width = img.shape[1] 
height = img.shape[0]

# Image percentage scale factor
resize_factor = 1

# resized image scale
resized_width = int(width * resize_factor)
resized_height = int(height * resize_factor)


dim = (resized_width, resized_height)

resized_img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

# RGB interval to find the pixels we are looking for
R = (150, 256)
G = 120  
B = 80


# A list to store the coordinates of all pixels in all shooting holes that are detected
shotCoords = []

# Total amount of pixels in shooting holes detected
shotValue = 0

# Image tittel
window_name = "Shooting disc"

# Color of the the circle to be drawn, red in this case. 
colorCircle = (0,255,0)

# Variable representing the size of the radius of the circle
CircleMarkingRadius = 1 

# Thickness of the circle
thickness = -1

# Jump factor 
jumpPixel = 7

count = True

# Check every pixel in each row to match the searching color
# Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
for y in range(resized_height):
    for x in range(0,resized_width, jumpPixel):
        
        #bluePixel = resized_img[y,x, 0]
        #greenPixel = resized_img[y,x, 1]
        #redPixel = resized_img[y,x, 2]
        
        if ( resized_img[y,x, 0] < 80  and count == True):
            
            resized_img = cv.circle(resized_img, (x,y), 3, colorCircle, thickness)
            #print(x, y)
            count = False
            jumpPixel = 7
        
        # @param img[heightPixel coord, rowPixel coord, indexColorPixel], SearchColor[index(B=0,G,1,R,2)]
        # if statement which compares the color of the current pixel with the specified color of SearchColor.
        if resized_img[y,x,0] < B and resized_img[y,x,1] < G  and (resized_img[y,x,2] > R[0] and resized_img[y,x,2] < R[1]):
           
            # @param index,2D values (y=height, x=width)
            shotCoords.insert(shotValue,[x,y]) 
            
            # Marking the shotpixel with circle
            resized_img = cv.circle(resized_img, (x,y), CircleMarkingRadius, colorCircle, thickness)
            shotValue += 1


print("\nNumber of pixel found in shooting holes: ",shotValue)

resized_img = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)

imgplot = plt.imshow(resized_img)

plt.xlim(0,resized_width)
plt.ylim(resized_height, 0)

#plt.savefig('books_read.png')
plt.show()

print("\n Process finished in:", np.ceil((time.time()- start_time)),"seconds")
