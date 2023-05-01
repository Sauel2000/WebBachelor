import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt

start_time = time.time()

PATHJ_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/jehad_tele/W27H27.jpg"

PATHS_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/1m.jpg"
PATHS_2 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/0.80m.jpg"
PATHS_3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/0.65m.jpg"




## Documentation for a function
# Function that reads the input image
img = cv.imread(PATHS_1)
flipped_image = cv.flip(img, 0)


# Image scale
width = img.shape[1] 
height = img.shape[0]

# Image percentage scale factor
resize_factor = 1

# resized image scale
resized_width = int(width * resize_factor)
resized_height = int(height * resize_factor)


dim = (resized_width, resized_height)

resized_img = cv.resize(flipped_image, dim, interpolation = cv.INTER_AREA)


# RGB interval to find the pixels we are looking for
R = (150, 256)
G = 120  
B = 80


# distance between two detected pixels
shotPixelDistance = 80

# Color of the the circle to be drawn, red in this case. 
colorCircle = (0,255,0)

# Variable representing the size of the radius of the circle
CircleMarkingRadius = 1 

# Thickness of the circle
thickness = -1

# Image tittel
window_name = "Shooting disc"

# A list to store the coordinates of all pixels in all shooting holes that are detected
shotCoords = []


# Total amount of pixels in shooting holes detected
shotValue = 0



# Check every pixel in each row to match the searching color
# Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
for y in range(resized_height):
    for x in range(0,resized_width, 4):
        
        # @param img[heightPixel coord, rowPixel coord, indexColorPixel], SearchColor[index(B=0,G,1,R,2)]
        # if statement which compares the color of the current pixel with the specified color of SearchColor.
        if resized_img[y,x,0] < B and resized_img[y,x,1] < G  and (resized_img[y,x,2] > R[0] and resized_img[y,x,2] < R[1]):
           
            # @param index,2D values (y=height, x=width)
            shotCoords.insert(shotValue,[x,y]) 
            
            # Marking the shotpixel with circle
            #resized_img = cv.circle(resized_img, (x,y), CircleMarkingRadius, colorCircle, thickness)
            shotValue += 1

#print(shotCoords)


# length of the array
length_shotCoords = len(shotCoords)

# Where index should start in an array
indexStart = 0


# amount of rectangles drawin
recCount = 0

# Group of pixels
groups = []

# check if marked pixels are in right shooting hole and divide- 
# -Them into right groups depended on shooting holes 
for point in shotCoords:

    # 
    matched_group = None
    
    for group in groups:


        if any(abs(point[i] - group[0][i]) <= shotPixelDistance for i in range(2)):
            matched_group = group
            break
    
    if matched_group is not None:
        matched_group.append(point)
    else:
        groups.append([point])

#variabel for shoving values into the samePixelshot array
#print(groups)


marks = 0
for group in groups:

    group_length = len(group)

    samePixelShots = np.zeros((group_length, 2), dtype=int)

    for points in range(group_length):
        #print(group[points])
        samePixelShots[points] = group[points]

    x, y, w, h = cv.boundingRect(samePixelShots)

    cv.rectangle(resized_img, (x, y), (x+w, y+h), (255, 0, 0), 0)
    # Find the center of the boundingRec
    center_x = x + int(w/2)
    center_y = y + int(h/2)

    resized_img[center_y, center_x] = [255, 255, 255]


    #print("\n", samePixelShots, "\n")
    marks += 1

print(marks)


# modifiy values in the samePixelshots 
#print(groups)
#print(samePixelShots, "\n")


'''
for x in range(shotValue):
    print(shotCoords[x])   
'''
#print("\nNumber of pixel found in shooting holes: ",shotValue)
#print("rectangle count: ", recCount, "\n")

#print("Original Image resolution: ",img.shape[1], " | ", img.shape[0])
#print("Resized image resolution",resized_width, " | ", resized_height)

#cv.imshow(window_name, resized_img)
#cv.waitKey(0)

# Convert to RGB color space
resized_img = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)

imgplot = plt.imshow(resized_img)

plt.xlim(0,resized_width)
plt.ylim(0, resized_height)

#plt.savefig('books_read.png')
plt.show()

print("\n Process finished in:", np.ceil((time.time()- start_time)),"seconds")
