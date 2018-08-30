from flask import Flask
from config import DevelopmentConfig
from api.views.userviews import user_blue_print
from api.views.qnview import qn_blue_print
from api.views.answerview import ans_blue_print
from flask_jwt_extended import JWTManager

def create_app(DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.config['JWT_SECRET_KEY'] = 'SECRET'
    app.register_blueprint(user_blue_print)
    app.register_blueprint(qn_blue_print)
    app.register_blueprint(ans_blue_print)
    JWTManager(app)

    return app
