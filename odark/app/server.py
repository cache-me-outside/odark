from flask import render_template, Response, Blueprint, current_app as app
from camera import VideoCamera
from odark.engine.classifier import Classifier

dashboard = Blueprint('dashboard', __name__)
# clf = Classifier()

@dashboard.route('/')
def index():
    """Dashboard"""
    return render_template('index.html')

@dashboard.route('/support')
def support():
    """Support"""
    return render_template('support.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        # predictions = clf.get_prediction(frame)
        # frame_with_rects = clf.draw_predictions(frame, predictions)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + camera.encode_frame(frame) + b'\r\n\r\n')

@dashboard.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera(app.config['STREAM_URL'])),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
