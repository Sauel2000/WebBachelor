import cv2 as cv
import numpy as np

class CalibrationSys:
    #Class variable
    VerticalSearchColor =(0,0,255)
    HorisontalSearchColor = (255,0,0)
    

    def __init__(self):
        print("Calibration constructor created")
        
        
    def displayPicturePixels(self,img):
        self.img.widthPixels = self.img.shape[0]
        CalibrationSys.heightPixels = self.img.shape[1]
        print("Picture width",CalibrationSys.widthPixels,"px.","Picture Height", CalibrationSys.heightPixels,"px.")
        
        
    def getAxisCoords(self, img):
        self.img = img
        pixelHeightLen=0 #IN CM
        pixelWidthLen = 0 #IN CM
        CalibrationSys.widthPixels = self.img.shape[0]
        CalibrationSys.heightPixels = self.img.shape[1]

        horiAxisPixel = 0
        vertAxisPixel = 0
        verticalAxisPoint=[]
        horizontalAxisPoint=[]
        
        for x in range(CalibrationSys.widthPixels):
             for y in range(CalibrationSys.heightPixels):
                if (self.img[x,y,0] == CalibrationSys.VerticalSearchColor[0]  and self.img[x,y,1] == CalibrationSys.VerticalSearchColor[1] and self.img[x,y,2] == CalibrationSys.VerticalSearchColor[2]):
                    verticalAxisPoint.insert(vertAxisPixel,[x,y])
                    vertAxisPixel += 1
                    
                if (self.img[x,y,0] == CalibrationSys.HorisontalSearchColor[0]  and self.img[x,y,1] == CalibrationSys.HorisontalSearchColor[1] and self.img[x,y,2] == CalibrationSys.HorisontalSearchColor[2]):
                    horizontalAxisPoint.insert(horiAxisPixel,[x,y])
                    horiAxisPixel +=1
                    
        pixelVertically= 48.320/(verticalAxisPoint[-1][0]-verticalAxisPoint[0][0]) #Piksel høyde i cm

        pixelHorizontal= 48.20 / (horizontalAxisPoint[-1][1]-horizontalAxisPoint[0][1]) #Piksel bredde i cm
        
        heightLengthIRL = 0
        widthLengthIRL = 0
        
        startVerticalCoord = verticalAxisPoint[0][0]
        startHorizontalCoord = horizontalAxisPoint[0][1]
        endVerticalCoord = verticalAxisPoint[-1][0]
        endHorizontalCoord = horizontalAxisPoint[-1][1]
        print(startVerticalCoord,endVerticalCoord,"Vertical", startHorizontalCoord,endHorizontalCoord)

        for x in range(startVerticalCoord, endVerticalCoord,1):
            heightLengthIRL = heightLengthIRL + pixelVertically
              

        for y in range(startHorizontalCoord, endHorizontalCoord,1):
            widthLengthIRL=widthLengthIRL + pixelHorizontal
        
        return "Pixelwidth is:", pixelHorizontal, "Pixelheight is:",pixelVertically, widthLengthIRL, heightLengthIRL
