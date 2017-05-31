from flask import render_template, Response, Blueprint, current_app as app
from camera import VideoCamera
from ..engine.classifier import Classifier
# TODO: Why in the mother fuck does ^^^ not import Classifier

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
def index():
    """Dashboard"""
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + camera.encode_frame(frame) + b'\r\n\r\n')

@dashboard.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera(app.config['STREAM_URL'])),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
