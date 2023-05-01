import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt

start_time = time.time()

def find_median(arr):
    arr.sort(key=lambda y: y[0])  # Sort by x-value
    length = len(arr)
    if length % 2 == 0:
        mid1 = length // 2
        mid2 = mid1 - 1
        median = ((arr[mid1][0] + arr[mid2][0]) / 2, (arr[mid1][1] + arr[mid2][1]) / 2)
    else:
        mid = length // 2
        median = arr[mid]
    return median

'''
def searchAreaMark(arr):
    
    newArray = []

    for firstPixel in arr:
        for points in arr:
            if (firstPixel[0] == points[0]):
                newArray.append(points)
    
    for i in newArray:
        resized_img = cv.circle(resized_img, (i[0],i[1]), 3, (255,0,255), -1)
'''
        
                    
                         


PATHT_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/senay_tele/w8_h6.jpg"

PATHS_1 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/1m.jpg"
PATHS_3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/opplosning_bilder/samuel_tele/0.65m.jpg"

# Function that reads the input image
img = cv.imread(PATHS_1)

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


# Color of the the circle to be drawn, red in this case. 
colorCircle = (0,255,0)

# Variable representing the size of the radius of the circle
CircleMarkingRadius = 1

# Thickness of the circle
thickness = -1

# Jump factor 
img_center_x = int((width / 2))
img_center_y = int((height)/ 2)

print(img_center_y)

count = True

jumpPixel_x = 7
jumpPixel_y = 5
jumpPixel_limit = 300
end_point = -1

whitePixel = 170
topLimit = bottomLimit = leftLimit = rightLimit = 0


#resized_img = cv.circle(resized_img, (img_center_x,1000), CircleMarkingRadius, colorCircle, thickness)
limitCircles = 0

#find Toplimit of search area for marked pixels
for i in range(img_center_y, end_point, -jumpPixel_limit):
        if(resized_img[i,img_center_x,0] > whitePixel and resized_img[i,img_center_x,1] > whitePixel  and resized_img[i,img_center_x,2] > whitePixel):
            resized_img = cv.circle(resized_img, (img_center_x,i), 100, (255,0,0), thickness)
            topLimit = i
            limitCircles += 1
            break


#find bottom of search area for marked pixels
for i in range(img_center_y, height, jumpPixel_limit):
        if(resized_img[i,img_center_x,0] > whitePixel and resized_img[i,img_center_x,1] > whitePixel  and resized_img[i,img_center_x,2] > whitePixel):
            
            resized_img = cv.circle(resized_img, (img_center_x,i), 100, (255,0,0), thickness)
            bottomLimit = i
            limitCircles += 1
            break  

#find left of search area for marked pixels
for i in range(img_center_x, end_point, -jumpPixel_limit):
        if(resized_img[img_center_y,i,0] > whitePixel and resized_img[img_center_y,i,1] > whitePixel  and resized_img[img_center_y,i,2] > whitePixel):
            resized_img = cv.circle(resized_img, (i,img_center_y), 100, (0,255,0), thickness)
            leftLimit = i
            limitCircles += 1
            break

#find right of search area for marked pixels
for i in range(img_center_x, width, jumpPixel_limit):
        if(resized_img[img_center_y,i,0] > whitePixel and resized_img[img_center_y,i,1] > whitePixel  and resized_img[img_center_y,i,2] > whitePixel):
            resized_img = cv.circle(resized_img, (i,img_center_y), 100, (0,255,0), thickness)
            rightLimit = i
            limitCircles += 1
            break

print(limitCircles)


# Check every pixel in each row to match the searching color
# Nested for loop which iterates through every pixel in the image by iterating through height and width of the image. 
for y in range(topLimit, bottomLimit,  jumpPixel_y):
    for x in range(leftLimit, rightLimit, jumpPixel_x):
        
        
        # @param img[heightPixel coord, rowPixel coord, indexColorPixel], SearchColor[index(B=0,G,1,R,2)]
        # if statement which compares the color of the current pixel with the specified color of SearchColor.
        if resized_img[y,x,0] < B and resized_img[y,x,1] < G  and (resized_img[y,x,2] > R[0] and resized_img[y,x,2] < R[1]):
           
            # @param index,2D values (y=height, x=width)
            shotCoords.insert(shotValue,[x,y]) 
            
            # Marking the shotpixel with circle
            resized_img = cv.circle(resized_img, (x,y), CircleMarkingRadius, colorCircle, thickness)
            shotValue += 1



# distance between two detected pixels
shotPixelDistance = 90

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

#variabel for shoving values into the samePixelshot array
#print(groups)


'''
for i in groups:
    newPoint = searchAreaMark(i)
    resized_img = cv.circle(resized_img, (int(newPoint[0]),int(newPoint[1])), 3, (255,0,0), -1)
    print(newPoint[0], newPoint[1])
'''

'''
medianArray = []

for group in groups:
    newArray = []

    for points in group:
        if (group[0][0] == points[0]):
            newArray.append(points)

    medianArray.append(find_median(newArray))
'''
'''
medianPoint = find_median(newArray)
resized_img = cv.circle(resized_img, (int(medianPoint[0]) + jumpPixel_x,int(medianPoint[1])), 3, (255,255,255), -1)
'''

for group in groups:
    x = group[0][0]
    y = group[0][1]

    print(x, y)

    resized_img = cv.circle(resized_img, (x,y), 3, (255,0,255), -1)
    #resized_img = cv2.rectangle(img, (x, y1), (x2, y2), (0, 255, 0), 2) # green rectangle with thickness of 2 pixels
    resized_img = cv.circle(resized_img, (x+shotPixelDistance , y+shotPixelDistance), 3, (0,255,255), -1)
    resized_img = cv.circle(resized_img, (x+shotPixelDistance , y-shotPixelDistance), 3, (0,255,255), -1)
    resized_img = cv.circle(resized_img, (x-shotPixelDistance , y+shotPixelDistance), 3, (0,255,255), -1)
    resized_img = cv.circle(resized_img, (x-shotPixelDistance , y-shotPixelDistance), 3, (0,255,255), -1)




marks = 0

centerPointsMark = []

for group in groups:

    group_length = len(group)

    samePixelShots = np.zeros((group_length, 2), dtype=int)

    for points in range(group_length):
        #print(group[points])
        samePixelShots[points] = group[points]

    x, y, w, h = cv.boundingRect(samePixelShots)

    cv.rectangle(resized_img, (x, y), (x+w, y+h), (0, 255, 255), 2)
    # Find the center of the boundingRec
    center_x = x + int(w/2)
    center_y = y + int(h/2)

    resized_img[center_y, center_x] = [255, 255, 255]
    centerPointsMark.append((center_x,center_y))
    #print("\n", samePixelShots, "\n")
    marks += 1
    
print(centerPointsMark)

resized_img = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)

imgplot = plt.imshow(resized_img)


plt.xlim(0,resized_width)
plt.ylim(resized_height, 0)

#plt.savefig('books_read.png')
plt.show()

'''
# Display the image
cv.imshow('Image', resized_img)

# Wait for a key press and then close the window
cv.waitKey(0)
cv.destroyAllWindows()
'''


print("\n Process finished in:", np.ceil((time.time()- start_time)),"seconds")
