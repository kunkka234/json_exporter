import time
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY


class RunLocalhost():
    def __init__(self, metric_collector, port=7979, gap=1):
        self.metric_collector = metric_collector
        self.port = port
        self.gap = gap

    def start(self):
        REGISTRY.register(self.metric_collector)
        start_http_server(self.port)
        while True:
            time.sleep(self.gap)
