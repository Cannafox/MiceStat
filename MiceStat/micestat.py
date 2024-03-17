from MiceStat.config import MiceStatConfig
from MiceStat.window import MiceStatWindow
from MiceStat.engine import MiceStatEngine

class MiceStat:
    def __init__(self):
        config = MiceStatConfig()
        window = MiceStatWindow()
        engine = MiceStatEngine()

        self.init_summary()

    def init_summary(self):
        print("MiceStat initialized.")
