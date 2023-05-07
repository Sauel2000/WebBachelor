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

def find_center(img):
    width = 9000
    height = 12000

    x = width // 2
    y = height // 2

    arr = []

    count = 0
    blackPixel = 50
    whitePixel = 170

    checkLimit = 10

    for i in range(x,width, 100):
        if (img[y,i,0] < blackPixel and img[y,i,1] < blackPixel and img[y,i,2] < blackPixel):
            point = (i, y)
            arr.append(point)
    
        if (img[y,i,0] > whitePixel and img[y,i,1] > whitePixel and img[y,i,2] > whitePixel):
            count += 1

        if (count == checkLimit):
            break


    count = 0

    for i in range(x,0, -100):
        #cv.circle(img, (i,y), 10, (255,0,255), thickness)

        
        if (img[y,i,0] < blackPixel and img[y,i,1] < blackPixel and img[y,i,2] < blackPixel):
            point = (i, y)
            arr.append(point)
        
        if(img[y,i,0] > whitePixel and img[y,i,1] > whitePixel and img[y,i,2] > whitePixel):
            count += 1

            #img = cv.circle(img, (i,y), CircleMarkingRadius, (255,0,0), thickness)
            
        if (count == checkLimit):
                break
        
    rightMostPixel = max(arr[i][0] for i in range(len(arr)))
    leftMostPixel = min(arr[i][0] for i in range(len(arr))) 

    distance_x = ((rightMostPixel - leftMostPixel) // 2) + leftMostPixel

    arr.clear()

    count = 0

    for i in range(y,height, 100):
    
        if (img[i,distance_x,0] < blackPixel and img[i,distance_x,1] < blackPixel and img[i,distance_x,2] < blackPixel):
            point = (i, y)
            arr.append(point)
        
        if (img[i,distance_x,0] > whitePixel and img[i,distance_x,1] > whitePixel and img[i,distance_x,2] > whitePixel):
            count += 1

        if (count == checkLimit):
            break

    count = 0
    for i in range(y,0, -100):
        #cv.circle(img, (i,y), 10, (255,0,255), thickness)

        
        if (img[i,distance_x,0] < blackPixel and img[i,distance_x,1] < blackPixel and img[i,distance_x,2] < blackPixel):
            point = (i, y)
            arr.append(point)
        
        if(img[i,distance_x,0] > whitePixel and img[i,distance_x,1] > whitePixel and img[i,distance_x,2] > whitePixel):
            count += 1

            img = cv.circle(img, (i,y), CircleMarkingRadius, (255,0,0), thickness)
            
        if (count == checkLimit):
                break

    bottomMostPixel = max(arr[i][0] for i in range(len(arr)))
    topMostPixel = min(arr[i][0] for i in range(len(arr)))

    distance_y =  ((bottomMostPixel - topMostPixel) // 2) + topMostPixel


    circleRadius = 50
    circleThickness = -1
    verticalColorCircle = (255, 0, 0)
    HorizontalColorCircle = (0, 255, 0)
    # display horixontal lines 
    img = cv.circle(img, (leftMostPixel,y), circleRadius, verticalColorCircle, circleThickness)
    img = cv.circle(img, (rightMostPixel,y), circleRadius, verticalColorCircle, circleThickness)
    img = cv.circle(img, (distance_x,y), circleRadius, verticalColorCircle, circleThickness)

    # display vertical line and the point where we search searching area from
    img = cv.circle(img, (distance_x,topMostPixel), circleRadius,HorizontalColorCircle, circleThickness)
    img = cv.circle(img, (distance_x,bottomMostPixel), circleRadius, HorizontalColorCircle, circleThickness)
    img = cv.circle(img, (distance_x,distance_y), circleRadius, HorizontalColorCircle, circleThickness)

    return (distance_x, distance_y)

def find_searching_area_limits(img, img_center_x, img_center_y):

    # Jump certain amount of pixel to find the limit of searching Area
    jumpPixel_limit = 300
    end_point = -1

    whitePixel = 170
    topLimit = bottomLimit = leftLimit = rightLimit = 0


    #resized_img = cv.circle(resized_img, (img_center_x,1000), CircleMarkingRadius, colorCircle, thickness)
    limitCircles = 0

    #find Toplimit of search area for marked pixels
    for i in range(img_center_y, end_point, -jumpPixel_limit):
            
            if(img[i,img_center_x,0] > whitePixel and img[i,img_center_x,1] > whitePixel  and img[i,img_center_x,2] > whitePixel):
                img = cv.circle(img, (img_center_x,i), 100, (255,0,0), thickness)
                topLimit = i
                limitCircles += 1
                break


    #find bottom of search area for marked pixels
    for i in range(img_center_y, height, jumpPixel_limit):
            if(img[i,img_center_x,0] > whitePixel and img[i,img_center_x,1] > whitePixel  and img[i,img_center_x,2] > whitePixel):
                
                img = cv.circle(img, (img_center_x,i), 100, (255,0,0), thickness)
                bottomLimit = i
                limitCircles += 1
                break  

    #find left of search area for marked pixels
    for i in range(img_center_x, end_point, -jumpPixel_limit):
            if(img[img_center_y,i,0] > whitePixel and img[img_center_y,i,1] > whitePixel  and img[img_center_y,i,2] > whitePixel):

                img = cv.circle(img, (i,img_center_y), 100, (0,255,0), thickness)
                leftLimit = i
                limitCircles += 1
                break

    #find right of search area for marked pixels
    for i in range(img_center_x, width, jumpPixel_limit):
            
            if(img[img_center_y,i,0] > whitePixel and img[img_center_y,i,1] > whitePixel  and img[img_center_y,i,2] > whitePixel):
                img = cv.circle(img, (i,img_center_y), 100, (0,255,0), thickness)
                rightLimit = i
                limitCircles += 1
                break
    
    return (topLimit, bottomLimit, leftLimit, rightLimit)

def SearchAreaMark(img, groups):
    for group in groups:
        x = group[0][0]
        y = group[0][1]
        
        # Which pixel we use to look for other pixels to group
        img = cv.circle(img, (x,y), 3, (255,0,255), -1)

        # The total square to find the pixels in the same group or same shooting hole
        img = cv.circle(img, (x+shotPixelDistance , y+shotPixelDistance), 3, (0,255,255), -1)
        img = cv.circle(img, (x+shotPixelDistance , y-shotPixelDistance), 3, (0,255,255), -1)
        img = cv.circle(img, (x-shotPixelDistance , y+shotPixelDistance), 3, (0,255,255), -1)
        img = cv.circle(img, (x-shotPixelDistance , y-shotPixelDistance), 3, (0,255,255), -1)

def groupPixelWithSameRGB(img, shotCoords, searchingLimits, color):
    
    
    topLimit = searchingLimits[0]
    bottomLimit = searchingLimits[1]
    leftLimit = searchingLimits[2]
    rightLimit = searchingLimits[3]


    # RGB interval to find the pixels we are looking for
    if (color == 0):
        R = (150, 256)
        G = 120  
        B = 80

    elif(color == 1):
        R = (150, 256)
        G = 120  
        B = 80


    jumpPixel_x = 7
    jumpPixel_y = 5


    # Check every pixel in each row to match the searching color
    # Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
    for y in range(topLimit, bottomLimit,  jumpPixel_y):
        for x in range(leftLimit, rightLimit, jumpPixel_x):
            
            # @param img[heightPixel coord, rowPixel coord, indexColorPixel], SearchColor[index(B=0,G,1,R,2)]
            # if statement which compares the color of the current pixel with the specified color of SearchColor.
            if img[y,x,0] < B and img[y,x,1] < G  and (img[y,x,2] > R[0] and img[y,x,2] < R[1]):
            
                # @param index,2D values (y=height, x=width)
                shotCoords.append([x,y]) 
                
                # Marking the shotpixel with circle
                #img = cv.circle(img, (x,y), CircleMarkingRadius, colorCircle, thickness)

    return shotCoords

def findCenterPixelOnMark(groups):

    centerPointsMark = []


    for group in groups:

        group_length = len(group)

        samePixelShots = np.zeros((group_length, 2), dtype=int)

        for points in range(group_length):
            #print(group[points])
            samePixelShots[points] = group[points]

        x, y, w, h = cv.boundingRect(samePixelShots)

        #cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)

        # Find the center of the boundingRec
        center_x = x + int(w/2)
        center_y = y + int(h/2)

        img[center_y, center_x] = [255, 255, 255]
        centerPointsMark.append((center_x,center_y))
    
    return centerPointsMark

def groupPixels_inSameMark(shotCoords):


    # Group of pixels
    groups = []

    # check if marked pixels are in right shooting hole and divide- 
    # -Them into right groups depended on shooting holes 
    for point in shotCoords:

        matched_group = None
        
        for group in groups:

            if ((abs(point[0] - group[0][0]) < shotPixelDistance) and (abs(point[1] - group[0][1]) < shotPixelDistance)):
                matched_group = group
                break

        if matched_group is not None:
            matched_group.append(point)
        else:
            groups.append([point])
    
    return groups
# Function that reads the input image
img = cv.imread(PATHS_6)

# Image scale
width = img.shape[1]
height = img.shape[0]

print(width, height)

dim = (width, height)


# A list to store the coordinates of all pixels in all shooting holes that are detected
shotCoords = []

# Color of the the circle to be drawn, red in this case. 
colorCircle = (0,255,0)

# Variable representing the size of the radius of the circle
CircleMarkingRadius = 1

# Thickness of the circle
thickness = -1

# Starting point from where we utilize Jump factor to find searching Area
centerPoint = find_center(img)
img_center_x = centerPoint[0]
img_center_y = centerPoint[1]

searchingLimits = find_searching_area_limits(img,img_center_x, img_center_y)


blue = 0
red = 1

shotCoords = groupPixelWithSameRGB(img, shotCoords, searchingLimits, blue)

startLook = shotCoords[0]
pixelDistance_arr = []

for points in shotCoords:
    if(points[0] == startLook[0]):
         pixelDistance_arr.append(points)


# distance between two detected pixels
endLook = max(pixelDistance_arr[i][1] for i in range(len(pixelDistance_arr)))
pixelDistance_deviation = 15
shotPixelDistance = (endLook - startLook[1] ) + pixelDistance_deviation

#print(shotPixelDistance)

groups = groupPixels_inSameMark(shotCoords)


#variabel for shoving values into the samePixelshot array
#print(groups)

SearchAreaMark(img, groups)

centerPixels = findCenterPixelOnMark(groups)

print(centerPixels)
#print(marks)  

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

imgplot = plt.imshow(img)


plt.xlim(0,width)
plt.ylim(height, 0)
plt.show()

print("\n Process finished in:", np.ceil((time.time()- start_time)),"seconds")
