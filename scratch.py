import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

if __name__ == '__main__':

    # Dependencies
    path_to_tesseract = r'D:\\cheat_checker\\tesseract\\tesseract.exe'

    # loop on PDF's within the
    images = convert_from_path('./pdfs/sat-practice-test-1.pdf',500,poppler_path=r'./poppler-22.04.0/Library/bin')

    # move into the images directory to store the images generated from the PDF
    os.chdir("./images")

    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')

    os.system("..")
    for f in os.listdir("./images"):
        # grab the image out of the image directory

        img = Image.open(f"./images/{f}")

        # get just the image name without file extension
        file_name_split = f.split(".")
        file_name = file_name_split[0]

        # Providing the tesseract executable
        # location to pytesseract library
        pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

        # This function will extract the text from the image
        image_text = pytesseract.image_to_string(img)

        with open(f"./image_to_text/{file_name}.txt", 'w') as file:
            file.write(image_text)

    print("done")
