from flask import Flask,request,Blueprint,jsonify,make_response
from flask_restful import Api,Resource,reqparse
from dbcontroller import Dbcontroller
from api.models.answersmodel import Answers
from flask_jwt_extended import (jwt_required, get_jwt_identity)
db = Dbcontroller()

ans_blue_print = Blueprint('ans_bp',__name__,url_prefix='/api/v1')
api = Api(ans_blue_print)

class AnswersHandler(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('answer',type=str,required=True, help='no answer provided')
        self.reqparse.add_argument('comment',type=str,required=False, help='no comment provided')
        
    @jwt_required
    def post(self,qnid):
        authid = get_jwt_identity()
        query = "SELECT * FROM questions WHERE qnid= '{}'".format(qnid)
        question = db.get_data_by_id(query)
        if question:
            qn = {}
            qn['qnid'] = question[0]
            qn['question'] = question[1]
            qn['usrId'] = question[2]
            
            if qn:
                args = self.reqparse.parse_args()
                response = Answers(args['answer'],qnid,qn['usrId'],authid,args['comment'])
                if response:
                    query = "SELECT * FROM answers WHERE answer= '{}'".format(args['answer'])
                    exist = db.get_data(query)
                    if exist:
                        return make_response(jsonify({'message':'answer already exists'}),406)
                    if len(args['answer']) ==0:
                        return make_response(jsonify({'message': 'Please enter an answer'}),406) 
                    query = "INSERT INTO answers(answer,qnid,usrid,authid) VALUES('{}','{}','{}','{}')".format(args['answer'],qnid,qn['usrId'],authid)
                    result = db.post_data(query)
                    if result:
                        return make_response(jsonify({'message':'Answer has been added'}),201)


class AnswersUpdate(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('answer',type=str,required=True, help='no answer provided')
        self.reqparse.add_argument('comment',type=str,required=False, help='no comment provided')

    @jwt_required
    def put(self,qnid,ansid):
        authid = get_jwt_identity()
        query = "SELECT * FROM questions WHERE qnid= '{}'".format(qnid)
        question = db.get_data_by_id(query)
        if question:
            qn = {}
            qn['qnid'] = question[0]
            qn['question'] = question[1]
            qn['usrId'] = question[2]
            
            if qn:
                args = self.reqparse.parse_args()
                response = Answers(args['answer'],qnid,qn['usrId'],authid,args['comment'])
                if response:
                    query = "SELECT * FROM answers WHERE answer= '{}'".format(ansid)
                    exist = db.get_data(query)
                    if exist and authid:
                        try:
                            query = "UPDATE answers SET answer= '{}'".format(args['answer'])
                            result = db.post_data(query)
                            if result:
                                return make_response(jsonify({'message':'Answer has been added'}),201)
                        except:
                            return make_response(jsonify({'message':'Answer not added'}),406)
                    elif exist and qn['usrid']:
                        try:
                            query = "UPDATE comment SET answer= '{}'".format(args['comment']) 
                            result = db.post_data(query)
                            if result:
                                return make_response(jsonify({'message':'comment has been added'}),201)
                        except:
                            return make_response(jsonify({'message':'comment not added'}),406)

                                


api.add_resource(AnswersHandler, '/questions/<int:qnid>/answers')
api.add_resource(AnswersUpdate, '/questions/<int:qnid>/answers/<int:ansid>')


