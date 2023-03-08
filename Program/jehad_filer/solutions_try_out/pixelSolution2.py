import cv2
import time

'''
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
'''



while True:

    #_, frame = cap.read()
    #hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #height, width, _, = frame.shape

    img = cv2.imread("Program\samuel_filer\samuel_bilder\frontTom.jpg")
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cx = int(10)
    cy = int(10)


    pixel_pos_detection = hsv_img[cy, cx]
    hue_value = pixel_pos_detection[0]

    color = "undefined"
    if (hue_value < 5 ):
        color = "RED"
    elif (hue_value < 22):
        color = "ORANGE"
    elif (hue_value < 33):
        color = "YELLOW"
    elif (hue_value < 78):
        color = "GREEN"
    elif (hue_value < 131):
        color = "BLUE"
    elif (hue_value < 170):
        color = "VIOLET"
    else:
        color = "RED"

    pixel_center_bgr = img[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.putText(img, color, (10,70), 0, 1.5, (b, g, r), 2)
    
    x_one, y_one = 0, 10
    x_two, y_two = 10, 0
    cv2.rectangle(img, (x_one,y_one),(x_two,y_two),(0,255,0),1)
    
    '''
    startRecMove = True
    while(startRecMove):
            time.sleep(2)
            x_one += 10
            x_two += 10

            if (x_two == 1280):
                startRecMove = False 
    '''
    cv2.imshow("image", img)
    key = cv2.waitKey(1)
    if( key == 27):
        break

cv2.destroyAllWindows()


