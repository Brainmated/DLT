import pytesseract
from PIL import Image

#
image_file = "test/test.jpg"
no_noise = "test/no_noise_test.jpg"

#perform accuracy test in original image and in a no_noise image
#check remove_noise.py to perform a noise removal
img = Image.open(image_file)
clean_img = Image.open(no_noise)

# Specify the language as 'ell' for Greek
ocr_result1 = pytesseract.image_to_string(img, lang='ell')

ocr_result2 = pytesseract.image_to_string(clean_img, lang='ell')

output_file = "test/ocr_result.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(ocr_result)

print("OCR result saved to:", output_file)
