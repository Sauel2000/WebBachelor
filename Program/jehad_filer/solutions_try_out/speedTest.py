import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt

# 
start_time = time.time()                
                         


PATHT_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/w8_h6.jpg"

PATHS_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/1m.jpg"
PATHS_3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/0.65m.jpg"

PATHS_4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/1.5m.jpg"
PATHS_5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/2m.jpg"
PATHS_6 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/2.5m.jpg"
PATHS_7 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/3m.jpg"

path_blue_0 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/bla_mark.jpg"
path_blue_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/bla_0.65m.jpg"
path_blue_2 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/bla_1m.jpg"
path_blue_3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/bla_1.5m.jpg"

path_blue_4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/blaWhite_mark_0.65m.jpg"
path_blue_5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/blaWhite_mark_1m.jpg"
path_blue_7 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/blaWhite_mark_1.5m.jpg"

Vw1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/greenMark_0.65m.jpg"
G1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/greenMark_0.65m.jpg"
blue = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/lightbla_tag.jpg"

blue2 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/strongBlue_mark_0.65m.jpg"


test = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/testMarks.jpg"


P1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/lightMarks_top.jpg"
P2 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/lightMarks_bottom.jpg"


P3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/darkMarks_top.jpg"
P4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/darkMarks_bottom.jpg"



# create a square for searching area
def find_searching_area_limits(img, img_center_x, img_center_y):


    # Jump certain amount of pixel to find the limit of searching Area
    jumpPixel_limit = 600

    # to calculate to start of the image in y and x axis
    end_point = -1

    # min value for detection of white pixel
    whitePixel = 150
    
    # values for knowing the limit of searching area 
    topLimit = bottomLimit = leftLimit = rightLimit = 0

    # count amount of circles created
    limitCircles = 0

    # Radius ofr circles
    circleRadius = 20
    
    #find Toplimit of search area for marked pixels
    for i in range(img_center_y, end_point, -jumpPixel_limit):
            
            if(img[i,img_center_x,0] > whitePixel and img[i,img_center_x,1] > whitePixel  and img[i,img_center_x,2] > whitePixel):
                limitPosition = i -jumpPixel_limit
                img = cv.circle(img, (img_center_x, limitPosition), circleRadius, (0,255,0), thickness)
                topLimit = limitPosition
                limitCircles += 1
                break


    #find bottom of search area for marked pixels
    for i in range(img_center_y, height, jumpPixel_limit):
            
            if(img[i,img_center_x,0] > whitePixel and img[i,img_center_x,1] > whitePixel  and img[i,img_center_x,2] > whitePixel):
                limitPosition = i +jumpPixel_limit
                img = cv.circle(img, (img_center_x,limitPosition), circleRadius, (0,255,0), thickness)
                bottomLimit = limitPosition
                limitCircles += 1
                break  

    #find left of search area for marked pixels
    for i in range(img_center_x, end_point, -jumpPixel_limit):
                        
            if(img[img_center_y,i,0] > whitePixel and img[img_center_y,i,1] > whitePixel  and img[img_center_y,i,2] > whitePixel):
                
                limitPosition = i - jumpPixel_limit
                img = cv.circle(img, (limitPosition,img_center_y), circleRadius, (0,255,0), thickness)
                leftLimit = limitPosition
                limitCircles += 1
                break

    #find right of search area for marked pixels
    for i in range(img_center_x, width, jumpPixel_limit): 
            
            if(img[img_center_y,i,0] > whitePixel and img[img_center_y,i,1] > whitePixel  and img[img_center_y,i,2] > whitePixel):
                limitPosition = i + jumpPixel_limit
                img = cv.circle(img, (limitPosition,img_center_y), circleRadius, (0,255,0), thickness)
                rightLimit = limitPosition
                limitCircles += 1
                break
    
    return (topLimit, bottomLimit, leftLimit, rightLimit)

# look for pixel with a same RGB interval and group them
def groupPixelWithSameRGB(img, shotCoords, searchingLimits, color):
    

    # values of each limits for the searching area
    topLimit = searchingLimits[0]
    bottomLimit = searchingLimits[1]
    leftLimit = searchingLimits[2]
    rightLimit = searchingLimits[3]
    
    # amount of pixels to jump 
    jumpPixel_x = 7
    jumpPixel_y = 5

    # RGB interval to find the pixels we are looking for
    if color == 0:
        R = 80  
        G = (70, 140) 
        B = (70, 150)

        
        # Check every pixel in each row to match the searching color
        # Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
        for y in range(topLimit, bottomLimit,  jumpPixel_y):
            for x in range(leftLimit, rightLimit, jumpPixel_x):
                
                # @param img[heightPixel coord, rowPixel coord, indexColorPixel], SearchColor[index(B=0,G,1,R,2)]
                # if statement which compares the color of the current pixel with the specified color of SearchColor.
                if (img[y,x,0] < B[1] and img[y,x,0] > B[0]) and img[y, x, 1] > G[0] and img[y,x,1] < G[1]  and (img[y,x,2] < R):
                
                    # @param index,2D values (y=height, x=width)
                    shotCoords.append([x,y]) 
                    
                    # Marking the shotpixel with circle
                    img = cv.circle(img, (x,y), CircleMarkingRadius, colorCircle, thickness)

        return shotCoords
    
    elif color == 1:
            R = (170, 256)
            G = 80
            B = 80

            # Check every pixel in each row to match the searching color
            # Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
            for y in range(topLimit, bottomLimit,  jumpPixel_y):
                for x in range(leftLimit, rightLimit, jumpPixel_x):
                    
                    # @param img[heightPixel coord, rowPixel coord, indexColorPixel], SearchColor[index(B=0,G,1,R,2)]
                    # if statement which compares the color of the current pixel with the specified color of SearchColor.
                    if img[y,x,0] < B and img[y,x,1] < G  and (img[y,x,2] > R[0] and img[y, x,2] < R[1]):
                    
                        shotCoords.append([x,y]) 
            
            return shotCoords
    
# Group pixels with is in the same shooting hole
def groupPixels_inSameMark(shotCoords):


    # Group of pixels
    groups = []

    # check if marked pixels are in right shooting hole and divide- 
    # -Them into right groups depended on shooting holes 
    for point in shotCoords:

        matched_group = None
        
        for group in groups:

            # check if the first detect pixel(x, y)  values compared to all detected pixels are less then a certain distance 
            if ((abs(point[0] - group[0][0]) < shotPixelDistance) and (abs(point[1] - group[0][1]) < shotPixelDistance)):
                matched_group = group
                break

        if matched_group is not None:
            matched_group.append(point)
        else:
            groups.append([point])
    
    return groups
# mark and find the center of every shooting hole
def findCenterPixelOnMark(groups):


    # values of pixel in the center of different marks
    centerPointsMark = []


    # create a square round grouped pixels and mark and calculate the center of the square
    # save all the mark position in a array as points with x and y values
    for group in groups:

        group_length = len(group)

        samePixelShots = np.zeros((group_length, 2), dtype=int)

        for points in range(group_length):
            #print(group[points])
            samePixelShots[points] = group[points]

        x, y, w, h = cv.boundingRect(samePixelShots)

        #cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 5)

        # Find the center of the boundingRec
        center_x = x + int(w/2)
        center_y = y + int(h/2)

        img[center_y, center_x] = [255, 255, 255]
        centerPointsMark.append((center_x,center_y))
    
    return centerPointsMark

# mark a square to show searching are of pixels in the same shooting hole
def SearchAreaMark(img, groups):

    # loop through first pixel detected per Mark
    for group in groups:
        x = group[0][0]
        y = group[0][1]
        
        # Which pixel we use to look for other pixels to group in the same mark
        img = cv.circle(img, (x,y), 3, (255,0,255), -1)

        # The total square to find the pixels in the same group or same Mark
        img = cv.circle(img, (x+shotPixelDistance , y+shotPixelDistance), 3, (0,255,255), -1)
        img = cv.circle(img, (x+shotPixelDistance , y-shotPixelDistance), 3, (0,255,255), -1)
        img = cv.circle(img, (x-shotPixelDistance , y+shotPixelDistance), 3, (0,255,255), -1)
        img = cv.circle(img, (x-shotPixelDistance , y-shotPixelDistance), 3, (0,255,255), -1)



# Function that reads the input image
img = cv.imread(P1)

# Image resolution
width = img.shape[1]
height = img.shape[0]

dim = (width, height)


# A list to store the coordinates of all pixels in all shooting holes that are detected
shotCoords = []

# Color of the the circle to be drawn, red in this case. 
colorCircle = (0,255,0)

# Variable representing the size of the radius of the circle
CircleMarkingRadius = 2

# Thickness of the circle
thickness = -1

# Starting point from where we utilize Jump factor to find searching Area



img_center_x = width // 2
img_center_y = height // 2

# Mark ish the center of shooting target
#img = cv.circle(img, (img_center_x,img_center_y), 50, (0,255,0), -1)

# find the searching area
searchingLimits = [0, width- 1000, 0, height - 1000]

# color of marks to look for
blue = 0
red = 1

# Store all pixels that has the same rgb interval
shotCoords = groupPixelWithSameRGB(img, shotCoords, searchingLimits, 0)


# first pixel detected with a defined rgb value
if shotCoords is not None: 
    startLook = shotCoords[0]
pixelDistance_arr = []

# look for amount of pixels in horizontal line for the first mark detected.
for points in shotCoords:
    if(points[0] == startLook[0] and abs(points[1] - startLook[1]) < 500 ):
         pixelDistance_arr.append(points)


# distance between two detected pixels
endLook = max(pixelDistance_arr[i][1] for i in range(len(pixelDistance_arr)))
pixelDistance_deviation = 30

# 
shotPixelDistance = (endLook - startLook[1] ) + pixelDistance_deviation

print(shotPixelDistance)
# gather pixels in the same shooting holes in each individual group
groups = groupPixels_inSameMark(shotCoords)

# mark searching area for shooting hole pixels
SearchAreaMark(img, groups)

# get the values of pixel in the center of each shooting hole
centerPixels = findCenterPixelOnMark(groups)


print(centerPixels)
 

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