from flask import Response, stream_with_context
import requests
import abc

class CameraBase(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def get_stream(self):
		pass

class ExternalCamera(CameraBase):

	def __init__(self, stream_url):
		self.stream_url = stream_url

	@staticmethod
	def _process_stream(content):
		# TOOD: Currently just a pass through. This needs to somehow buffer chunks until an image is captured.
		for chunk in content:
			if chunk:
				yield chunk

	def get_stream(self):
		req = requests.get(self.stream_url, stream=True)
		return Response(stream_with_context(self._process_stream(req.iter_content(chunk_size=256))),
					content_type=req.headers['content-type'])
