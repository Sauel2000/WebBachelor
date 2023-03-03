import cv2

black_dot = "C:/Users/senay/OneDrive/Dokumenter/USN - 3/Bachelor oppgave/IMG_Processing_Testing/blackdot.jpg"
dots_on_board = "C:/Users/senay/OneDrive/Dokumenter/USN - 3/Bachelor oppgave/IMG_Processing_Testing/dots_on_board3.jpg"

#img_50 = cv2.resize(dots_on_board, None, fx = 0.50, fy = 0.50)
#cv2.imshow('Resized image', img_50)

# Loading an image in grayscale
gray = cv2.imread(dots_on_board, 0)

# Converts image to binary image, where pixels are set to 0 or 255, 
# the thresholded image will have white pixels if intensity of the of the pixels is below the threshold 100, 
# and black pixels if intensity of the pixels is above the threshold. 
#th, threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
th, threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)


# Finding the countours around the black pixels, finds border around the the black pixels
cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

# Finds the countour area around the black dot. 
# Using a condition specifying the minimum area which has to be satisfied 
# for the value of the countour area of the black dot to be put into the list, xcnts. 
s1 = 3
s2 = 20
xcnts = []
for cnt in cnts:
    if s1<cv2.contourArea(cnt) < s2:
        xcnts.append(cnt)
        
print("\nDots number: {}". format(len(xcnts)))

cv2.imshow('Last picture', threshed)
cv2.waitKey(0)

# Press + to stop process 
cv2.destroyAllWindows()
