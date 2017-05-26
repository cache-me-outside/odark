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

	dfnet = TFNet(options)
		
	@classmethod
	def _get_detection_json(cls, img):
		return cls.dfnet.return_predict(img)

	@classmethod
	def get_img_prediction(cls, orig_img):
		result = cls._get_detection_json(orig_img)
		print result


if __name__ == "__main__":
	img_path = os.path.join(basedir, 'dog.jpg')
	imgcv = cv2.imread(img_path)
	Classifier.get_img_prediction(imgcv)