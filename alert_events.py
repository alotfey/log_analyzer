"""Alert Events."""
import event_handler

class AlertEvents:
    def __init__(self):
        self.alert_events = []

    def add_alert_event(self, alert_events):
        """Add alert event to list."""
        for alert_event in alert_events:
            if "login" in alert_event:
                self.alert_events.append(alert_event)
        return self.alert_events

log_events = event_handler.EventHandler("apache.log").get_request_url()
alert_events = AlertEvents().add_alert_event(log_events)
print(alert_events)