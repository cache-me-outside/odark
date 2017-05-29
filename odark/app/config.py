import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    STREAM_URL = '[prod_url]'

class DevelopmentConfig(Config):
    DEBUG = True
    STREAM_URL = 'http://206.140.121.226/mjpg/video.mjpg'


class TestingConfig(Config):
    TESTING = True


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}