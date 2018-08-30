import re
from flask import Flask,jsonify,request,Blueprint,make_response
from flask_restful import Api,Resource,reqparse
from api.models.usermodel import Users
from flask_jwt_extended import (create_access_token,jwt_required, get_jwt_identity)
from werkzeug.security import safe_str_cmp
from dbcontroller import Dbcontroller
db = Dbcontroller()

user_blue_print = Blueprint('users_bp',__name__,url_prefix='/api/v1')
api = Api(user_blue_print)

class UserRegistration(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username',type=str,required=True,\
        help='name field empty')
        self.reqparse.add_argument('email',type=str,required=True,\
        help='email field empty')
        self.reqparse.add_argument('password',type=str,required=True,\
        help='password field empty')
    def post(self):
        args = self.reqparse.parse_args()
        response = Users(args['username'],args['email'],args['password'])
        if response:
            name = args['username']
            name = name.strip()
            if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.-]+$)",args['email']):
                return make_response(jsonify({'message':'wrong email entry'}),406)
            query = "SELECT * FROM users WHERE email= '{}'".format(args['email'])
            exist = db.get_data(query)
            if exist:
                return make_response(jsonify({'message':'User already exists'}),406)
            if len(args['password'])<8:
                return make_response(jsonify({'message':'Short password. Password should not be less that 8 characters'}),406)
            if response.save():
                return make_response(jsonify({'Welcome': '{}'.format(name) }),201)
        return make_response(jsonify({'Not registered': '{}'.format(name) }),400)



class UserLogin(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username',type=str,required=True,\
        help='name field empty')
        self.reqparse.add_argument('email',type=str,required=False,\
        help='email field empty')
        self.reqparse.add_argument('password',type=str,required=False,\
        help='password field empty')

    def post(self):
        args = self.reqparse.parse_args()
        response = Users(args['username'],args['email'],args['password'])
        user = response.get_specific_user(args['username'])

        if user and safe_str_cmp(user[3], args['password']):
            access_token = create_access_token(identity=user[0], fresh=True)

            return make_response(jsonify({'message': 'Logged in successfully','access_token': access_token}),200)

        return make_response(jsonify({'Not logged in': '{}'.format(args['username']) }),400)

    

api.add_resource(UserRegistration, '/auth/signup')
api.add_resource(UserLogin, '/auth/login')






