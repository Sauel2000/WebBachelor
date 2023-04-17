'''

##General CV2 library

'''
import cv2 as cv
import numpy as np

#Path to pictures
path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/linjal.jpg"
path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"
savePath="C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/resized_SS.jpg"
PATH4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/resized_SS_RedMarks.jpg"
PATH5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/Skyteskive_redRectangleMark.jpg"
PATH6 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/fysiskMark.jpg"
PATH7 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/jehad_m.jpg"


'''
Cv2 Section

https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56

'''

## Documentation for a function
# Function that reads the input image
img = cv.imread(PATH6)

# Image scale
width = img.shape[1] 
height = img.shape[0]

# Image percentage scale factor
resize_factor = 0.2

# resized image scale
resized_width = int(width * resize_factor)
resized_height = int(height * resize_factor)


dim = (resized_width, resized_height)

resized_img = cv.resize(img, dim, interpolation = cv.INTER_AREA)


# RGB interval to find the pixels we are looking for
R = (150, 256)
G = 80
B = 80


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


# A list to store pixel coordinates which are in the same shooting hole
samePixelShots = []


# Total amount of pixels in shooting holes detected
shotValue = 0



# Check every pixel in each row to match the searching color
# Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
for y in range(resized_height):
    for x in range(resized_width):
        
        # @param img[heightPixel coord, rowPixel coord, indexColorPixel], SearchColor[index(B=0,G,1,R,2)]
        # if statement which compares the color of the current pixel with the specified color of SearchColor.
        if resized_img[y,x,0] < B and resized_img[y,x,1] < G  and (resized_img[y,x,2] > R[0] and resized_img[y,x,2] < R[1]):
           
            # @param index,2D values (y=height, x=width)
            shotCoords.insert(shotValue,[x,y]) 
            
            # Marking the shotpixel with circle
            #resized_img = cv.circle(resized_img, (x,y), CircleMarkingRadius, colorCircle, thickness)
            shotValue += 1


# length of the array
length_shotCoords = len(shotCoords)

# Where index should start in an array
indexStart = 0

# distance between two detected pixels
shotPixelDistance = 30


# This for loop is to go through all detected pixels and organize pixels for each shooting hole
# Afterwards we use the median of all pixels in a shooting hole to mark the pixel in the middle
for i in range(length_shotCoords - 1):

    nextPixel = i + 1

    # Compare x and y values between to pixels
    XvalueDiff = abs((shotCoords[nextPixel][0] - shotCoords[i][0]))
    YvalueDiff = abs((shotCoords[nextPixel][1] - shotCoords[i][1]))

    # Check between two pixel if they have more than 6 pixel between them, it means there are pixels in different holes.
    if ((XvalueDiff > shotPixelDistance or YvalueDiff > shotPixelDistance)) or i == (length_shotCoords -2):

        # send in all values which are in the same pixel shooting hole into another array
        samePixelShots.extend(shotCoords[indexStart:nextPixel])
        
        # We check if the length of the array is pair or odd to modifiy to find the right median. 
        # If it is odd we find the middle value, if it is pair we pick the next value.
        if(len(samePixelShots) % 2 == 0):
            median = int(np.ceil(len(samePixelShots) / 2 ))
            print("pair")
        else:
            median = int(np.ceil(len(samePixelShots) / 2 )) - 1 
            print("odd")

        x_pos = samePixelShots[median][0]
        y_pos = samePixelShots[median][1]

        
        print(" median pixel ->  { x_pos",x_pos, "| y_pos:", y_pos, " }")

        # Mark the pixel which is median of all pixel that are detected in that shooting hole
        resized_img = cv.circle(resized_img, (x_pos,y_pos), CircleMarkingRadius, colorCircle, -1)
        
        print(samePixelShots, "\n-------------- \n")
        
        # Clear all values in the array so median can be calculated
        samePixelShots.clear()

        # Move index value to look for pixels in the next shooting hole
        indexStart = nextPixel


cv.imwrite(savePath, resized_img)
    
# Prints all shot coordinates 
'''
for x in range(shotValue):
    print(shotCoords[x])   
'''
print("Number of hits",shotValue)


print(resized_img.shape[0], " | ", resized_width)
print(resized_img.shape[1], " | ", resized_width)

cv.imshow(window_name, resized_img)
cv.waitKey(0)

