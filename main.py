import argparse
from config import Config
from metrics_collector import MetricsCollector
from run_localhost import RunLocalhost


class JsonCollector():
    def __init__(self, args):
        self.config_path = args.config
        self.port = args.port
        self.gap = args.gap

    def load_config_file(self):
        self.config = Config(self.config_path)

    def run_localhost(self):
        run_localhost = RunLocalhost(
            MetricsCollector(self.config), self.port, self.gap)
        run_localhost.start()

    def run(self):
        self.load_config_file()
        self.run_localhost()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", nargs='?',
                        default="./config.yml", const="./config.yml")
    parser.add_argument("-p", "--port", nargs='?',
                        default=7979, const=7979, type=int)
    parser.add_argument("-g", "--gap", nargs='?', default=1, const=1, type=int)
    args = parser.parse_args()

    collector = JsonCollector(args)
    collector.run()
