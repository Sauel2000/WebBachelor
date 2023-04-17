'''

##General CV2 library

'''
import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt



start_time = time.time()


#Path to pictures
path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/linjal.jpg"
path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"
savePath="C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/resized_SS.jpg"
PATH4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/resized_SS_RedMarks.jpg"
PATH5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/olemarkus_m.jpg"
PATH6 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/fysiskMark.jpg"
PATH7 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/nalMark.jpg"

'''
Cv2 Section

https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56

'''

## Documentation for a function
# Function that reads the input image
img = cv.imread(PATH7)



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
G = 100
B = 100



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
shotPixelDistance = 100

# amount of rectangles drawin
recCount = 0

# This for loop is to go through all detected pixels and organize pixels for each shooting hole
# Afterwards we use the median of all pixels in a shooting hole to mark the pixel in the middle
for i in range(length_shotCoords - 1):

    # Variabel that captures the next pixel value
    nextPixel = i + 1

    

    # Compare x and y values between to pixels
    XvalueDiff = abs((shotCoords[nextPixel][0] - shotCoords[i][0]))
    YvalueDiff = abs((shotCoords[nextPixel][1] - shotCoords[i][1]))

    # Check between two pixel if they have more than 6 pixel between them, it means there are pixels in different holes.
    if ((XvalueDiff > shotPixelDistance or YvalueDiff > shotPixelDistance)) or i == (length_shotCoords - 2): # !!! check if it counts all values
        
        # variabel for shoving values into the samePixelshot array
        start = indexStart
        end = nextPixel

        samePixelShots_length = end - start

        # A list to store pixel coordinates which are in the same shooting hole
        samePixelShots = np.zeros((samePixelShots_length, 2), dtype=int)

        # modifiy values in the samePixelshots 
        for i in range(samePixelShots_length):
            samePixelShots[i] = shotCoords[start]
            start += 1
        
        # modifiy the shape of the array so it can fit the requirements as input for boundingRec
        #samePixelShots = samePixelShots.reshape((-1,1,2)).astype(np.int32)
        newArray =  samePixelShots.reshape((-1,1,2)).astype(np.int32)
        # create a bounding rectangle around the pixels in the array
        x, y, w, h = cv.boundingRect(newArray)


        cv.rectangle(resized_img, (x, y), (x+w, y+h), (0, 255, 0), 0)

        recCount += 1

        # Find the center of the boundingRec
        center_x = x + int(w/2)
        center_y = y + int(h/2)

        

        # Draw lines from the center to the top-most and bottom-most pixels
        max_y = max(samePixelShots, key=lambda t: t[1])[1]
        min_y = min(samePixelShots, key=lambda t: t[1])[1]
        cv.line(resized_img, (center_x, center_y), (center_x, max_y), (255, 0, 0), 2)
        cv.line(resized_img, (center_x, center_y), (center_x, min_y), (255, 0, 0), 2)

        resized_img[center_y, center_x] = [255, 255, 255]

        topToBottom = max_y - min_y

        print("Shooting hole center: ",recCount,"| x:", center_x, "| y:", center_y," | top to bottom: ", topToBottom )



    # Move index value to look for pixels in the next shooting hole
        indexStart = nextPixel


#resized_img[center_y, center_x] = [255, 255, 255]

cv.imwrite(savePath, resized_img)
    
# Prints all shot coordinates 
'''
for x in range(shotValue):
    print(shotCoords[x])   
'''
print("\nNumber of pixel found in shooting holes: ",shotValue)
print("rectangle count: ", recCount, "\n")

print("Original Image resolution: ",img.shape[1], " | ", img.shape[0])
print("Resized image resolution",resized_width, " | ", resized_height)

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
