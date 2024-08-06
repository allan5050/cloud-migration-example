# Cloud Migration Example: On-Premises to AWS

## Project Overview

This repository shows an example solution for migrating on-premises workloads to AWS cloud infrastructure. The project addresses a common scenario where a customer seeks to improve reliability and leverage cloud benefits by moving their existing applications to the cloud.

## Scenario

A customer currently runs two primary workloads on-premises:

1. A three-tier application architecture:
   - Frontend: HTML, CSS, JavaScript
   - Backend: Apache Web Server and a Java application
   - Database: MySQL
   This application hosts a dynamic website that accepts user traffic from the internet.

2. A data analytics workload:
   - Runs Apache Hadoop
   - Analyzes large volumes of on-premises data
   - Uses visualization tools for insights

These components run on physical servers in a data center. The current setup is vulnerable to complete system outages during power failures. To address this and gain other cloud benefits, the customer aims to migrate all components to the cloud and using AWS services where appropriate.

## Solution Design

The proposed solution uses AWS services to:
- Decouple the application layers (frontend, backend, and database)
- Host both the web application and data analytics workload in the cloud
- Improve reliability and scalability
- Use managed services where beneficial

Key considerations in the design:
- Using managed services and advocating for code refactoring to use cloud-native technologies
- Migrating the Hadoop-based analytics to Amazon EMR
- Selecting appropriate AWS services for data ingestion, storage, and visualization

## Repository Contents

- `DiagramMaker.py`: Python script for generating the architecture diagram
- `aws_cloud_migration_architecture.png`: The output architecture diagram

## Architecture Diagram

The architecture diagram in this repository visualizes how both the web application and data analytics workloads will be hosted on AWS. It illustrates the AWS services selected and how they interact to create a scalable, reliable, and efficient cloud infrastructure.

To view the diagram:
1. Navigate to the `/` root directory and open the PNG file.

To regenerate the diagram:
1. Ensure Python is installed on your system.
2. Install the required library: `pip install diagrams`
3. Run the script: `python generate_diagram.py`

## Key Components of the Solution
Frontend:
- Route 53: DNS service to route users to the website
- CloudFront: Content Delivery Network for faster global access
- WAF: Web Application Firewall for security

Instead of S3 for static content, we'll use:
- EC2 instances in an Auto Scaling group behind an Application Load Balancer to host the dynamic website

Backend:
- API Gateway: Manages API requests
- Elastic Beanstalk: Hosts the Java application
- EC2 instances: Additional compute resources if needed
- Cognito: Handles user authentication


Database:
- RDS MySQL: Stores relational data
- ElastiCache: Provides caching for improved performance


Data Analytics:
- S3 (Data Lake): Stores large amounts of raw data
- EMR: Runs Hadoop workloads
- Glue: Performs ETL jobs
- Athena: Queries data in S3
- QuickSight: Visualizes data


Security and Management:
- IAM: Manages access permissions
- KMS: Handles encryption keys
- CloudWatch: Monitors resources
- CloudTrail: Logs API activity
- Systems Manager: Manages operational tasks

Direct Connect: Provides a dedicated network connection from on-premises to AWS
