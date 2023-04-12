from ImagInfoClass import*
#from hitsbetweenShots import*
import cv2 as cv
import math

path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/ABCop.jpg"
path2 = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/AutenC.jpg"

img = cv.imread(path2)

img[26,289]=(0,0,255) #Vertikale rød 
img[557,289]=(0,0,255) #Vertikale rød
img[292,14]=(255,0,0)  #Horizontal blå markeringer
img[297,564]=(255,0,0)  #Horizontal blå markeringer 

'''
#PATH DEL
#############################################################
#This part is not needed when Jehad part is finished
img[8,291]=(0,0,255) #Vertikale rød 
img[565,291]=(0,0,255) #Vertikale rød
img[292,5]=(255,0,0)  #Horizontal blå markeringer
img[292,574]=(255,0,0)  #Horizontal blå markeringer
#############################################################
'''
HitCalibSys = PixelSizeSys()

pixel = HitCalibSys.getAxisCoords(img)
deltaX = (pixel[0])**2
deltaY = (pixel[1])**2
distance = (deltaY+deltaX)**(1/2)
print(distance)

print(math.atan2(pixel[1],pixel[0]))   
 
print (pixel)
HitCalibSys.showGraph(img)