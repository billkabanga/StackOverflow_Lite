import psycopg2



class Dbcontroller(object):
    def __init__(self):
        try:
            self.connect = psycopg2.connect(
                "dbname='StackOverflow-lite' user='postgres' host='localhost' password='focus2red' port='5432'"
            )
            self.connect.autocommit = True
            self.cursor = self.connect.cursor()

        except:
            print ('Database not available')

    def get_user(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def create_tables(self):
        user_table = "CREATE TABLE IF NOT EXISTS users(id serial PRIMARY KEY, username varchar(50), email varchar(100), password varchar(20)"
        questions_table = "CREATE TABLE IF NOT EXISTS questions(id serial PRIMARY KEY, question(100), FOREIGN KEY(user) REFERENCES user_table(id)"
        answer_table = "CREATE TABLE IF NOT EXISTS answers(id serial PRIMARY KEY, question(100), FOREIGN KEY(question) REFERENCES questions_table(id), FOREIGN KEY(user) REFERENCES user_table(id)"

        self.cursor.execute(user_table)
        self.cursor.execute(questions_table)
        self.cursor.execute(answer_table)

    def post_data(self,query):
        self.cursor.execute(query)
        re = self.cursor.fetchone()

        return re
    
    def get_all_questions(self):
        self.cursor.execute("SELECT * FROM questions")
        questions = self.cursor.fetchall()
        
        return questions

    def get_all_answers(self):
        self.cursor.execute("SELECT * FROM answers")
        answers = self.cursor.fetchall()

    def get_specific_question(self,id):
        self.cursor.execute("SELECT * FROM questions id = '{}' ".format(id))
        question = self.cursor.fetchone()
        return question

    def get_specific_answer_by_qnId(self, qnId):
        self.cursor.execute("SELECT * FROM answers WHERE qnId = '{}'".format(qnId))


    def update_record(self):
        update_command = "UPDATE users SET   WHERE "
        self.cursor.execute(update_command)

if __name__ == '__main__':
    database_connection = Dbcontroller()


            
