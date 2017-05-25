from flask import Flask, render_template, Response
from camera import ExternalCamera
from config import config
import os

app = Flask(__name__)
config_level = os.getenv('FLASK_CONFIGURATION', 'default')
app.config.from_object(config[config_level])

@app.route('/')
def index():
    """Dashboard"""
    return render_template('index.html')

@app.route('/camera_stream')
def camera_stream():
    """Video streaming route. Put this in the src attribute of an img tag."""
    camera = ExternalCamera(app.config['STREAM_URL'])
    return camera.get_stream()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
