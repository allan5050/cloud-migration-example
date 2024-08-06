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

## AWS Cloud Migration Architecture Explanation

This section provides a detailed explanation of the AWS Cloud Migration Architecture diagram.

### Overview
The architecture illustrates the modernization of an on-premises three-tier application and data analytics workload using AWS services. It's designed to provide improved scalability, reliability, and security while leveraging managed services to reduce operational overhead.

### Component Breakdown

1. User Access and Content Delivery
   - Amazon Route 53 serves as the DNS service, directing users to the website.
   - Amazon CloudFront acts as a content delivery network, caching content globally for faster access.
   - AWS WAF (Web Application Firewall) is implemented to protect against common web exploits.

2. Web Application Hosting
   - EC2 instances within an Auto Scaling group host the dynamic website.
   - An Application Load Balancer distributes traffic across these instances, ensuring performance and cost-efficiency.

3. Backend Services
   - Amazon API Gateway manages and routes API requests.
   - AWS Elastic Beanstalk hosts the migrated Java application, simplifying deployment and scaling.
   - Additional EC2 instances are available for compute-intensive tasks.

4. Authentication
   - Amazon Cognito handles user authentication, providing secure and scalable user management.

5. Database Tier
   - Amazon RDS for MySQL stores relational data, replacing the on-premises MySQL database.
   - Amazon ElastiCache provides a caching layer, improving read performance for frequently accessed data.

6. Data Analytics
   - Amazon S3 serves as a data lake, storing raw data in a scalable and cost-effective manner.
   - Amazon EMR runs Hadoop workloads, efficiently processing large amounts of data.
   - AWS Glue performs ETL (Extract, Transform, Load) jobs, preparing data for analysis.
   - Amazon Athena allows for running ad-hoc queries directly on S3 data.
   - Amazon QuickSight provides visualization capabilities for creating dashboards and reports.

7. Security and Management
   - AWS Identity and Access Management (IAM) controls access to AWS resources.
   - AWS Key Management Service (KMS) manages encryption keys, ensuring data security.
   - Amazon CloudWatch monitors resources and applications.
   - AWS CloudTrail logs all API activity for auditing and troubleshooting.
   - AWS Systems Manager helps manage EC2 instances and automate operational tasks.

8. Hybrid Connectivity
   - AWS Direct Connect provides a dedicated, private network connection from the on-premises data center to AWS, ensuring high-bandwidth, low-latency access for hybrid cloud scenarios or during the migration process.

### Key Benefits of This Architecture

1. Improved Scalability: Auto Scaling and managed services allow the infrastructure to adapt to changing demands.
2. Enhanced Reliability: Distributed services and AWS's robust infrastructure minimize the risk of system-wide outages.
3. Increased Security: Integrated security services like WAF, IAM, and KMS provide comprehensive protection.
4. Operational Efficiency: Managed services reduce the operational burden, allowing focus on core business logic.
5. Performance Optimization: Global content delivery, caching, and optimized data processing improve overall system performance.
6. Cost Optimization: Pay-as-you-go pricing and the ability to scale resources as needed help manage costs effectively.
7. Analytics Capabilities: Integrated data analytics services provide powerful insights to drive business decisions.

This architecture addresses the initial challenges of the on-premises setup, providing a robust, scalable, and secure cloud-based solution. It leverages AWS services to their full potential, enabling the business to focus on innovation rather than infrastructure management.
