from flask import Flask
from config import config
from server import dashboard
import os

app = Flask(__name__)
config_level = os.getenv('FLASK_CONFIGURATION', 'default')
app.config.from_object(config[config_level])

app.register_blueprint(dashboard)
