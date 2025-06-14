"""
AWS Auditor
"""
import boto3

def audit_aws():
    findings = []
    ec2 = boto3.client('ec2')
    s3 = boto3.client('s3')

    # EC2 Audit
    for reservation in ec2.describe_instances()['Reservations']:
        for instance in reservation['Instances']:
            if 'PublicIpAddress' in instance:
                findings.append(f"AWS EC2 {instance['InstanceId']} has public IP: {instance['PublicIpAddress']}")

    # S3 Audit
    for bucket in s3.list_buckets()['Buckets']:
        acl = s3.get_bucket_acl(Bucket=bucket['Name'])
        for grant in acl['Grants']:
            if 'AllUsers' in grant['Grantee'].get('URI', ''):
                findings.append(f"AWS S3 {bucket['Name']} is publicly accessible")

    return findings
