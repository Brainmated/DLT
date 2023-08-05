import cv2
from PIL import Image
from matplotlib import pyplot as plt
import pytesseract
import numpy as np

#thinner the font of the image
def thin_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return(image)

eroded_image = thin_font(no_noise)
cv2.imwrite("test/eroded_test.jpg", eroded_image)
    

def thick_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return(image)

dilated_image = thick_font(no_noise)
cv2.imwrite("test/dilated_test.jpg", dilated_image)
