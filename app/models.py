import json
import uuid
import re
import jwt
from flask import jsonify,make_response
from datetime import datetime, timedelta
from dbcontroller import Dbcontroller
db = Dbcontroller()

class Users(object):
    def __init__(self,username,email,password):
        self.id = uuid.uuid4().int
        self.username = username
        self.email = email
        self.password = password

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

    def input_validate_user(self,username='' ,email='' ,password=''):
        if re.compile('[+)((*&^%$£"!¬))]').match(username):
            return jsonify({'message': 'Please enter a valid username'})

        if not re.match(r'([+)((*&-]+)@([^%$£"!¬))])', email):
            return jsonify({'message': 'Please enter a valid email'})

        if len(password)<8:
            return jsonify({'message':'Short password'})

    def save(self,input_validate_user):
        if input_validate_user(self.username,self.email,self.password):
            query= "INSERT INTO users VALUES('{}','{}','{}','{}')".format(self.id,self.username,
            self.email,self.password)
            return db.post_data(query)
        return False

    def get_user(self,input_validate_user,username):
        if input_validate_user(self.username,self.password):
            query = "SELECT * FROM users WHERE username = '{}'".format(self.username)
            return db.get_user(query)
        return False
    
    @staticmethod
    def token_generator(self, id):
        """method to generate token for user identification"""
        try:
            #setting up payload with expiration time
            payload = {
                'exp': datetime.utcnow()+timedelta(hours=5),
                'iat': datetime.utcnow,
                'usr': id
            }
            #byte token string crested with payload
            jwt_string = jwt.encode(
                payload,
                'secret',
                algorithm='HS256'
            ).decode('UTF-8')
            return jwt_string

        except Exception as e:
            return str(e)

    @staticmethod
    def token_decoder(self,token):
        try:
            payload = jwt.decode(token, 'secret')
            return jsonify({
                'id': payload['usr'],
                'status': 'Success'
            })
        except jwt.ExpiredSignatureError:
            return jsonify({'message':'Epired token. login to get new token'})
        except jwt.InvalidTokenError:
            return jsonify({'message':'Invalid token. register or login again'})
        

    