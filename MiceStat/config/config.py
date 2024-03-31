import os
import sys
import yaml
from types import SimpleNamespace

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
from utils import LoggerFactory


class MiceStatConfig:
    logger_factory = LoggerFactory()
    configs_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

    def __init__(self, config_fn="default"):
        self.logger = self.logger_factory.create_logger(self)

        self.config_fn = f"{config_fn}.yml"
        self.config_path = os.path.join(self.configs_directory, self.config_fn)
        self.config = self.load_config_from_file(self.config_path)

    def load_config_from_file(self, config_path):
        self.logger.info(f"Loading config from {config_path}")

        with open(config_path, 'r') as config_file:
            result = yaml.safe_load(config_file)

        self.logger.info("Config loaded successfully")

        return result
