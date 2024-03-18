import numpy as np
import pytesseract
import cv2

class MiceStatEngine:
    def __init__(self, window):
        self.init_summary()

        self.window = window

    def init_summary(self):
        print("Engine initialized.")

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
