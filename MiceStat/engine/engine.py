import numpy as np
import pytesseract
import cv2
import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
from utils import LoggerFactory

class MiceStatEngine:
    logger_factory = LoggerFactory()

    def __init__(self, window):
        self.logger = self.logger_factory.create_logger(self)
        self.window = window

        self.logger.info("Engine initialized")

    def load_frame(self, frame):
        self.last_frame = self._crop_to_game_size(frame)

    def get_frame_statistics(self):
        # self.last_frame["whole"].show()
        self.last_frame["header"] = cv2.cvtColor(np.array(self.last_frame["header"]), cv2.COLOR_RGB2BGR)
        self.last_frame["header"] = cv2.cvtColor(self.last_frame["header"], cv2.COLOR_BGR2GRAY)
        cv2.imshow("test", self.last_frame["header"])
        cv2.waitKey(0)
        print(pytesseract.image_to_string(self.last_frame["header"]))
        # print(self.last_frame.getpixel((560,212)))

    def _get_game_boundaries(self, frame):
        pass
