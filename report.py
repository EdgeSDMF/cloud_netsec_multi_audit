"""
Report generator and notifier
"""
import smtplib
from email.message import EmailMessage

def send_email_report(findings, to_email="you@example.com"):
    body = "\n".join(findings)
    print(f"Sending report to {to_email}...")  # Simulate sending
    print(body)
    return True
