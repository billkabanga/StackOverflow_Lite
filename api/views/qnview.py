import json
from flask import Flask,request,Blueprint,jsonify,make_response
from flask_restful import Api,Resource,reqparse
from api.models.qnmodel import Questions
from dbcontroller import Dbcontroller
from flask_jwt_extended import (jwt_required, get_jwt_identity)
db = Dbcontroller()

qn_blue_print = Blueprint('qn_bp',__name__,url_prefix='/api/v1')
api = Api(qn_blue_print)

class QuestionsHandler(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('question', type=str,required=True, help='no question to add')
        self.reqparse.add_argument('usrId', type=int,required=False, help='no user Id')
        
    @jwt_required
    def post(self):
        args = self.reqparse.parse_args()
        response = Questions(args['question'],args['usrId'])
        args['usrId']= get_jwt_identity()
        if response:
            query = "SELECT * FROM questions WHERE question= '{}'".format(args['question'])
            exist = db.get_data(query)
            if exist:
                return make_response(jsonify({'message':'Question already exists'}),406)
            query = "INSERT INTO questions(question,usrId) VALUES('{}','{}') RETURNING qnid".format(args['question'],args['usrId'])
            result = db.post_data(query)
            if result:
                return make_response(jsonify({'message': 'question added successfully'}),201)
        return make_response(jsonify({'message': 'question not added'}),404)

    def get(self):
        response = Questions.get_questions() 
        if response:
            return response
        return make_response(jsonify({'message':'No questions have been entered so far'}),404)
            
class SpecificQuestion(Resource):
    def get(self,qnid):
        query = "SELECT qnid,question FROM questions WHERE qnid= '{}'".format(qnid)
        question = db.get_data_by_id(query)
        if question:
            qn = {}
            qn['qnid'] = question[0]
            qn['question'] = question[1]
            
            if qn:
                query = "SELECT answer FROM answers WHERE qnid = '{}'".format(qnid)
                answer = db.get_all_data(query)
                return jsonify({'qn':qn},{'answer':answer})
        return make_response(jsonify({'Message':'Question does not exist'}),404)

    @jwt_required
    def delete(self,qnid):
        query = "SELECT * FROM questions WHERE qnid= '{}'".format(qnid)
        question = db.get_data_by_id(query)
        if question:
            qn = {}
            qn['qnid'] = question[0]
            qn['question'] = question[1]
            qn['usrId'] = question[2]

            if qn:
                query = "DELETE FROM questions WHERE qnid= '{}'".format(qnid)
                db.delete_data(query)
                return make_response(jsonify({'message':'question deleted successfully'}),204)

        

        



api.add_resource(QuestionsHandler, '/questions')
api.add_resource(SpecificQuestion, '/questions/<int:qnid>')



