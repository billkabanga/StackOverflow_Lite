from flask import jsonify
from dbcontroller import Dbcontroller
db = Dbcontroller()

class Answers(object):
    def __init__(self,answer,qnid,usrid,authid,comment):
        self.answer = answer
        self.qnid = qnid
        self.usrid = usrid
        self.authid = authid
        self.comment = comment


