import cv2
from PIL import Image
from matplotlib import pyplot as plt
import pytesseract
import numpy as np


def remove_borders(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntSorted = sorted(contours, key = lambda x:cv2.contourArea(x))
    cnt = cntSorted[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = image[y:y+h, x:x]
    return(crop)

#work with the generated no_noise file to help reduce bordering
no_borders = remove_borders(no_noise)
cv2.imwrite("test/no_borders_test.jpg", no_borders)

color = [255, 255, 255]

top, bottom, left, right = [150]*4

image_with_border = cv2.copyMakeBorder(no_borders, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

cv2.imwrite("test/bordered_test.jpg", image_with_border)

#debugging to find if the processed image has any black borders surrounding image
print("Is image empty?", no_borders is None)

#display shape and debug accordinglt
print("Image shape:", no_borders.shape)
print("Image data type:", no_borders.dtype)
