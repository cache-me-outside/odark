from time import time
import os

script_dir = os.path.dirname(__file__)

class TestCamera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
        self.frames = [open(os.path.join(script_dir, './mocks/' + f) + '.jpg', 'rb').read() for f in ['mock-1', 'mock-2', 'mock-3']]

    def get_frame(self):
        return self.frames[int(time()) % 3]
