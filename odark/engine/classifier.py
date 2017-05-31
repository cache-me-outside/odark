from darkflow.net.build import TFNet
import os
import cv2

basedir = os.path.abspath(os.path.dirname(__file__))


class Classifier(object):
    options = {
        "model": os.path.join(basedir, 'model/tiny-yolo-voc.cfg'),
        "load": os.path.join(basedir, 'model/tiny-yolo-voc.weights'),
        "threshold": 0.25
    }

    def __init__(self):
        self.dfnet = TFNet(self.options)

    def get_prediction(self, frame):
    	return self.dfnet.return_predict(frame)

    def draw_label(self, frame, prediction):
    	org = (prediction['topleft']['x'] + 5, prediction['topleft']['y'] - 10)
    	label = prediction['label']
    	font_scale = 0.5
    	font = cv2.FONT_HERSHEY_SIMPLEX
    	font_color = (0, 0, 0)
    	font_thickness = 1

    	(w, h), baseline = cv2.getTextSize(label, font, font_scale, font_thickness)
    	top_left = (prediction['topleft']['x'], prediction['topleft']['y'] - (h + 13))
    	bottom_right = (prediction['topleft']['x'] + (w + 10), prediction['topleft']['y'])
    	bg_color = (255, 0, 255)

    	cv2.rectangle(frame, top_left, bottom_right, bg_color, cv2.cv.CV_FILLED)
    	cv2.putText(frame,  label, org, font, font_scale, font_color, font_thickness)

    def draw_bounding_rect(self, frame, prediction):
		top_left = (prediction['topleft']['x'], prediction['topleft']['y'])
		bottom_right = (prediction['bottomright']['x'], prediction['bottomright']['y'])
		color = (255, 0, 255)
		cv2.rectangle(frame, top_left, bottom_right, color, 2)

    def draw_predictions(self, frame, predictions):
    	img = frame
    	for predict in predictions:
    		self.draw_bounding_rect(img, predict)
    		self.draw_label(img, predict)
    	return img
