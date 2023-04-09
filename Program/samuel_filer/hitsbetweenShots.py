from ImagInfoClass import *
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
class DistanceBetweenHits:
    #Class variable
    CalibSys = PixelSizeSys()
    PixelSize = CalibSys.getAxisCoords(img)

    VerticalSearchColor =(0,0,255)
    HorisontalSearchColor = (255,0,0)
    #print(VertAxisCoords)
    #print(HorizontalAxisCoords)

    def __init__(self):
        print("Distance calculation constructor called")
        

    def getDistanceBetweenHits(self):
  
        PixelWidth =DistanceBetweenHits.PixelSize[0]
        PixelHeigh =DistanceBetweenHits.PixelSize[1]

        print( PixelHeigh, PixelWidth)
        return  PixelHeigh, PixelWidth