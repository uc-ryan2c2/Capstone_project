import requests
import json
import os
from googlesearch import search


class CheatChecker:
    def __init__(self, api_token, api_url, header):
        self.url_list = None
        self.answer_list = None
        self.questions = None
        self.selected_quiz_id = None
        self.quiz_ids = None
        self.quizzes = None
        self.selected_course_id = None
        self.course_ids = None
        self.course_list = None
        self.api_token = api_token
        self.api_url = api_url
        self.header = header

    def list_course(self):
        request = requests.get(
            f"{self.api_url}/courses",
            headers=self.header
        )

        # format the request data collected from the API call to json format
        request.json()
        content = request.content.decode('utf-8')
        data = json.loads(content)

        # put course names and id's in a list for later use
        self.course_list = []
        self.course_ids = []
        for course in data:
            self.course_list.append(course['name'])
            self.course_ids.append(course['id'])

    def display_course_selection(self):
        # Temp Gui, this will be refactored when I code to django
        print("Please select a class below")
        n = 1
        for course in self.course_list:
            print(f"{n}. {course}")
            n = n + 1

        user_input = input("> ")

        # this will set the users answer to the index number of the selected item in list
        user_answer = int(user_input) - 1

        # grab the class ID of the selected class based on the index from the above calculation
        self.selected_course_id = self.course_ids[user_answer]

    def list_quizzes(self):
        # list quizzes in a course
        request = requests.get(
            f"{self.api_url}/courses/{self.selected_course_id}/quizzes",
            headers=header
        )
        # format the request data collected from the API call to json format
        request.json()
        content = request.content.decode('utf-8')
        data = json.loads(content)

        # display the quizzes for the course
        # Also will need the quiz ID to be able to list the questions for the quiz
        self.quizzes = []
        self.quiz_ids = []
        for quiz in data:
            self.quizzes.append(quiz['title'])
            self.quiz_ids.append(quiz['id'])

    def display_quizzes(self):
        print("Please choose a quiz below")
        n = 1
        for quiz in self.quizzes:
            print(f"{n}. {quiz}")
            n = n + 1

        user_input = input("> ")

        # # this will set the users answer to the index number of the selected item in list
        user_answer = int(user_input) - 1

        # grab the class ID of the selected class based on the index from the above calculation
        self.selected_quiz_id = self.quiz_ids[user_answer]

    def list_quiz_questions(self):
        url = f"{self.api_url}/courses/{self.selected_course_id}/quizzes/{self.selected_quiz_id}/questions"
        request = requests.get(
            url,
            headers=self.header
        )
        # format the request data collected from the API call to json format
        # The answers can also be grabbed. #TODO do we want to display that information in some sort of way?
        request.json()
        content = request.content.decode('utf-8')
        data = json.loads(content)
        print("done")

        self.questions = []
        self.answer_list = []
        for question in data:
            # grab the question text
            question_text = question['question_text'].split("<em>")[1].split("&")[0]
            self.questions.append(question_text)

            # Grab the answers and put them in a list and add that list to the main list
            question_list = question['answers']
            temp_answer_list = []
            for answer in question_list:
                temp_answer_list.append(answer['text'])

            self.answer_list.append(temp_answer_list)

    def list_urls(self):
        # this will search online for each question in the selected quit and list out URLs for each question
        # append the URLs to a list for later use
        self.url_list = []
        for q in self.questions:
            temp_url_list = []
            for url in search(q, tld="co.in", num=10, stop=10, pause=2):
                temp_url_list.append(url)
            self.url_list.append(temp_url_list)

    # TODO do I need to create a function for the cheat checker score? How will the score be calculated?
    def webscrape(self):
        print("tempt")


if __name__ == '__main__':
    # set up canvas environment
    # api token for canvas
    canvas_api_token = os.environ['canvas_token']

    # set the base api url
    canvas_api_url = "https://canvas.instructure.com/api/v1"

    # create header for api calls to canvas
    header = {
        "Authorization": f"Bearer {canvas_api_token}"
    }

    # start the api calls to canvas
    CC = CheatChecker(canvas_api_token, canvas_api_url, header)
    CC.list_course()
    CC.display_course_selection()
    CC.list_quizzes()
    CC.display_quizzes()
    CC.list_quiz_questions()

    # Start the web scrapping
    CC.list_urls()
