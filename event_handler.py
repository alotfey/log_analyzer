"""Collect log events from apache log file."""

import os
import re


class EventHandler:
    def __init__(self, path):
        self.path = path

    def collect_ips(self):
        """Collect IP addresses from log file."""
        # regex for IP address
        ip_regex = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        ips = []
        with open(self.path) as f:
            for line in f:
                if ip_regex.search(line) and ip_regex.search(line).group() not in ips:
                    ips.append(ip_regex.search(line).group())
        return ips

    def get_request_url(self):
        """Collect request from log file."""
        # regex for request
        request_regex = re.compile(r"\"(.+?)\"")
        requests = []
        with open(self.path) as f:
            for line in f:
                if request_regex.search(line):
                    request_event = request_regex.search(line).group()
                    request_event = request_event.split()[1]
                    if request_event not in requests:
                        requests.append(request_event)
        return requests
