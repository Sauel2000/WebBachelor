
'''

General CV2 library

'''
import cv2 as cv


#Path to pictures
path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/linjal.jpg"
path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"

'''
Cv2 Section

https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56

'''
img = cv.imread(path1)


#Colors are all in BGR format
SearchColor = (255, 0, 0)
colorCircle = (0,0,255)
CircleMarkingRadius = 10
window_name = "Chil"
thickness=1
shotCoords = []
shotValue = 0
#Check every pixel in each row to match the searching color
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        #@param img[heightPixel coord, rowPixel coord, indexColorPixel], SearchColor[index(B=0,G,1,R,2)]
        if img[y,x,0] == SearchColor[0] and img[y,x,1] == SearchColor[1] and img[y,x,2] == SearchColor[2]:
            #@param index,2D values (y=height, x=width)
            shotCoords.insert(shotValue,[x,y])
            #Marking the shotpixel with circle
            img = cv.circle(img, (x,y), CircleMarkingRadius, colorCircle, thickness)
            shotValue += 1


cv.imwrite(savePath,img)
    
#Pring all shoot coordinates 
for x in range(shotValue):
    print(shotCoords[x])   
print("Number of hits",shotValue)


cv.imshow(window_name, img)
cv.waitKey(0)

