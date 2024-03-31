import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
from utils import LoggerFactory

class MiceStatStatistics:
    logger_factory = LoggerFactory()

    def __init__(self):
        self.logger = self.logger_factory.create_logger(self)

        self.logger.info("Statistics initialized.")
