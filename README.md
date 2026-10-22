# AI-Powered AWS DevOps Troubleshooting Assistant 

## Project Overview

An AWS-based proof-of-concept that uses Amazon Bedrock AI to analyze Nginx server logs and provide troubleshooting recommendations.

The project demonstrates cloud monitoring, serverless automation, AWS IAM security, and AI-assisted DevOps troubleshooting.

## Architecture

EC2 (Nginx) → CloudWatch Logs → AWS Lambda → Amazon Bedrock → AI Troubleshooting Response

API Gateway provides an IAM-protected GET `/analyze` endpoint connected to Lambda.

## AWS Services Used

- **Amazon EC2:** Hosts the Ubuntu/Nginx test server.
- **Amazon CloudWatch:** Collects EC2 metrics and Nginx access/error logs.
- **AWS Lambda (Python):** Retrieves recent Nginx logs and sends them for AI analysis.
- **Amazon Bedrock (Nova Lite):** Generates troubleshooting explanations and recommendations.
- **Amazon API Gateway:** Provides an API endpoint connected to Lambda.
- **AWS IAM:** Controls access to AWS services and the API.

## How It Works

1. Nginx generates server access and error logs.
2. CloudWatch Agent forwards logs to CloudWatch.
3. Lambda retrieves recent Nginx access logs.
4. Lambda sends the logs to Amazon Bedrock.
5. Bedrock analyzes the logs and suggests troubleshooting steps.
6. Lambda returns the AI-generated analysis.

## Features

- EC2 infrastructure monitoring
- Centralized Nginx logging
- Serverless log retrieval using Python
- AI-powered log analysis
- IAM-based access control
- Troubleshooting recommendations without automatic server modifications

## Testing

Successfully tested the Lambda function with CloudWatch logs and received AI-generated analysis.

The API Gateway route was configured with IAM authorization. End-to-end API invocation has not yet been verified.

## Project Scope

This is a learning-focused proof-of-concept, not a production monitoring system. It analyzes a limited set of recent Nginx access logs and provides advisory troubleshooting recommendations.

## Cost Management

AWS resources can incur charges. The infrastructure may be shut down after testing to avoid ongoing costs.

## Future Improvements

- Terraform infrastructure provisioning
- Jenkins CI/CD integration
- Nginx error-log analysis
- CloudWatch alarm integration
- Additional API testing and security controls
