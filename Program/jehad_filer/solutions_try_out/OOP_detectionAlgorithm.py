import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt
 
class markingCenters:

    # A list to store the coordinates of all pixels in all shooting holes that are detected
    shotCoords = []

    def __init__(self, img):
        self.img = img
        self.width = img.shape[1]
        self.height = img.shape[0]

    # find a pixel close to the center of the shooting target 
    def find_center(self, display = False):

        # center of image based on resolution
        x = self.width // 2
        y = self.height // 2

        # Array for black pixels detected, black pixels is supposed to represent the target
        blackPixelsArray = []

        # count how many times we detect white pixel
        count = 0

        # value that is max threshold for black pixel
        blackPixel = 50

        # value that is min threshold from 170 to 255
        whitePixel = 170

        # check amount of times for white pixelø
        checkLimit = 10

        # look in axis'es for black pixels, if found put it into array and if not add 1 to count and if you find white pixels 10 times, stop. 
        # look in +x axis 
        for i in range(x, self.width, 100):
            if (self.img[y,i,0] < blackPixel and self.img[y,i,1] < blackPixel and self.img[y,i,2] < blackPixel):
                point = (i, y)
                blackPixelsArray.append(point)

            if (self.img[y,i,0] > whitePixel and self.img[y,i,1] > whitePixel and self.img[y,i,2] > whitePixel):
                count += 1

            if (count == checkLimit):
                break
        


        # count how many times we detect white pixel (We reset the value here to 0)
        count = 0

        # look in axis'es for black pixels, if found put it into array and if not add 1 to count and if you find white pixels 10 times, stop. 
        # look in -x axis 
        for i in range(x,0, -100):
            
            if (self.img[y,i,0] < blackPixel and self.img[y,i,1] < blackPixel and self.img[y,i,2] < blackPixel):
                point = (i, y)
                blackPixelsArray.append(point)
            
            if(self.img[y,i,0] > whitePixel and self.img[y,i,1] > whitePixel and self.img[y,i,2] > whitePixel):
                count += 1
                
            if (count == checkLimit):
                    break
        
        #Find the black pixel which is furthest to the right           
        rightMostPixel = max(blackPixelsArray[i][0] for i in range(len(blackPixelsArray)))
        
        #Find the black pixel which is furthest to the left           
        leftMostPixel = min(blackPixelsArray[i][0] for i in range(len(blackPixelsArray))) 

        # Find the center x value between leftMostPixel and rightMostPixel
        distance_x = ((rightMostPixel - leftMostPixel) // 2) + leftMostPixel

        # clear array to input new black pixels when we look for y values next
        blackPixelsArray.clear()

        # count how many times we detect white pixel (We reset the value here to 0)
        count = 0


        # look in axis'es for black pixels, if found put it into array and if not add 1 to count and if you find white pixels 10 times, stop. 
        # look in y axis 
        for i in range(y, self.height, 100):
        
            if (self.img[i,distance_x,0] < blackPixel and self.img[i,distance_x,1] < blackPixel and self.img[i,distance_x,2] < blackPixel):
                point = (i, y)
                blackPixelsArray.append(point)
            
            if (self.img[i,distance_x,0] > whitePixel and self.img[i,distance_x,1] > whitePixel and self.img[i,distance_x,2] > whitePixel):
                count += 1

            if (count == checkLimit):
                break

        # count how many times we detect white pixel (We reset the value here to 0)
        count = 0

        # look in -y axis 
        for i in range(y,0, -100):
            
            if (self.img[i,distance_x,0] < blackPixel and self.img[i,distance_x,1] < blackPixel and self.img[i,distance_x,2] < blackPixel):
                point = (i, y)
                blackPixelsArray.append(point)
            
            if(self.img[i,distance_x,0] > whitePixel and self.img[i,distance_x,1] > whitePixel and self.img[i,distance_x,2] > whitePixel):
                count += 1

            if (count == checkLimit):
                    break
            
        #find the top and bottom most pixel 
        bottomMostPixel = max(blackPixelsArray[i][0] for i in range(len(blackPixelsArray)))
        topMostPixel = min(blackPixelsArray[i][0] for i in range(len(blackPixelsArray)))

        # find the center y value between the most top and bottom black pixel
        distance_y =  (( bottomMostPixel - topMostPixel) // 2) + topMostPixel


        if display == True:

            circleRadius = 50
            circleThickness = -1
            verticalColorCircle = (255, 0, 0)
            HorizontalColorCircle = (0, 255, 0)


            # display horixontal lines 
            self.img = cv.circle(self.img, (leftMostPixel,y), circleRadius, verticalColorCircle, circleThickness)
            self.img = cv.circle(self.img, (rightMostPixel,y), circleRadius, verticalColorCircle, circleThickness)
            self.img = cv.circle(self.img, (distance_x,y), circleRadius, verticalColorCircle, circleThickness)

            # display vertical line and the point where we search searching area from
            self.img = cv.circle(self.img, (distance_x,topMostPixel), circleRadius,HorizontalColorCircle, circleThickness)
            self.img = cv.circle(self.img, (distance_x,bottomMostPixel), circleRadius, HorizontalColorCircle, circleThickness)
            self.img = cv.circle(self.img, (distance_x,distance_y), circleRadius, HorizontalColorCircle, circleThickness)

        return (distance_x, distance_y)
        
    # create a square for searching area
    def find_searching_area_limits(self, display = False):

        # Starting point from where we utilize Jump factor to find searching Area
        centerPoint = self.find_center()
        img_center_x = centerPoint[0]
        img_center_y = centerPoint[1]


        # Jump certain amount of pixel to find the limit of searching Area
        jumpPixel_limit = 500

        # to calculate start of the image in y and x axis
        end_point = -1

        # min value for detection of white pixel
        whitePixel = 150
        
        # values for knowing the limit of searching area 
        topLimit = bottomLimit = leftLimit = rightLimit = 0

        # count amount of circles created ( For testing )
        limitCircles = 0
        
        #find Toplimit of search area for marked pixels
        for i in range(img_center_y, end_point, -jumpPixel_limit):
                
                # Look for white pixels, if found, jump another certain amount of pixels and consider it a limit for searching area
                if(self.img[i,img_center_x,0] > whitePixel and self.img[i,img_center_x,1] > whitePixel  and self.img[i,img_center_x,2] > whitePixel):
                    
                    limitPosition = i -jumpPixel_limit
                    topLimit = limitPosition
                    limitCircles += 1
                    break


        #find bottom of search area for marked pixels
        for i in range(img_center_y, self.height, jumpPixel_limit):
                
                # Look for white pixels, if found, jump another certain amount of pixels and consider it a limit for searching area
                if(self.img[i,img_center_x,0] > whitePixel and self.img[i,img_center_x,1] > whitePixel  and self.img[i,img_center_x,2] > whitePixel):
                    
                    limitPosition = i +jumpPixel_limit
                    bottomLimit = limitPosition
                    limitCircles += 1
                    break  

        #find left of search area for marked pixels
        for i in range(img_center_x, end_point, -jumpPixel_limit):
            
                 # Look for white pixels, if found, jump another certain amount of pixels and consider it a limit for searching area
                if(self.img[img_center_y,i,0] > whitePixel and self.img[img_center_y,i,1] > whitePixel  and self.img[img_center_y,i,2] > whitePixel):
                    
                    limitPosition = i - jumpPixel_limit
                    leftLimit = limitPosition
                    limitCircles += 1
                    break

        #find right of search area for marked pixels
        for i in range(img_center_x, self.width, jumpPixel_limit): 
                
                # Look for white pixels, if found, jump another certain amount of pixels and consider it a limit for searching area
                if(self.img[img_center_y,i,0] > whitePixel and self.img[img_center_y,i,1] > whitePixel  and self.img[img_center_y,i,2] > whitePixel):
                   
                    limitPosition = i + jumpPixel_limit
                    rightLimit = limitPosition
                    limitCircles += 1
                    break
        
        # Display all Limits on the image ( for testing )
        if display == True:

            circleRadius = 50
            circleThickness = -1
            ColorCircle = (255, 0, 255)

            # display horixontal lines 
            self.img = cv.circle(self.img, (img_center_x, topLimit), circleRadius, ColorCircle, circleThickness)
            self.img = cv.circle(self.img, (img_center_x, bottomLimit), circleRadius, ColorCircle, circleThickness)
            self.img = cv.circle(self.img, (leftLimit, img_center_y), circleRadius, ColorCircle, circleThickness)
            self.img = cv.circle(self.img, (rightLimit, img_center_y), circleRadius, ColorCircle, circleThickness)

        
        return (topLimit, bottomLimit, leftLimit, rightLimit)

    # look for pixel with a same RGB interval and group them
    def groupPixelWithSameRGB(self, color, display = False):
        
        # find the searching area
        searchingLimits = self.find_searching_area_limits()


        # values of each limits for the searching area
        topLimit = searchingLimits[0]
        bottomLimit = searchingLimits[1]
        leftLimit = searchingLimits[2]
        rightLimit = searchingLimits[3]

        # amount of pixels to jump 
        jumpPixel_x = 7
        jumpPixel_y = 5

        CircleMarkingRadius = 1
        colorCircle = (0, 255, 0)
        thickness = -1

        # RGB interval to find the pixels we are looking for
        if color == "blue":
            R = 90
            G = (70, 140)
            B = (100, 190)

            # Check every pixel in each row to match the searching color
            # Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
            for y in range(topLimit, bottomLimit,  jumpPixel_y):
                for x in range(leftLimit, rightLimit, jumpPixel_x):
                    
                    # check for certian RGB values from pixels and add them to an array if found
                    if (self.img[y,x,0] < B[1] and self.img[y,x,0] > B[0]) and self.img[y,x,1] > G[0]  and self.img[y,x,1] < G[1]  and (self.img[y,x,2] < R):
                        
                        # Expected to be close to other Pixel that have same RGB values, therefore we lower the jump to detect more of the same pixels
                        jumpPixel_x = 3
                        self.shotCoords.append([x,y]) 

                        # Display  every pixel that are detected based on the RGB interval ( Only for testing )
                        if display == True:
                            self.img = cv.circle(img, (x,y), CircleMarkingRadius, colorCircle, thickness)
                    else:
                        jumpPixel_x = 7

            return self.shotCoords
        
        elif color == "red":
            R = (170, 256)
            G = 70
            B = 70

            # Check every pixel in each row to match the searching color
            # Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
            for y in range(topLimit, bottomLimit,  jumpPixel_y):
                for x in range(leftLimit, rightLimit, jumpPixel_x):
                    
                    # @param img[heightPixel coord, rowPixel coord, indexColorPixel], SearchColor[index(B=0,G,1,R,2)]
                    # if statement which compares the color of the current pixel with the specified color of SearchColor.
                    if self.img[y,x,0] < B and self.img[y,x,1] < G  and (self.img[y,x,2] > R[0] and self.img[y, x,2] < R[1]):
                        
                        # Expected to be close to other Pixel that have same RGB values, therefore we lower the jump to detect more of the same pixels
                        jumpPixel_x = 3
                        self.shotCoords.append([x,y]) 

                        # Display  every pixel that are detected based on the RGB interval ( Only for testing )
                        if display == True:

                            self.img = cv.circle(self.img, (x,y), CircleMarkingRadius, colorCircle, thickness)
                    else:
                        jumpPixel_x = 7

            return self.shotCoords

    # Group pixels which is in the same shooting hole
    def groupPixels_inSameMark(self):

        groups = []

        # First detected pixel on a shooting hole
        startLook = self.shotCoords[0]

        pixelDistance_arr = []

        # group all pixels in the first detected shooting hole
        for points in self.shotCoords:
            if(points[0] == startLook[0] and abs(points[1] - startLook[1]) < 500 ):
                pixelDistance_arr.append(points)


        # Use the first pixel detected which is mostlikely the top pixel on a shooting mark
        # Find the Pixel that is the furthest in Y axis from the first pixel detected
        # find the distance and add certain amount of extra pixels to group all pixels based on that distance
        endLook = max(pixelDistance_arr[i][1] for i in range(len(pixelDistance_arr)))
        pixelDistance_deviation = 15
        shotPixelDistance = (endLook - startLook[1] ) + pixelDistance_deviation


        # check if marked pixels are in right shooting hole and divide- 
        # -them into right groups depended on shooting holes and distance they are away from the first pixel detected-
        # -on every shooting hole
        for point in self.shotCoords:

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
    def findCenterPixelOnMark(self, display = False):

        # Groups of pixels based on different shooting holes
        groups = self.groupPixels_inSameMark()

        # Array for pixels that are center of each shooting hole
        centerPointsMark = []


        # create a bounding rectangle around pixels detected in a group ( shooting hole )
        # Find the center of the rectangle and consider it the center of the shooting hole
        for group in groups:

            group_length = len(group)

            samePixelShots = np.zeros((group_length, 2), dtype=int)

            for points in range(group_length):
                samePixelShots[points] = group[points]

            x, y, w, h = cv.boundingRect(samePixelShots)

            if display == True:
                cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)

            # Find the center of the boundingRec
            center_x = x + int(w/2)
            center_y = y + int(h/2)

            self.img[center_y, center_x] = [255, 255, 255]
            centerPointsMark.append((center_x,center_y))
        
        return centerPointsMark

    # Get the values of the X and Y for all the center of marks depending on the color your searching for.
    def get_centerValues(self, color, display):
        self.shotCoords.clear()
        self.groupPixelWithSameRGB(color)
        self.groupPixels_inSameMark()
        centerPoints = self.findCenterPixelOnMark()
        return centerPoints



PATHS_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/1m.jpg"
PATHS_3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/0.65m.jpg"

PATHS_4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/1.5m.jpg"
PATHS_5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/2m.jpg"
PATHS_6 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/2.5m.jpg"
PATHS_7 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/3m.jpg"


PATH9 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/bla_mark.jpg"
PATH11 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/bla_0.65m.jpg"
path_blue_2 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/bla_1m.jpg"
path_blue_3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/bla_1.5m.jpg"

path_blue_4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/blaWhite_mark_0.65m.jpg"
path_blue_5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/blaWhite_mark_1m.jpg"
path_blue_7 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/blaWhite_mark_1.5m.jpg"

blue2 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/strongBlue_mark_0.65m.jpg"
fullTest = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/2m_test.jpg"


L1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/lights/standardLights.jpg"
L2 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/lights/darkLights.jpg"
L3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/lights/blitzLights.jpg"
L4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/lights/handOverLights.jpg"



start_time = time.time()                

# Function that reads the input image
img = cv.imread(fullTest)

width = img.shape[1]
height = img.shape[0]

#blueMark = markingCenters(img).get_centerValues("blue")

blueMarks = markingCenters(img).get_centerValues("blue", False)
redMarks = markingCenters(img).get_centerValues("red", False)

test = markingCenters(img)

#test.find_center(True)
test.find_searching_area_limits(True)
#test.groupPixelWithSameRGB("red", True)
#test.groupPixelWithSameRGB("blue", True)
test.findCenterPixelOnMark(True)



print(blueMarks)
print(redMarks)

redMark = cv.cvtColor(img, cv.COLOR_BGR2RGB)

imgplot = plt.imshow(redMark)


plt.xlim(0,width)
plt.ylim(height, 0)
plt.show()


print("\n Process finished in:", np.ceil((time.time()- start_time)),"seconds")


