import cv2

path = 'C:/Users/senay/OneDrive/Dokumenter/USN - 3/Bachelor oppgave/IMG_Processing_Testing/Skyteskive.jpg'


def read_image(path):
    """
    Reads the input image.
    
    @param path: The image to be read.
    """
    return cv2.imread(path)
    
def show_image(window_name, image):
    """
    Displays an image in a window.

    @param window_name: The name of the window to display the image in.
    @param image: The image to display.
    """
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

def convert_to_gray(image):
    """
    Converts an image to grayscale.

    @param image: The input image.
    @return: The grayscale image.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_threshold(image, threshold_value=127):
    """
    Applies a binary threshold to an image.

    @param image: The input image.
    @param threshold_value: The threshold value.
    @return: The thresholded image.
    """
    _, threshold = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return threshold

def find_contours(image):
    """
    Finds the contours in a binary image.

    @param image: The input image.
    @return: The contours and hierarchy arrays.
    """
    return cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

def draw_contours(image, contours):
    """
    Draws the contours on an image.

    @param image: The input image.
    @param contours: The contours to draw.
    """
    for contour in contours:
        if len(contour) < 5:
            continue

        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(image, [contour], 0, (0, 0, 255), 5)

        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10'] / M['m00'])
            y = int(M['m01'] / M['m00'])

            if len(approx) == 3:
                cv2.putText(image, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            elif len(approx) == 4:
                cv2.putText(image, ' ', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            elif len(approx) == 5:
                cv2.putText(image, 'Pentagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            elif len(approx) == 6:
                cv2.putText(image, ' ', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            else:
                cv2.putText(image, '*', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255), 1)

# displaying the image after drawing contours
def disp_image(image):
    cv2.imshow('CenterPoint', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

read_image(path)