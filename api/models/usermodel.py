import re
from flask import jsonify,make_response
from dbcontroller import Dbcontroller
db = Dbcontroller()


class Users(object):
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
   
    def save(self):
            query= "INSERT INTO users(username,email,password) VALUES('{}','{}','{}') RETURNING usrid".format(self.username,
            self.email,self.password)
            return db.post_data(query)
        
    def get_specific_user(self,username):
        query = "SELECT * FROM users WHERE username = '{}'".format(self.username)
        return db.get_data(query)
        
    

        
