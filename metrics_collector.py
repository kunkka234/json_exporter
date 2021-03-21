import sys
import time
import requests
from requests.auth import HTTPBasicAuth
from prometheus_client.core import GaugeMetricFamily
from json import loads
from jsonpath_ng import parse


class MetricsCollector():
    def __init__(self, config):
        self.config = config.config_json

    def collect(self):
        self.metric = GaugeMetricFamily(
            "json_exporter", "monitoring", labels=["label"])

        for target in self.config["targets"]:
            url = target["endpoint"]

            auth = None
            if "http_client_config" in target.keys():
                if "basic_auth" in target["http_client_config"].keys():
                    username = target["http_client_config"]["basic_auth"]["user_name"]
                    password = target["http_client_config"]["basic_auth"]["password"]
                    auth = HTTPBasicAuth(username, password)

            res = requests.get(url, auth=auth)
            json = loads(res.text)

            for metric in target["metrics"]:
                label = metric["label"]
                values = metric["values"]
                for value in metric["values"]:
                    if "number" in value.keys():
                        self.add_number_metric(label, json, value["number"])
                    elif "boolean" in value.keys():
                        self.add_boolean_metric(label, json, value["boolean"])
                    elif "string" in value.keys():
                        self.add_string_metric(
                            label, json, value["string"]["path"], value["string"]["expected"])
                    else:
                        raise Exception("wrong type of value")

        yield self.metric

    def add_number_metric(self, label, json, path):
        value = parse(path).find(json)[0].value
        self.metric.add_metric(labels=[label], value=value)

    def add_boolean_metric(self, label, json, path):
        boolean_value = parse(path).find(json)[0].value
        self.metric.add_metric(labels=[label], value=boolean_value)

    def add_string_metric(self, label, json, path, expected):
        str_value = parse(path).find(json)[0].value
        value = True if str_value == expected else False
        self.metric.add_metric(labels=[label], value=value)
