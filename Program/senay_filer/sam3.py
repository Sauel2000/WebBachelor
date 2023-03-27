"""@package cv2
This program uses the OpenCV (cv2) library to search for pixels of a specific color in an image and mark them with a red circle.
The coordinates of the marked pixels are stored in a list and printed out.
The image with the marked pixels is also displayed in a window and saved as a new image file.
Opencv uses BGR color format
"""

import cv2 as cv

# Path to pictures
path = "C:/Users/senay/OneDrive/Dokumenter/USN - 3/Bachelor oppgave/IMG_Processing_Testing/dark-image.png"
savePath ="C:/Users/senay/OneDrive/Dokumenter/USN - 3/Bachelor oppgave/IMG_Processing_Testing/ll.png"

# Reference to the library we use 
cv2_section = "https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56"

# Function that reads the input image
img = cv.imread(path)

# Color we search for, blue in this case.
SearchColor = (255, 0, 0)

# Color of the circle to be drawn around the matching pixels, red in this case.
colorCircle = (0,0,255)

# Size of the radius of the circle to be drawn
CircleMarkingRadius = 10

# Thickness of the circle outline
thickness=1

# A list to store the coordinates of the matching pixels
shotCoords = []

# Counter for the number of matching pixels found
shotValue = 0

## Check every pixel in each row to match the searching color
# Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        # Compare the color of the current pixel with the specified search color using an if statement        
        if img[y,x,0] == SearchColor[0] and img[y,x,1] == SearchColor[1] and img[y,x,2] == SearchColor[2]:
            ## If the current pixel matches the search color, insert its coordinates into the list of matching pixels   
            shotCoords.insert(shotValue,[x,y])
            ## Draw a circle around the matching pixel
            img = cv.circle(img, (x,y), CircleMarkingRadius, colorCircle, thickness)
            ## Increment the counter for the number of matching pixels found
            shotValue += 1

## Save the marked image as a new file
# @param savePath Name of newfile
# @param img The image to save
cv.imwrite(savePath,img)
    
# Prints the coordinates of all the matching pixels
for x in range(shotValue):
    print(shotCoords[x])   
# Prints the total number of matching pixels found
print("Number of hits",shotValue)

## Display the marked image in a new window
# @param window name, the image to display
cv.imshow("Marked image", img)
# Wait for a keyboard input 
cv.waitKey(0)

