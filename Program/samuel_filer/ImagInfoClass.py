import cv2 as cv
import math

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#from intersect import intersection
#import numpy as np

class PixelSizeSys:
    #Class variable
    VerticalSearchColor =(0,0,255)
    HorisontalSearchColor = (255,0,0)
    IRLdistVertAxisPoint = 48
    IRLdistHoriAxisPoint = 48

    def __init__(self):
        print("Calibration constructor created")
        
        
    def getAxisCoords(self, img):
        PixelSizeSys.img = img
        pixelHeightLen=0 #IN CM
        pixelWidthLen = 0 #IN CM
        PixelSizeSys.widthPixels = img.shape[0]
        PixelSizeSys.heightPixels = img.shape[1]

        horiAxisPixel = 0
        vertAxisPixel = 0
        verticalAxisPoint=[]
        horizontalAxisPoint=[]
        
        for x in range(PixelSizeSys.widthPixels):
             for y in range(PixelSizeSys.heightPixels):
                if (img[x,y,0] == PixelSizeSys.VerticalSearchColor[0]  and img[x,y,1] == PixelSizeSys.VerticalSearchColor[1] and img[x,y,2] == PixelSizeSys.VerticalSearchColor[2]):
                    verticalAxisPoint.insert(vertAxisPixel,[x,y])
                    vertAxisPixel += 1
                    
                if (img[x,y,0] == PixelSizeSys.HorisontalSearchColor[0]  and img[x,y,1] == PixelSizeSys.HorisontalSearchColor[1] and img[x,y,2] == PixelSizeSys.HorisontalSearchColor[2]):
                    horizontalAxisPoint.insert(horiAxisPixel,[x,y])
                    horiAxisPixel +=1
                    
        pixelVertically= PixelSizeSys.IRLdistVertAxisPoint/(verticalAxisPoint[-1][0]-verticalAxisPoint[0][0]) #Piksel høyde i cm

        pixelHorizontal= PixelSizeSys.IRLdistHoriAxisPoint/ (horizontalAxisPoint[-1][1]-horizontalAxisPoint[0][1]) #Piksel bredde i cm
        
        heightLengthIRL = 0
        widthLengthIRL = 0
        
        startVerticalCoord = verticalAxisPoint[0][0]
        startHorizontalCoord = horizontalAxisPoint[0][1]
        endVerticalCoord = verticalAxisPoint[-1][0]
        endHorizontalCoord = horizontalAxisPoint[-1][1]
        #print(startVerticalCoord,endVerticalCoord,"Vertical", startHorizontalCoord,endHorizontalCoord)

        for x in range(startVerticalCoord, endVerticalCoord,1):
            heightLengthIRL = heightLengthIRL + pixelVertically
              

        for y in range(startHorizontalCoord, endHorizontalCoord,1):
            widthLengthIRL=widthLengthIRL + pixelHorizontal
        #print("PixWidth:", pixelHorizontal,"PixHeight:", pixelVertically,"SumPixWidth",widthLengthIRL,"SumPixHeight",heightLengthIRL)
        pixelDiagonal = math.sqrt((pixelHorizontal**2 + pixelVertically**2))
        pixelInfo = [pixelDiagonal,pixelVertically,pixelHorizontal]
        
        return (pixelHorizontal, pixelVertically, pixelDiagonal)




    def showGraph(self,img):
    #path= "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/AutenC.jpg"

        PixelSizeSys.img = img


        columnPixels = (img.shape[0])   #Bredden i bildet i piksler
        widthPixels =(img.shape[1])     #Høyden i bilde i  piksler

        # Vector origin vertical position 
        X = [289]
        Y = [26]

        XU = [289,26,0,-531]
        #Vector origin horizontal position
        X1 = [14]
        Y1 = [292]
  
        # Directional vector for vertical position
        U = [0]                   # INTERSECTER MED HORISONTAL PÅ 289
        V = [-531]  
        test = [289,26,14,292]
        # Direction vector for horizontal position
        U1 = [550]
        V1 = [-5]

        # Creating plot
        plt.quiver(X, Y, U, V, color='b', units='xy', scale=1)
        plt.quiver(X1, Y1, U1, V1, color='g', units='xy', scale=1)

        plt.title('Single Vector')


        imgplot = plt.imshow(img)
        plt.show()