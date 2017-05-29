import cv2

class VideoCamera(object):
    def __init__(self, stream_url):
        self.video = cv2.VideoCapture(stream_url)
        assert (self.video.isOpened()), "Could not open video feed."

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        return frame

    def encode_frame(self, frame):
    	ret, jpeg = cv2.imencode('.jpg', frame)
    	return jpeg.tobytes()
