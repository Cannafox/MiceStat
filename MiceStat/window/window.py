import pytesseract
import cv2
from PIL import Image
import numpy as np

GAME_SCREEN_BOUNDARIES = (560,212,1359,812)

# GAME_HEADER_BOUNDARIES = (590, 212, 1359, 235)
GAME_HEADER_BOUNDARIES = (25, 0, 799, 23)
GAME_CHAT_BOUNDARIES = (0, 420, 480, 578)
GAME_LEADERBOARD_BOUNDARIES = (650, 455, 799, 578)

class MiceStatWindow:
    def __init__(self, dummy_image = "test_data/dummy_map_test_01.png"):
        self.frame = ""
        self.header = ""
        self.chat = ""
        self.leaderboard = ""


        self.init_summary()

    def get_header(self):
        return self.header

    def get_chat(self):
        return self.chat

    def get_leaderboard(self):
        return self.leaderboard

    def update_frame(self, frame):
        # GAME_SCREEN_BOUNDARIES = (560,212,1359,812)

        self.frame = frame[212:812, 560:1359]
        # cv2.imshow("test", self.frame)
        # self.frame = frame.crop(GAME_SCREEN_BOUNDARIES)
        # self.frame = self.frame.convert('L')
        self._update_regions()

    def _update_regions(self):
        self.header = self._get_header_region()
        self.header = cv2.resize(self.header, (0,0), fx=2, fy=2)
        # self.chat = self._get_chat_region()
        # self.leaderboard = self._get_leaderboard_region()

    def init_summary(self):
        print("MiceStatWindow initialized.")

    def _get_header_region(self):
        return self.frame[0:23, 25:799]

    def _get_chat_region(self):
        return self.frame.crop(GAME_CHAT_BOUNDARIES)

    def _get_leaderboard_region(self):
        return self.frame.crop(GAME_LEADERBOARD_BOUNDARIES)

    def show_frame(self):
        self.frame.show()

    def show_header(self):
        cv2.imshow("header", self.header)
        cv2.waitKey(0)

    def show_leaderboard(self):
        self.leaderboard.show()

    def show_chat(self):
        self.chat.show()

    def get_screen_data(self):
        header_data = self._get_header_data()
        chat_data = self._get_chat_data()
        leader_data = self._get_leaderboard_data()

        return {"header": header_data,
                "chat": chat_data,
                "leaderboard": leader_data}
