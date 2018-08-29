from api import create_app
from instance.config import DevelopmentConfig
from dbcontroller import Dbcontroller

app = create_app(DevelopmentConfig)


if __name__ == '__main__':
    database_connection = Dbcontroller()
    database_connection.create_tables()
    app.run()
    