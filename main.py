import requests
import json
import csv
from pdf2image import convert_from_path
import poppler

if __name__ == '__main__':


    images = convert_from_path('./pdfs/sat-practice-test-1.pdf',500,poppler_path=r'./poppler-22.04.0/Library/bin')

    for i in range(len(images)):

        # Save pages as images in the pdf
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')