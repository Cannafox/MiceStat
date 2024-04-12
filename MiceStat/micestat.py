import time
import os
import cv2
from PIL import Image
from MiceStat.config import MiceStatConfig
from MiceStat.window import MiceStatWindow
from MiceStat.engine import MiceStatEngine
from MiceStat.statistics import MiceStatStatistics
from MiceStat.utils import LoggerFactory

class MiceStat:
    logger_factory = LoggerFactory()

    def __init__(self):
        self.logger = self.logger_factory.create_logger(self)

        self.config = MiceStatConfig()
        self.statistics = MiceStatStatistics()
        self.window = MiceStatWindow()
        self.engine = MiceStatEngine(self.window)

        self.logger.info("MiceStat initialized.")

    def run(self):
        self.logger.info("Run loop...")
        self.window.update()
        self.window.show_frame()
        self.window.show_chat()
        self.window.show_header()
        self.window.show_leaderboard()
        # self.window.update_regions()
        time.sleep(3)

        # test_data = os.listdir('test_data')
        # for img in test_data:
            # test_path = os.path.join("test_data", img)
            # print(test_path)

            # screen_screenshot = Image.open(test_path)
            # screen_screenshot = cv2.imread(test_path)
            # self.window.update_frame(screen_screenshot)
            # self.window.show_header()
            # print(pytesseract.image_to_string(self.window.get_header()))
            # print(pytesseract.image_to_string(self.window.get_chat()))
            # print(pytesseract.image_to_string(self.window.get_leaderboard()))

        # frame = self.window.get_screen_data()
        # self.engine.load_frame(frame)

        # statistics = self.engine.get_frame_statistics()
