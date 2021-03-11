import sys
import time
import json
import requests
from requests.auth import HTTPBasicAuth
# from prometheus_client import start_http_server, Metric, REGISTRY
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY




# ------- get the json ----------------

# proxy setting
proxies = {
    "http": "http://host:port",
    "https": "http://host:port"
}


# ---------------------------------------

class JsonCollector(object):
    def collect(self):
        self.metric = GaugeMetricFamily("test_metric", "monitoring jira index & confluence synchrony-interop", labels=["my_metric"])

        url = "https://example.com/jira/rest/api/2/index/summary"
        self.add_jira_index_metric("LABEL", url, "username", "password")
        url = "https://example.com/confluence/rest/synchrony-interop/synchrony-status"
        self.add_confluence_interop_metric("LABEL", url, "username", "password")

        yield self.metric


    def get_json(self, url, username, password):
        r = requests.get(url, proxies=proxies, auth=HTTPBasicAuth(username, password))
        return json.loads(r.text)

    def add_jira_index_metric(self, label, url, username, password):
        json = self.get_json(url, username, password)
        status = json["issueIndex"]["indexReadable"]
        self.metric.add_metric(labels=[label], value=status)

    def add_confluence_interop_metric(self, label, url, username, password):
        json = self.get_json(url, username, password)
        status = True if json["status"]=="running" else False
        self.metric.add_metric(labels=[label], value=status)

    def test(self):
        self.collect()

REGISTRY.register(JsonCollector())
start_http_server(7979)
while True: time.sleep(1)

# collector = JsonCollector()

# collector.test()
