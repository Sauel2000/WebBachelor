import cv2
import numpy as np
import time


start_time = time.time()

PATH = "C:/Users/jehad/Desktop/WebBachelor/Program/samuel_filer/samuel_bilder/skyteSkive.jpg"
PATH2 = "C:/Users/jehad\Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/color_image.jpg"
PATH3 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/skyteskive_ThreeMark.jpg"
PATH4 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/resized_SS_RedMarks.jpg"
PATH5 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/smallRedMarkers.jpg"
PATH6 = "C:/Users/jehad/Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/virkeligObjekt.jpg"
img = cv2.imread(PATH5)

width = img.shape[1]
height = img.shape[0]
dim = (width, height)

wall = False

x_img = 1
y_img = 1 


row = 1

punkter = 0


print(dim)
#resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

while(wall == False):
    x1 = x_img - 1 # -10
    y1 = y_img - 1 # -10

    x2 = x_img
    y2 = y_img
    pixel_center = img[(y_img,x_img)]
    

    
    #if(( pixel_center[0] < 3) and  pixel_center[1] < 7 and (pixel_center[2] > 245 and pixel_center[2] < 256 ) ):
    if( pixel_center[0] < 8 and  pixel_center[1] < 4 and pixel_center[2] < 256 and pixel_center[2] > 245  ):
          punkter += 1
          cv2.rectangle(img, (x1,y1), (x2,y2), (0, 255, 0), -1)
          #print(x1,y1,x2,y2)
          #print(x_img, y_img)
          #print("DONE!")

   
  
    if (x_img == (width - 10)):
        y_img += 1
        x_img = 1
        #print("going to row", row ,"| y position = ", y_img,  "\n\n")
        row += 1

    if (y_img == (height - 10)):
            wall = True
    x_img += 1
    #print("x position: ", x_img)

#print(punkter)
print(dim)
cv2.imshow('detect holes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
print("\n Process finished in:", np.ceil((time.time()- start_time)),"seconds")


