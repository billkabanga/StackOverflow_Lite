import psycopg2
import os
from instance.config import TestingConfig




class Dbcontroller(object):
    def __init__(self):
        
        if os.getenv("APP_SETTING") == TestingConfig:
            dbname = "apptest_db"
        else:
            dbname = "StackOverflow-lite"
        try:
            self.connect = psycopg2.connect(
                dbname=dbname ,user='postgres', host='localhost', password='focus2red' ,port='5432'
            )
            self.connect.autocommit = True
            self.cursor = self.connect.cursor()

        except:
            print ('Database not available')

   

    def create_tables(self):
        user_table = "CREATE TABLE IF NOT EXISTS users(usrid serial PRIMARY KEY, username varchar(50),\
         email varchar(100), password varchar(20))"
        questions_table = "CREATE TABLE IF NOT EXISTS questions(qnid serial PRIMARY KEY, question varchar(100),\
         usrId integer, FOREIGN KEY(usrid) REFERENCES users(usrid))"
        answer_table = "CREATE TABLE IF NOT EXISTS answers(ansid serial PRIMARY KEY, answer varchar(100),\
         qnId integer, usrId integer)"

        self.cursor.execute(user_table)
        self.cursor.execute(questions_table)
        self.cursor.execute(answer_table)

    def drop_tables(self):
        drop_user_table = "DROP TABLE users cascade"
        drop_questions_table = "DROP TABLE questions cascade"
        drop_answer_table = "DROP TABLE answers cascade"


        self.cursor.execute(drop_user_table)
        self.cursor.execute(drop_questions_table)
        self.cursor.execute(drop_answer_table)



    def post_data(self,query):
        self.cursor.execute(query)
        return True
    
    def delete_data(self,query):
        self.cursor.execute(query)
        return True


    def get_data(self,query):
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        return data
    
    def get_data_by_id(self,query):
        self.cursor.execute(query)
        data =self.cursor.fetchone()
        return data
    
    def get_all_data(self,query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    


            
