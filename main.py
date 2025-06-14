from aws import audit_aws
from azure import audit_azure
from gcp import audit_gcp
from report import send_email_report

if __name__ == "__main__":
    all_findings = audit_aws() + audit_azure() + audit_gcp()
    send_email_report(all_findings)
