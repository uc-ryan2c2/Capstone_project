# Capstone_project
This is the repo that will hold the code for Senior Design

The goal of this project is to make an anti cheat systetm that will allow teachers to upload and scan a test to see if there are any answers online.
The script will mark where the asnwers where found so teachers can double-check what the script found.
At the end, the test will get a score with how easy it is to "cheat" on.

This is similar to turnitin.com

Things to look into
* google dorks
* Web Crawlers

## Resources
- https://www.reddit.com/r/learnpython/comments/kswa60/google_dork_using_python/    (exploit DB)
- https://www.scrapingbee.com/blog/crawling-python/
- https://www.geeksforgeeks.org/performing-google-search-using-python-code/
- https://www.quickprogrammingtips.com/azure/how-to-upload-files-to-azure-storage-blobs-using-python.html
- https://apitracker.io/a/chegg
- https://apitracker.io/a/quizlet
- https://apitracker.io/a/coursehero
- https://github.com/matmill5/ken-batcher-pp-ocr/blob/master/go_OCR.py


## Phases with development
### phase 1 (main code development)
1a. Turn PDF document into image
1b. Scan Image to grab text off of image
1c. Look at output and see how we can just grab the questions off the image
1d. If output cannot be parsed for questions, create an AI that can  jub grab the questions
1e. Create a function that will be run against each question to start the web scraper
1f. output a list of URLs found for each question that was searched against and web-scrape each URL to see if the question was found
1g. Figure out a way to see if the questioned was answered within the URL (this could be where the teacher uploads the answer document and we match the answers found online to the answer document)
1h. mark where each question was found 
1i. Give the test a score on how easy it is to find the answers online (optional)

### phase 2 (UI development)
2a. Create a button that will allow users to upload a document (PDF)
2b. Create a document display form on the website that will display the document that was uploaded
2c. Create a button that will start the cheat checker
2d. display the content that was found by the webscrapper
2e. All the user to export the findings to a PDF document


