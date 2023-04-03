from ImagInfoClass import CalibrationSys
import cv2 as cv

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ABCop.jpg"
savePath="C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ll.png"


img = cv.imread(path)
#############################################################
#This part is not needed when Jehad part is finished
img[8,291]=(0,0,255) #Vertikale rød 
img[565,291]=(0,0,255) #Vertikale rød
img[292,5]=(255,0,0)  #Horizontal blå markeringer
img[292,574]=(255,0,0)  #Horizontal blå markeringer
#############################################################

cv.imwrite(savePath,img)
CalibSys = CalibrationSys()

VertAxisCoords = CalibSys.getAxisCoords(img) # VerticalFirstAxisXCoord
HorizontalAxisCoords = CalibSys.getAxisCoords(img) # HorizontalAxisXCord




print(VertAxisCoords)
print(HorizontalAxisCoords)
