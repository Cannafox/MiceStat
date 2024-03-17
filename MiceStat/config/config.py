import os
import yaml
from types import SimpleNamespace

def get_config_from_file(config_path):
    with open(config_path, 'r') as config_file:
        result = yaml.safe_load(config_file)

    return result

class MiceStatConfig:
    configs_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

    def __init__(self, config_fn="default", debug=False):
        config_fn = f"{config_fn}.yml"
        config_path = os.path.join(self.configs_directory, config_fn)
        self.config = get_config_from_file(config_path)

        self.debug = debug
        self.init_summary()

    def init_summary(self):
        msg = []
        msg.append("MiceStatConfig dump")
        for config_name, config_value in self.config.items():
            msg.append(f"| {config_name}={config_value}")
        msg.append("> MiceStatConfig initialized.")

        print('\n'.join(msg))

