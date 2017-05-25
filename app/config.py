import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    STREAM_URL = '[prod_url]'

class DevelopmentConfig(Config):
    DEBUG = True
    STREAM_URL = 'http://airportcam.puc.edu/-wvhttp-01-/getoneshot?camera_id=1&frame_count=no_limit'


class TestingConfig(Config):
    TESTING = True


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}