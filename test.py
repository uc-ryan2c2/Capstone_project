from PIL import Image
from pytesseract import pytesseract
import os

#testinng

if __name__ == '__main__':
    #Define path to tessaract.exe
    path_to_tesseract = r'./tesseract/tesseract-ocr-w64-setup-v5.2.0.20220712.exe'
    #Define path to image
    path_to_images = r'images/'
    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract
    for root, dirs, file_names in os.walk(path_to_images):
        #Iterate over each file_name in the folder
        for file_name in file_names:
            #Open image with PIL
            img = Image.open(path_to_images + file_name)
            #Extract text from image
            text = pytesseract.image_to_string(img)
            print(text)