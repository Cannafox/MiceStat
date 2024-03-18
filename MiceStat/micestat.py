import os
import pytesseract
import cv2
from PIL import Image
from MiceStat.config import MiceStatConfig
from MiceStat.window import MiceStatWindow
from MiceStat.engine import MiceStatEngine
from MiceStat.statistics import MiceStatStatistics

class MiceStat:
    def __init__(self):
        self.config = MiceStatConfig()
        self.statistics = MiceStatStatistics()
        self.window = MiceStatWindow()
        self.engine = MiceStatEngine(self.window)

        self.init_summary()

    def init_summary(self):
        print("MiceStat initialized.")

    def run(self):
        test_data = [os.listdir('test_data')[0]]
        for img in test_data:
            test_path = os.path.join("test_data", img)
            print(test_path)

            # screen_screenshot = Image.open(test_path)
            screen_screenshot = cv2.imread(test_path)
            self.window.update_frame(screen_screenshot)
            # self.window.show_header()
            print(pytesseract.image_to_string(self.window.get_header()))
            # print(pytesseract.image_to_string(self.window.get_chat()))
            # print(pytesseract.image_to_string(self.window.get_leaderboard()))

        # frame = self.window.get_screen_data()
        # self.engine.load_frame(frame)

        # statistics = self.engine.get_frame_statistics()
