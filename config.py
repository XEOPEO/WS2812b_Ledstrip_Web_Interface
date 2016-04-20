class Config(object):
    # Flask Application Key (optional)
    SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    # Add settings for developement here.
    DEBUG = True

class ProductionConfig(Config):
    # Add settings for production here.
    pass

class TestingConfig(Config):
    TESTING = True
