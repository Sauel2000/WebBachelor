
'''

##General CV2 library

'''
import cv2 as cv


#Path to pictures
path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/linjal.jpg"
path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"

'''
Cv2 Section

https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56

'''

## Documentation for a function
# Function that reads the input image
img = cv.imread(path1)

# Color we search for, blue in this case.
SearchColor = (255, 0, 0)

# Color of the the circle to be drawn, red in this case. 
colorCircle = (0,0,255)

# Variable representing the size of the radius of the circle
CircleMarkingRadius = 5

window_name = "Chil"

# Thickness of the circle
thickness=2

# A list to store the coordinates of the shots
shotCoords = []

# Value of each shot
shotValue = 0

# Check every pixel in each row to match the searching color
# Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        # @param img[heightPixel coord, rowPixel coord, indexColorPixel], SearchColor[index(B=0,G,1,R,2)]
        # if statement which compares the color of the current pixel with the specified color of SearchColor.
        if img[y,x,0] == SearchColor[0] and img[y,x,1] == SearchColor[1] and img[y,x,2] == SearchColor[2]:
            # @param index,2D values (y=height, x=width)
            shotCoords.insert(shotValue,[x,y])
            # Marking the shotpixel with circle
            img = cv.circle(img, (x,y), CircleMarkingRadius, colorCircle, thickness)
            shotValue += 1


cv.imwrite(savePath,img)
    
# Prints all shot coordinates 
for x in range(shotValue):
    print(shotCoords[x])   
print("Number of hits",shotValue)

cv.imshow(window_name, img)
cv.waitKey(0)

