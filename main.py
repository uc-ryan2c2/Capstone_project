import requests
import json
import csv
import yaml
import PyPDF4


if __name__ == '__main__':
    # create a place for teachers to upload a test documents (Need to decide the type of do
    # creating a pdf file object
    pdfFileObj = open('./example_test/sat-practice-test-1.pdf', 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
    # printing number of pages in pdf file
    print(pdfReader.numPages)
    # creating a page object
    pageObj = pdfReader.getPage(0)
    # extracting text from page
    file_contents = ""
    for i in range(pdfReader.numPages):
        file_contents += pdfReader.getPage(i).extractText()
    # closing the pdf file object
    pdfFileObj.close()

    # Write contents of the PDF file to a new json file
    with open("New_file.txt", "w", encoding='utf-8') as file:
        file.write(file_contents)



    print("Done")