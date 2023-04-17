'''

##General CV2 library

'''
import cv2 as cv
import matplotlib.pyplot as plt


#Path to pictures
path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/linjal.jpg"
path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"
savePath="C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/resized_SS.jpg"
PATH4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/resized_SS_RedMarks.jpg"
PATH5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/Skyteskive_redRectangleMark.jpg"
PATH6 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/fysiskMark.jpg"
PATH7 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/jehad_m.jpg"
PATH8 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/linjal_L.jpg"


'''
Cv2 Section

https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56

'''

## Documentation for a function
# Function that reads the input image
img = cv.imread(PATH8)

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

print(resized_img.shape[0], " | ", resized_width)
print(resized_img.shape[1], " | ", resized_width)

resized_img = cv.circle(resized_img, (24,1800), 1, [0,0,255], -1)

resized_img = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)

imgplot = plt.imshow(resized_img)

plt.xlim(0,resized_width)
plt.ylim(0, resized_height)

#plt.savefig('books_read.png')
plt.show()

