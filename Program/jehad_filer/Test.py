import cv2
import numpy as np
import time

start_time = time.time()

PATH = "C:/Users/jehad/Desktop/WebBachelor/Program/samuel_filer/samuel_bilder/skyteSkive.jpg"
PATH2 = "C:/Users/jehad\Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/color_image.jpg"
PATH3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/skyteskive_ThreeMark.jpg"
img = cv2.imread(PATH3)

width = 1280
height = 720
dim = (width, height)

wall = False

x_img = 2
y_img = 2


row = 1



resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

while(wall == False):
    x1 = x_img - 2 # -10
    y1 = y_img - 2 # -10

    x2 = x_img
    y2 = y_img
    pixel_center = resized_img[(y_img,x_img)] # dobbel sjekk om x og y ligger i riktig parameter posisjon
    #cv2.rectangle(resized_img, (x1,y1), (x2,y2), (0, 255, 0), 1)
    #print(pixel_center)

    '''
    if(pixel_center[0] < 100):
         x_img += 5
         pixel_center = resized_img[(y_img,x_img)]

         if(pixel_center[0] > 180):
              x_img += 5
              pixel_center = resized_img[(y_img,x_img)]
              if(pixel_center[0] < 100):
                    cv2.rectangle(resized_img, (x1,y2), (x2,y2), (0, 255, 0), 2)
                    print("\n --------------------------------------- \n\n\n STOP DU FANT DEN STOP STOP TOP!! \n\n\n ----------------------------- \n")
                    wall = True
              x_img -= 5
         x_img -= 5
     '''
    
    if(( pixel_center[0] < 10) and  pixel_center[1] < 36 and (pixel_center[2] > 200 and pixel_center[2] < 256 )):
             
          cv2.rectangle(resized_img, (x1,y1), (x2,y2), (0, 255, 0), 1)
          print(x1,y1,x2,y2)
          #print(x_img, y_img)
          #print("DONE!")
          
    '''
    if(pixel_center[0] > 200):
         
         print("done, run :",pixel_center)
         x_img += 10
         pixel_center = resized_img[(y_img,x_img)]
         print(pixel_center)
         wall = True
    '''
    if (x_img == 1270):
        y_img += 2
        x_img = 2
        #print("going to row", row ,"| y position = ", y_img,  "\n\n")
        row += 1



    if (y_img == 710):
            wall = True
    x_img += 2
    #print("x position: ", x_img)
    
cv2.imshow('detect holes',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
print("\n Process finished in:", np.ceil((time.time()- start_time)),"seconds")


