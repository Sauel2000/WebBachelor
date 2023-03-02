import sys # to access the system
import cv2
import os
path = 'C:\\Users\\Samue\\Desktop\\BachelorGit\\WebBachelor\\Program\\samuel_filer\\samuel_bilder\\skyteskive.jpg'


img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
 
while True:
    cv2.imshow("skive", img)
    cv2.waitKey(0)
    sys.exit() # to exit from all the processes
 
cv2.destroyAllWindows() # destroy all windows


'''
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()
'''