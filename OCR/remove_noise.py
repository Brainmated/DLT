import cv2
from PIL import Image
from matplotlib import pyplot as plt
import pytesseract
import numpy as np

def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return(image)

no_noise = noise_removal(im_bw)
cv2.imwrite("test/no_noisetest.jpg", no_noise)
