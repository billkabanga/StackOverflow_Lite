from flask import Flask,request,Blueprint,jsonify,make_response
from flask_restful import Api,Resource,reqparse
from dbcontroller import Dbcontroller
from api.models.answersmodel import Answers
db = Dbcontroller()

ans_blue_print = Blueprint('ans_bp',__name__,url_prefix='/api/v1')
api = Api(ans_blue_print)

class AnswersHandler(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('answer',type=str,required=True, help='no answer provided')
        

    def post(self,qnid):
        query = "SELECT * FROM questions WHERE qnid= '{}'".format(qnid)
        question = db.get_data_by_id(query)
        if question:
            qn = {}
            qn['qnid'] = question[0]
            qn['question'] = question[1]
            qn['usrId'] = question[2]
            
            if qn:
                args = self.reqparse.parse_args()
                response = Answers(args['answer'],qnid,qn['usrId'])
                if response:
                    query = "SELECT * FROM answers WHERE answer= '{}'".format(args['answer'])
                    exist = db.get_data(query)
                    if exist:
                        return make_response(jsonify({'message':'answer already exists'}),406)
                    if len(args['answer']) ==0:
                        return make_response(jsonify({'message': 'Please enter an answer'}),406) 
                    query = "INSERT INTO answers(answer,qnid,usrid) VALUES('{}','{}','{}')".format(args['answer'],qnid,qn['usrId'])
                    result = db.post_data(query)
                    if result:
                        return make_response(jsonify({'message':'Answer has been added'}),201)

api.add_resource(AnswersHandler, '/questions/<int:qnid>/answers')


