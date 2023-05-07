import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from ImageInfoClass2 import CalibrationSys
import math


path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/integration.jpg"


img = mpimg.imread(path)
heightPixels = (img.shape[0])   #Width in pic in pixles
widthPixels =(img.shape[1])     #Height in pic in pixles




# Define the starting and ending points of the first vector
hor_start = np.array([1458,6265])
hor_end = np.array([7919, 6030])



# Define the starting and ending points of the second vector
ver_start = np.array([4552,2925])
ver_end = np.array([4738,9338])
intersection_point = []








# Finding direction vector of horizontal and vertical
v1_dir = hor_end - hor_start
v2_dir = ver_end - ver_start



# Defining the "average pixel width and height"
pixel_size_horizontal = 442.5/abs(hor_end[0]-hor_start[0])
pixel_size_vertical = 442.5/abs(ver_end[1]-ver_start[1])

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
#Shoot coordinates
shot1_start = [intersection_point[0],intersection_point[1]]       #origo
shot1_end = [3009,5873]


shot2_start = [intersection_point[0],intersection_point[1]]       #origo
shot2_end = [5095,6250]


shot3_start = [intersection_point[0],intersection_point[1]]       #origo
shot3_end = [4559,7230]


#Defining vector direction for target reference
hor_x_mm_10 = (hor_end[0]-intersection_point[0])/200
hor_y_mm_10 = (hor_start[1]-intersection_point[1])/200
hor_xy_mm_end = np.array([hor_x_mm_10,hor_y_mm_10])


print(hor_x_mm_10,hor_y_mm_10,"deltaY")


#Vertical vector center out
ver_x_mm_10 = (ver_end[0]-intersection_point[0])/200
ver_y_mm_10 = (ver_start[1]-intersection_point[1])/200
ver_xy_mm_end = np.array([ver_x_mm_10,ver_y_mm_10])







mm_IRL_Hor = pixel_size_horizontal * 1348
mm_IRL_Ver = pixel_size_vertical * 1349
hypIRL = np.sqrt(mm_IRL_Hor**2+mm_IRL_Ver**2)
print(mm_IRL_Hor,"X-katet til skudd")
print(mm_IRL_Ver, "Y-katet til skudd")
print(hypIRL,"Avstand til skudd")

U3 = [85]  #7330-1580
V3 = [835.5]   #(-1)*(5530-7065)
fig, ax = plt.subplots()
#Define starting and ending points of axis. Start at left top corner
plt.xlim(0,widthPixels)
plt.ylim(heightPixels,0)
ax.imshow(img)
ax.plot([hor_start[0], hor_end[0]], [hor_start[1], hor_end[1]], color='red', linewidth=1)
ax.plot([ver_start[0], ver_end[0]], [ver_start[1], ver_end[1]], color='green', linewidth=1)
ax.plot([shot1_start[0], shot1_end[0]], [shot1_start[1], shot1_end[1]], color='green', linewidth=1)
ax.plot([shot2_start[0], shot2_end[0]], [shot2_start[1], shot2_end[1]], color='green', linewidth=1)
ax.plot([shot3_start[0], shot3_end[0]], [shot3_start[1], shot3_end[1]], color='green', linewidth=1)
#ax.plot([hor_start[0], hor_xy_mm_end[0]], [hor_start[1], hor_xy_mm_end[0]], color='green', linewidth=1)
plt.quiver(intersection_point[0],intersection_point[1],hor_xy_mm_end[0],hor_xy_mm_end[1],color='g',units ='xy', scale=1,width=10)
plt.quiver(intersection_point[0],intersection_point[1],ver_xy_mm_end[0],ver_xy_mm_end[1],color='red',units ='xy', scale=1,width=10)



plt.show()