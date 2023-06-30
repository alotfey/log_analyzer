"""Alert Events."""
import event_handler
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m%d %H:%M:%S",
)


class AlertEvents:
    def __init__(self):
        self.alert_login_events = []
        self.alert_ip_events = []
        self.alert_ip_list = ["83.149.9.216", "208.115.111.72"]

    def alert_login(self, alert_events):
        """Add alert event to list."""
        for alert_event in alert_events:
            if "login" in alert_event:
                self.alert_events.append(alert_event)
                logging.info("Alert event: %s", alert_event)
        return self.alert_events

    def alert_ips(self, alert_events):
        """Add alert event to list."""
        for ip in self.alert_ip_list:
            if ip in alert_events:
                self.alert_ip_events.append(ip)
                logging.info("Alert event: %s", ip)
        return self.alert_ip_events


log_events = event_handler.EventHandler("apache.log").collect_ips()
alert_events = AlertEvents().alert_ips(log_events)
