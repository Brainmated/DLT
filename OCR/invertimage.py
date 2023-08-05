import cv2
from PIL import Image
from matplotlib import pyplot as plt
import pytesseract
import numpy as np


inverted_image = cv2.bitwise_not(img)
cv2.imwrite("test/inverted_test.jpg", inverted_image)


#------------------GRAYSCALE IMAGE----------  

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_image = grayscale(img)
cv2.imwrite("test/grayedtest.jpg", gray_image)

im_bw = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite("test/bwtest.jpg", im_bw)    
