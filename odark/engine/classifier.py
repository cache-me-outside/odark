from darkflow.net.build import TFNet
import os
import cv2

basedir = os.path.abspath(os.path.dirname(__file__))

class Classifier(object):

	options = {
		"model": os.path.join(basedir, 'model/tiny-yolo-voc.cfg'),
		"load": os.path.join(basedir, 'model/tiny-yolo-voc.weights'),
		"threshold": 0.1
	}

	def __init__(self):
		self.dfnet = TFNet(self.options)

	def get_prediction(self, img):
		return cls.dfnet.return_predict(img)
