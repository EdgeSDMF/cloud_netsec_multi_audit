# ☁️ Multi-Cloud Security Auditor

Audits cloud platforms (AWS, Azure, GCP) for:
- Public EC2/VMs
- Public S3/Buckets
- Insecure firewall/Security Groups

### ✅ Platforms:
- AWS (via boto3)
- Azure/GCP simulated for structure
- Extendable for real cloud SDKs

### 🚀 Run the audit
```bash
python main.py
```

### 📧 Email Integration
Uses `smtplib` (mocked). Replace `send_email_report` with actual credentials or SMTP service (e.g., SendGrid, SES).

### 🛠️ CI/CD Automation
- Add a cron job or GitHub Actions workflow to run weekly.
