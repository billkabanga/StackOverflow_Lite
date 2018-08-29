import unittest
import json
from api import create_app
from dbcontroller import Dbcontroller
from instance.config import TestingConfig

class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client
        db = Dbcontroller()
        db.create_tables()

        self.user = {
            "usrid": "1",
            "username": "James Ambayo",
            "email": "tkbill@gmail.com",
            "password": "1234567890"
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
            "username": "Jose Gimenez",
            "email": "jose@gmail.com",
            "password": "1234565"
        }
        self.login = {
            "username": "Kabanga Bill",
            "password": "123456789"
        }
    
    

    



    