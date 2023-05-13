import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from ImageInfoClass2 import CalibrationSys
from markedAxisShoot import markingCenters
import math
import cv2 as cv


path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/A2.jpg"


img = cv.imread(path)

heightPixels = (img.shape[0])   #Width in pic in pixles
widthPixels =(img.shape[1])     #Height in pic in pixles


redMarks = markingCenters(img).get_centerValues("red",False)



lowest_x = redMarks[0] # initialize lowest element x in list
lowest_y = redMarks[0] # initialize lowest element y in list
highest_x = redMarks[0] 
highest_y = redMarks[0] 

for tuple in redMarks:
    if tuple[0] < lowest_x[0]:
        lowest_x = tuple
    print(tuple[1])
    if tuple[1] < lowest_y[1]:
        lowest_y = tuple
    if tuple[0] > highest_x[0]:
        highest_x = tuple
    if tuple[1] > highest_y[0]:
        highest_y = tuple

print("X",lowest_x,"Y", lowest_y)

print(redMarks,"Red")

# Define the starting and ending points of the first vector
hor_start = np.array([lowest_x[0],lowest_x[1]])
hor_end = np.array([highest_x[0], highest_x[1]])



# Define the starting and ending points of the second vector
ver_start = np.array([lowest_y[0],lowest_y[1]])
ver_end = np.array([highest_y[0],highest_y[1]])
intersection_point = []








# Finding direction vector of horizontal and vertical
v1_dir = hor_end - hor_start
v2_dir = ver_end - ver_start





# Calculate the determinant of the matrix formed by the direction vectors
det = np.linalg.det(np.vstack((v1_dir, v2_dir)))

# Check if the vectors are parallel (determinant is 0)
if np.isclose(det, 0):
    # Check if the vectors are collinear
    print("The vectors are parallel or collinear and do not intersect.")
else:
    # Calculate the parameter values for each vector using Cramer's rule
    v1_param = np.linalg.det(np.vstack((ver_start - hor_start, v2_dir))) / det
    v2_param = np.linalg.det(np.vstack((ver_start - hor_start, v1_dir))) / det
    
    
    # Check if the intersection point is within the bounds of both vectors
    if (0 <= v1_param <= 1) and (0 <= v2_param <= 1):
        # Calculate the intersection point using the parameter values
        intersection_point = hor_start + v1_param * v1_dir
        
        print("The intersection point is:", intersection_point)
    else:
        print("The vectors intersect, but the intersection point is not within the bounds of both vectors.")
print(intersection_point)

# Defining the "average pixel width and height"
pixel_size_horizontal = 484/abs(hor_end[0]-hor_start[0])
pixel_size_vertical = 484/abs(ver_end[1]-ver_start[1])

fig, ax = plt.subplots()
for x in range (0,len(redMarks),1):
    print("************************************************")
    tempX = pixel_size_horizontal*(redMarks[x][0]-intersection_point[0])
    tempY = pixel_size_vertical*(-1*(redMarks[x][1]-intersection_point[1]))
    test = hor_end[0]-hor_start[0]
    hypIRL = np.sqrt(tempX**2+tempY**2)
    print(x,"Skudd nummer øvre venstre kant",tempX,"X-Katet", tempY, "Y-katet", hypIRL,"Avstand fra origo til skudd")
    ax.plot([intersection_point[0],redMarks[x][0]], [intersection_point[1], redMarks[x][1]], color='y', linewidth=5)




#Define starting and ending points of axis. Start at left top corner
plt.xlim(0,widthPixels)
plt.ylim(heightPixels,0)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
ax.imshow(img)
ax.plot([hor_start[0], hor_end[0]], [hor_start[1], hor_end[1]], color='red', linewidth=5)
ax.plot([ver_start[0], ver_end[0]], [ver_start[1], ver_end[1]], color='green', linewidth=5)

plt.show()