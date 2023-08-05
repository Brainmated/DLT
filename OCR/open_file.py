import cv2
from PIL import Image
from matplotlib import pyplot as plt
import pytesseract
import numpy as np

''' 
For a pdf it is better to:
    
import PyPDF2

pdf_file = 'test/test.pdf'
with open(pdf_file, 'rb') as f:
    #pdf_reader = PyPDF2.PdfFileReader(f)
    #page = pdf_reader.getPage(0)
    #text = page.extractText()
    print(text)
'''

image_file = "test/test.jpg"


img = cv2.imread(image_file)

cv2.waitKey(0)
cv2.destroyAllWindows()

def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)
    if len(im_data.shape) == 2:
        # If the image is grayscale, add a third dimension
        im_data = im_data[...,np.newaxis]
    height, width, depth = im_data.shape
    
    figsize = width/float(dpi), height/float(dpi)
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    
    if depth == 1:
        # If the image is grayscale, use a grayscale colormap
        ax.imshow(im_data[:,:,0], cmap="gray")
    else:
        ax.imshow(im_data)
    
    ax.axis("off")
