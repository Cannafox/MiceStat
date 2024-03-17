import pytesseract
from PIL import Image

class MiceStatWindow:
    def __init__(self):
        self.init_summary()

    def init_summary(self):
        print("MiceStatWindow initialized.")

    def get_screen_data(dummy_screenshot=False):
        if dummy_screenshot:
            return Image.open(dummy_screenshot)
