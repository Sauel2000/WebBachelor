import cv2
import numpy as np
import time

start_time = time.time()

PATH = "C:/Users/jehad/Desktop/WebBachelor/Program/samuel_filer/samuel_bilder/skyteSkive.jpg"
PATH2 = "C:/Users/jehad\Desktop/WebBachelor/Program/jehad_filer/solutions_try_out/color_image.jpg"
img = cv2.imread(PATH)

width = 1280
height = 720
dim = (width, height)

wall = False

x_img = 10
y_img = 10

x1 = 10
y1 = 0
x2 = 20
y2 = 10
row = 1

resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

while(wall == False):
    pixel_center = resized_img[(y_img,x_img)] # dobbel sjekk om x og y ligger i riktig parameter posisjon
    #cv2.rectangle(resized_img, (x1,y1), (x2,y2), (0, 255, 0), 1)
    print(pixel_center)
    #print("image shape:", resized_img.shape)
    if (x_img == 1270):
        y_img += 10
        x_img = 10
        print("going to row 2 | y position = ", y_img,  "\n\n")

    if (y_img == 710):
            wall = True
    x_img += 10
    print("x position: ", x_img)
    #x1 += 10
    #x2 += 10
    '''
    cv2.imshow('detect holes',resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
print("\n Process finished in:", np.ceil((time.time()- start_time)),"seconds")


