import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from ImageInfoClass2 import CalibrationSys
import math


path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/young.jpg"


img = mpimg.imread(path)
heightPixels = (img.shape[0])   #Width in pic in pixles
widthPixels =(img.shape[1])     #Height in pic in pixles

# Define the starting and ending points of the first vector
v1_start = np.array([1922.5, 4143])
v1_end = np.array([7395+1922.5, 4143-113])
# Define the starting and ending points of the second vector
v2_start = np.array([5580,360])
v2_end = np.array([121.5+5580, 7432+360])
intersection_point = []
pixel_size_horizontal = 485/7395
pixel_size_vertical = 485/7432


# Calculate the direction vectors of each vector
v1_dir = v1_end - v1_start
v2_dir = v2_end - v2_start
# Calculate the determinant of the matrix formed by the direction vectors
det = np.linalg.det(np.vstack((v1_dir, v2_dir)))

# Check if the vectors are parallel (determinant is 0)
if np.isclose(det, 0):
    # Check if the vectors are collinear
    if np.isclose(np.cross(v1_dir, v2_dir), 0):
        print("The vectors are collinear but do not intersect.")
    else:
        print("The vectors are parallel and do not intersect.")
else:
    # Calculate the parameter values for each vector using Cramer's rule
    v1_param = np.linalg.det(np.vstack((v2_start - v1_start, v2_dir))) / det
    v2_param = np.linalg.det(np.vstack((v2_start - v1_start, v1_dir))) / det
    
    # Check if the intersection point is within the bounds of both vectors
    if (0 <= v1_param <= 1) and (0 <= v2_param <= 1):
        # Calculate the intersection point using the parameter values
        intersection_point = v1_start + v1_param * v1_dir
        
        print("The intersection point is:", intersection_point)
    else:
        print("The vectors intersect, but the intersection point is not within the bounds of both vectors.")
print(intersection_point)
#Shoot coordinates
v3_start = [intersection_point[0],intersection_point[1]]       #origo
v3_end = [intersection_point[0]+92,intersection_point[1]-861]

mm_IRL_Hor = pixel_size_horizontal * 92
mm_IRL_Ver = pixel_size_vertical * 861
hypIRL = np.sqrt(mm_IRL_Hor**2+mm_IRL_Ver**2)
print(mm_IRL_Hor,mm_IRL_Ver,hypIRL)

U3 = [85]  #7330-1580
V3 = [835.5]   #(-1)*(5530-7065)
fig, ax = plt.subplots()
#Define starting and ending points of axis. Start at left top corner
plt.xlim(0,widthPixels)
plt.ylim(heightPixels,0)
ax.imshow(img)
ax.plot([v1_start[0], v1_end[0]], [v1_start[1], v1_end[1]], color='red', linewidth=1)
ax.plot([v2_start[0], v2_end[0]], [v2_start[1], v2_end[1]], color='green', linewidth=1)
ax.plot([v3_start[0], v3_end[0]], [v3_start[1], v3_end[1]], color='green', linewidth=1)
plt.show()