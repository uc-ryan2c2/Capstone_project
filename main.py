import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import 

class Abstraction:
    def __init__(self, pdf_name):
        self.pdf_name = pdf_name

    def PDFtoImage(self):
        # Create the directory for the images to get saved to
        just_pdf_name_list = self.pdf_name.split(".")
        just_pdf_name = just_pdf_name_list[0]
        pdf_image_dir_name = f"{just_pdf_name}-images"

        # Check if the directory already exist
        images_dir_exist = os.path.exists(f"./images/{pdf_image_dir_name}")

        # Create the directory if it does not exist
        if images_dir_exist == False:
            os.mkdir(f"./images/{pdf_image_dir_name}")
        else:
            print("Directory already exist")

        if os.listdir(f"./images/{pdf_image_dir_name}") == []:
            # Change into the specific directory for the PDF to save the images to
            images = convert_from_path(f"./pdfs/{self.pdf_name}", 500, poppler_path=r'./poppler-22.04.0/Library/bin')

            os.chdir(f"./images/{pdf_image_dir_name}")
            for i in range(len(images)):
                # Save pages as images in the pdf
                images[i].save('page' + str(i) + '.jpg', 'JPEG')
        else:
            print(f"images already generated for {just_pdf_name}")

if __name__ == '__main__':

    # Dependencies
    path_to_tesseract = r'D:\\cheat_checker\\tesseract\\tesseract.exe'

    list_of_test = []
    for pdfs in os.listdir("pdfs"):
        list_of_test.append(pdfs)

    # GUi that will list out the test so the user can select which test he would like to scrape
    print("Please select which test document you would like to target")
    n = 1
    for file in list_of_test:
        print(f"{n}", f"{file}")
        n = n + 1
    print("q. Quit")

    user_input = input("> ")

    if user_input == "q":
        exit()
    else:
        pdf_selected = int(user_input) - 1
        pdf_name = list_of_test[pdf_selected]

        # Start the class that will grab the questions from the test document
        abstraction = Abstraction(pdf_name)
        abstraction.PDFtoImage()

