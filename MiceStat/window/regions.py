import cv2
from enum import Enum

GAME_HEADER_BOUNDARIES = (25, 0, 799, 23)
GAME_CHAT_BOUNDARIES = (0, 420, 480, 578)
GAME_LEADERBOARD_BOUNDARIES = (650, 455, 799, 578)

class Region:
    @staticmethod
    def create_region(region_type, frame):
        if region_type == RegionType.CHAT:
            return RegionChat(frame)
        elif region_type == RegionType.LEADERBOARD:
            return RegionLeaderboard(frame)
        elif region_type == RegionType.HEADER:
            return RegionHeader(frame)

    def get_region(self, frame, boundaries):
        y_0, x_0, x_1, y_1 = boundaries
        return frame[x_0:y_1, y_0:x_1]

    def show(self):
        cv2.imshow(self.__class__.__name__, self.region)
        cv2.waitKey(0)


class RegionHeader(Region):
    def __init__(self, frame):
        self.boundaries = GAME_HEADER_BOUNDARIES
        self.update(frame)

    def update(self, frame):
        self.region = self.get_region(frame, self.boundaries)


class RegionChat(Region):
    def __init__(self, frame):
        self.boundaries = GAME_CHAT_BOUNDARIES
        self.update(frame)

    def update(self, frame):
        self.region = self.get_region(frame, self.boundaries)


class RegionLeaderboard(Region):
    def __init__(self, frame):
        self.boundaries = GAME_LEADERBOARD_BOUNDARIES
        self.update(frame)

    def update(self, frame):
        self.region = self.get_region(frame, self.boundaries)


class RegionType(Enum):
    HEADER = "HEADER"
    LEADERBOARD = "LEADERBOARD"
    CHAT = "CHAT"
    SCOREBOARD = "SCOREBOARD"
