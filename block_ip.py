from telegram_alert import send_telegram_alert
import json
import datetime

def main():
    with open("anomaly_result.json", "r") as f:
        result = json.load(f)

    if result["label"] == "anomaly":
        ip = result["source_ip"]
        score = result["score"]
        timestamp = result.get("timestamp", datetime.datetime.now().isoformat())

        if block_ip(ip):
            log_blocked_ip(ip, score, timestamp)
            send_alert_email(ip)
            send_telegram_alert(ip, score)
