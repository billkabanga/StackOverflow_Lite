from flask import jsonify
from dbcontroller import Dbcontroller
db = Dbcontroller()


class Questions(object):
    def __init__(self,question,usrId):
        self.question = question
        self.usrId = usrId

    def post_question(self):
        query = "INSERT INTO questions(question,usrId) VALUES('{}','{}') RETURNING qnid".format(self.question,self.usrId)
        return db.post_data(query)
 
    @classmethod
    def get_questions(self):
        query = "SELECT * FROM questions"
        questions = db.get_all_data(query)
        results = []
        for question in questions:
            qns = {}
            qns['qnid'] = question[0]
            qns['question'] = question[1]
            qns['usrId'] = question[2]
        
            results.append(qns)
        return results

        


