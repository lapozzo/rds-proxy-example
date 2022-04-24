# Introduction

Simple RDS Proxy example with Terraform

## Requirements
* aws-cli/2.0.56+
* Python/3.7.3+

## Provisioned Components
* VPC and Subnets
* RDS Mysql 8.0.27 (db.t3.micro)
* RDS Proxy, Secrets, Roles and Policies
* Lambda (simple connection test with RDS Proxy)

## Troubleshooting

If you have some problem with RDS Proxy, try to describe the RDS Proxy components and look for the state and reason fields:

```sh
aws rds describe-db-proxy-targets --db-proxy-name rdsproxy
aws rds describe-db-proxies --db-proxy-name rdsproxy
aws rds describe-db-proxy-target-groups --db-proxy-name rdsproxy
```

Verify the CloudWatch /aws/rds/proxy/rdsproxy log group and Proxy metrics for some hints.

Carefully read the 'Quotas and limitations for RDS Proxy', for example: 'all proxies listen on port 3306 for MySQL' event if your MySql listen on another port, that can lead to Time Out if your security group not allow 3306.

More info: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.troubleshooting.html
