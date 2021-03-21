import yaml


class Config():
    def __init__(self, config_path):
        try:
            with open(config_path, "r") as f:
                self.config_json = yaml.safe_load(f)
        except Exception as e:
            print("unable to open config file")
            raise e
