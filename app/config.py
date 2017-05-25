import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''
    STREAM_URL = 'http://airportcam.puc.edu/-wvhttp-01-/getoneshot?camera_id=1&frame_count=no_limit'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}