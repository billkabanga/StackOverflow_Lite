import unittest
import json
from api import create_app
from dbcontroller import Dbcontroller
from instance.config import TestingConfig

BASE_URL = 'http://127.0.0.1:5000/api/v1'


class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        db = Dbcontroller()
        db.create_tables()

        self.user = {
            "usrid": "1",
            "username": "Jude Inoo",
            "email": "jude@gmail.com",
            "password": "155555555"
        }
        self.question = {
            "qnId": "1",
            "question": "What is an exception?",
            "usrid": "3"
        }
        self.answer = {
            "ansid": "1",
            "answer": "Set of rules",
            "qnid": "1",
            "usrid": "1"
        }
        self.signup = {
            "username": "Ambayo James",
            "email": "ambayo@gmail.com",
            "password": "123456789"
        }
        self.login = {
            "username": "Ambayo James",
            "password": "123456789"
        }

        self.question_add = {
            "question": "What is c++?",
            "usrId": "1"
        }
        self.another_question = {
            "question": "What is python?",
            "usrId": "1"
        }
        self.answer_post = {
            "answer": "pythonic language"
        }
    
    def test_user_signup(self):
        with self.client as client:
            response = client.post(BASE_URL+'/auth/signup',json=dict(self.user))
            self.assertEqual(response.status_code,201)

    def test_user_login(self):
        with self.client as client:
            client.post(BASE_URL+'/auth/signup',json=dict(self.signup))
            response = client.post(BASE_URL+'/auth/login',json=dict(self.login))
            self.assertEqual(response.status_code,200)
    

    def test_post_question(self):
        with self.client as client:
            client.post(BASE_URL+'/auth/signup',json=dict(self.signup))
            response = client.post(BASE_URL+'/auth/login',json=dict(self.login))
            response_data = json.loads(response.data.decode())
            test_response = client.post(BASE_URL+'/questions', headers={'Authorization': 'Bearer '+ response_data['access_token']},\
            json=dict(self.question_add))
            self.assertEqual(test_response.status_code,201)

    def test_get_questions(self):
        with self.client as client:
            client.post(BASE_URL+'/auth/signup',json=dict(self.signup))
            login_response = client.post(BASE_URL+'/auth/login',json=dict(self.login))
            login_data = json.loads(login_response.data.decode())
            client.post(BASE_URL+'/questions', headers={'Authorization': 'Bearer '+ login_data['access_token']},\
            json=dict(self.question_add))

            response = client.get(BASE_URL+'/questions')
            self.assertEqual(response.status_code,200)

    def test_get_specific_question(self):
        with self.client as client:
            client.post(BASE_URL+'/auth/signup',json=dict(self.signup))
            login_response = client.post(BASE_URL+'/auth/login',json=dict(self.login))
            login_data = json.loads(login_response.data.decode())
            client.post(BASE_URL+'/questions', headers={'Authorization': 'Bearer '+ login_data['access_token']},\
            json=dict(self.question_add))
            client.post(BASE_URL+'/questions', headers={'Authorization': 'Bearer '+ login_data['access_token']},\
            json=dict(self.another_question))

            response = client.get(BASE_URL+'/questions/2')
            self.assertEqual(response.status_code,200)
    
    def test_post_answer_to_question(self):
        with self.client as client:
            client.post(BASE_URL+'/auth/signup',json=dict(self.signup))
            login_response = client.post(BASE_URL+'/auth/login',json=dict(self.login))
            login_data = json.loads(login_response.data.decode())
            client.post(BASE_URL+'/questions', headers={'Authorization': 'Bearer '+ login_data['access_token']},\
            json=dict(self.question_add))
            client.post(BASE_URL+'/questions', headers={'Authorization': 'Bearer '+ login_data['access_token']},\
            json=dict(self.another_question))
            client.get(BASE_URL+'/questions/2')
            response = client.post(BASE_URL+'/questions/2/answers',json=dict(self.answer_post))
            self.assertEqual(response.status_code,201)

    def test_delete_question(self):
        with self.client as client:
            client.post(BASE_URL+'/auth/signup',json=dict(self.signup))
            login_response = client.post(BASE_URL+'/auth/login',json=dict(self.login))
            login_data = json.loads(login_response.data.decode())
            client.post(BASE_URL+'/questions', headers={'Authorization': 'Bearer '+ login_data['access_token']},\
            json=dict(self.question_add))
            client.post(BASE_URL+'/questions', headers={'Authorization': 'Bearer '+ login_data['access_token']},\
            json=dict(self.another_question))
            client.get(BASE_URL+'/questions/2')
            response = client.delete(BASE_URL+'/questions/2',headers={'Authorization': 'Bearer '+ login_data['access_token']})
            self.assertEqual(response.status_code,204)





    def tearDown(self):
        db = Dbcontroller()
        db.drop_tables()

            




    



    