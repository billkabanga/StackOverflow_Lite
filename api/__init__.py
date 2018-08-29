from flask import Flask
from instance.config import DevelopmentConfig
from api.views.userviews import my_blue_print
from flask_jwt_extended import JWTManager

def create_app(DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.config['JWT_SECRET_KEY'] = 'SECRET'
    app.register_blueprint(my_blue_print)
    JWTManager(app)

    return app
