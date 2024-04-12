from utils import LoggerFactory
import os
import sys
import cv2
import Xlib.display as display
from Xlib import X, Xatom
from PIL import Image
import numpy as np

from .regions import RegionHeader, RegionChat, RegionLeaderboard, Region, RegionType

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)

GAME_SCREEN_BOUNDARIES = (560, 250, 1359, 855)
WINDOW_NAME = "dummy_map_test_03.png"
REGIONS_TO_WATCH = [RegionType.HEADER, RegionType.LEADERBOARD, RegionType.CHAT]


class MiceStatWindow:
    logger_factory = LoggerFactory()
    d = display.Display()
    root = d.screen().root

    def __init__(self):
        self.window = ""
        self.logger = self.logger_factory.create_logger(self)

        self.regions = {}
        self.regions_data = {}

        self._update_frame()

        for region in REGIONS_TO_WATCH:
            self.regions[region] = Region.create_region(region, self.frame)
            self.regions_data[region] = ""

        self.logger.info("Window initialized.")

    def get_header(self):
        return self.header

    def get_chat(self):
        return self.chat

    def get_leaderboard(self):
        return self.leaderboard

    def _get_window(self):
        # windows = self.root.query_tree().children
        windows = self.root.get_full_property(self.d.intern_atom('_NET_CLIENT_LIST'), 0).value
        for window in windows:
            try:
                window = self.d.create_resource_object('window', window)

                wm_name = window.get_wm_name()

                if WINDOW_NAME in wm_name:
                    self.logger.info(f"Found {wm_name}")
                    return window
            except Exception as ex:
                self.logger.error(ex)

    def capture_window(self, window):
        geom = self.window.get_geometry()
        self.logger.info(geom)
        raw = self.root.get_image(0, 0, geom.width, geom.height, X.ZPixmap, 0xffffffff)
        image = Image.frombytes("RGB", (geom.width, geom.height), raw.data,
                                "raw", "RGBX")
        return np.array(image)

    def update(self):
        self._update_frame()
        self._update_regions()

    def _update_frame(self):
        self.logger.info("Updating frame...")
        self.window = self._get_window()
        self.frame = self.capture_window(self.window)
        y_0, x_0, x_1, y_1 = GAME_SCREEN_BOUNDARIES
        self.frame = self.frame[x_0:y_1, y_0:x_1]

    def _update_regions(self):
        for region in self.regions.keys():
            self.regions[region].update(self.frame)

    def show_frame(self):
        cv2.imshow("frame", self.frame)
        cv2.waitKey(0)

    def show_header(self):
        self.regions[RegionType.HEADER].show()

    def show_leaderboard(self):
        self.regions[RegionType.LEADERBOARD].show()

    def show_chat(self):
        self.regions[RegionType.CHAT].show()

    def get_screen_data(self):
        header_data = self._get_header_data()
        chat_data = self._get_chat_data()
        leader_data = self._get_leaderboard_data()

        return {
            "header": header_data,
            "chat": chat_data,
            "leaderboard": leader_data
        }
