import cv2 as cv



#Path to pictures
path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/litenPX.jpg"
path1 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png"
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"
img = cv.imread(path)


columnPixels = (img.shape[0])
widthPixels =(img.shape[1])
# Blue color in BGR
color = (190, 200, 224)
colorCircle = (0,255,0)
radius = 5
window_name = "Chil"
thickness=1
T = []
T1=[(467),(287)]
#img[110,100] = [0,0,255]
#img[111,100] = [0,0,255]
shotValue = 0
for y in range(columnPixels):
    #print("y", y)
    for x in range(widthPixels):
        #print("x",x)
        if img[y,x,0] == color[0] and img[y,x,1] == color[1] and img[y,x,2] == color[2]:
            T.insert(shotValue,[y,x])
            
            img = cv.circle(img, (x,y), radius, colorCircle, thickness)
            #print(T[shotValue],"Shot",y,x)
            shotValue += 1
            #img[y,x] = [255,255,255]
            
cv.imwrite(savePath,img)
    

for x in range(shotValue):
    print(T[x][0],T[x][1])
print(shotValue)
   
# Displaying the image 
cv.imshow(window_name, img)
cv.waitKey(0)
#print ("Y", T[0][0],"X",T[0][1])
#print(pixval)
#ball = img[T[0][0]:T[shotValue-1][shotValue-1],T[0][1]:T[shotValue-1][shotValue-1]]
#img[273:333, 100:160] = ball



#cv.imshow("Image", img)
#cv.waitKey(0)

#cx = 0
#cy = 0
#center_px = img[cy,cx]
#print(center_px)
