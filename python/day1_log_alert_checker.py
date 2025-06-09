#day1_log_alert_checker.py

"""
This script checks a log entry for suspicious keywords such as 'failed' or 'unauthorized'
and prints an alert if an anomaly is found.
"""

log_entry = "Failed login attempt from 192.168.1.10"

if "failed" in log_entry.lower() or "unauthorized" in log_entry.lower():
    print("ALERT: Suspicious login attempt detected")
else:
    print("No log entry anomalies detected.")
