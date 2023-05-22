import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


from markedAxisShoot2 import markingCenters
import math
import cv2 as cv


path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/108mpSamsungS21ultraTest/4444.jpg"
path2 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/108mpSamsungS21ultraTest/5555.jpg"
path3 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/108mpSamsungS21ultraTest/7777.jpg"
path4 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/108mpSamsungS21ultraTest/8888.jpg"
path5 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/108mpSamsungS21ultraTest/9999.jpg"

path12 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/iphone12mpTest/iphone2.jpg"
path13 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/iphone12mpTest/iphone3.jpg"
path14 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/iphone12mpTest/iphone4.jpg"

path17 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/senayTest/s1.jpg"
path18 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/senayTest/s2.jpg"
path19 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/senayTest/s3.jpg"

#**************************************************************************************
path22 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/sollysSamsungs21/1.jpg"
#**************************************************************************************
path25 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/sollysIphone11/sol1.jpg"
#**************************************************************************************


img = cv.imread(path25) 

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
        tuple = lowest_x
    if tuple[1] < lowest_y[1]:
        lowest_y = tuple
    if tuple[0] > highest_x[0]:
        highest_x = tuple
    if tuple[1] > highest_y[0]:
        highest_y = tuple

# Define the starting and ending points of the first vector
hor_start = np.array([lowest_x[0],lowest_x[1]])
hor_end = np.array([highest_x[0], highest_x[1]])

# Define the starting and ending points of the second vector
ver_start = np.array([lowest_y[0],lowest_y[1]])
ver_end = np.array([highest_y[0],highest_y[1]])
intersection_point = []

# Finding direction vector of horizontal and vertical axis vecktor
horVecDirection = hor_end - hor_start
verVecDiretion = ver_end - ver_start


# Calculate the determinant of the matrix formed by the direction vectors
det = np.linalg.det(np.vstack((horVecDirection, verVecDiretion)))

# Check if the vectors are parallel (determinant is 0)
if np.isclose(det, 0):
    # Check if the vectors are collinear
    print("The vectors are either parallel or collinear and do not intersect.")
else:
    # Calculate the parameter values for each vector using Cramer's rule
    v1_param = np.linalg.det(np.vstack((ver_start - hor_start, verVecDiretion))) / det
    v2_param = np.linalg.det(np.vstack((ver_start - hor_start, horVecDirection))) / det
    
    # Check if the intersection point is within the parameters of both vectors
    if (0 <= v1_param <= 1) and (0 <= v2_param <= 1):
        # Calculate the intersection point using the parameter values
        intersection_point = hor_start + v1_param * horVecDirection
        
        print("Intersection coord is:", intersection_point)
    else:
        print("Vectors intersect, but they are not within the parameters of both vectors")
print(intersection_point)

#Calculate delta x1 for square 1,4 and delta x2 for 2 and 3
pixel_size_horizontal_1_4 = 240/abs(intersection_point[0]-hor_end[0])
pixel_size_horizontal_2_3 = 240/abs(intersection_point[0]-hor_start[0])


#Calculate delta y1 for square 1, 2  and 3,4
pixel_size_vertical_1_2 = 240/abs(intersection_point[1]-ver_start[1])
pixel_size_vertical_3_4 = 240/abs(intersection_point[1]-ver_end[1])


#Create check up variables in case intersection to axis are not 240 mm
diff_h_1_2  = diff_h_3_4=  diff_w_1_4 =  diff_w_2_3= 0

diff_xy_1_4 = diff_xy_2_3 = diff_yx_1_2 = diff_yx_3_4 = 0

#Check if distance between intersection point (Origo) to vertical axis are 240 and if not add and subtract the difference
if (highest_y[1]-intersection_point[1])*pixel_size_vertical_1_2 != 240 or (abs(lowest_y[1]-intersection_point[1])*pixel_size_vertical_1_2 != 240):
    #Positive means center is dragged to right axis with height diff
    diff_h_3_4 = 240-(highest_y[1]-intersection_point[1])*pixel_size_vertical_3_4
    diff_h_1_2 = 240+(lowest_y[1]-intersection_point[1])*pixel_size_vertical_1_2
    print(pixel_size_vertical_1_2*(-1*(redMarks[0][1]-intersection_point[1])),"1,2")
    print(pixel_size_vertical_3_4*(-1*(redMarks[0][1]-intersection_point[1])),"3,4")
    print(pixel_size_vertical_3_4*(-1*(redMarks[-1][1]-intersection_point[1])),"3,4Sisteskudd")
    print(diff_h_1_2,diff_h_3_4)
    

#Check if distance between intersection point (Origo) to horizontal axis are 240 and if not add and subtract the difference
if ((highest_x[0]-intersection_point[0])*pixel_size_horizontal_1_4 != 240 or abs(lowest_x[0]-intersection_point[0])*pixel_size_horizontal_2_3) !=240:
    #Positive means center is dragged down to bottom axis with width diff
    diff_w_1_4 = 240-(highest_x[0]-intersection_point[0])*pixel_size_horizontal_1_4

    diff_w_2_3 = 240+((lowest_x[0]-intersection_point[0]))*pixel_size_horizontal_2_3


fig, ax = plt.subplots()
tempX = tempY = 0
#Automatic test for all shoots
for x in range (0,len(redMarks),1):
    print("************************************************")
    if ((redMarks[x][0]-intersection_point[0]) > 0):
        if(tempX == -240 and tempX > 0.5):
            print("Grader er over 5 og resultatene vil avvike")
        tempX = (pixel_size_horizontal_1_4*(redMarks[x][0]-intersection_point[0])) -abs(diff_w_1_4)
    else:
        tempX = (pixel_size_horizontal_2_3*(redMarks[x][0]-intersection_point[0])) +abs(diff_w_2_3)
    if ((redMarks[x][1]-intersection_point[1]) > 0):
        tempY = (pixel_size_vertical_3_4*(-1*(redMarks[x][1]-intersection_point[1]))) -abs(diff_h_1_2)
        if(tempY == -240 and tempX > 0.5):
            print("Grader er over 5 og resultatene vil avvike")
            
    else:
        tempY = (pixel_size_vertical_1_2*(-1*(redMarks[x][1]-intersection_point[1])))+abs(diff_h_3_4)
        if(tempY == 240 and tempX < -0.5):
            print("Grader er over 5 og resultatene vil avvike")
    
    print(x,tempX,"X",tempY, "Y")
    ax.plot([intersection_point[0],redMarks[x][0]], [intersection_point[1], redMarks[x][1]], color='g', linewidth=5)

#Define starting and ending points of axis. Start at left top corner
plt.xlim(0,widthPixels)
plt.ylim(heightPixels,0)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
ax.imshow(img)

plt.show()