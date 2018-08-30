import unittest
import json
from api import create_app
from dbcontroller import Dbcontroller
from instance.config import TestingConfig

class BaseTest(unittest.TestCase):

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

    def tearDown(self):
        db = Dbcontroller()
        db.drop_tables()

    