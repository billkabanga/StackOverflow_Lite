class Config(object):
    DEBUG = False
    DBNAME = "StackOverflow-lite"


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DBNAME = "apptest_db"
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


