from darkflow.net.build import TFNet
import os
import cv2

# options = {"model": "/Users/tylerriedal/Code/odark/engine/model/tiny-yolo-voc.cfg",
# "load": "/Users/tylerriedal/Code/odark/engine/model/tiny-yolo-voc.weights", "threshold": 0.1}
# tfnet = TFNet(options)


# imgcv = cv2.imread("/Users/tylerriedal/Code/odark/engine/dog.jpg")
# # import pdb; pdb.set_trace()
# t0 = time.time()
# result = tfnet.return_predict(imgcv)
# t1 = time.time()
# print(result)
# print (t1-t0)

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