
import boto3
import json
from datetime import datetime, timedelta, timezone

logs = boto3.client("logs", region_name="ap-south-1")
bedrock = boto3.client("bedrock-runtime", region_name="ap-south-1")

def lambda_handler(event, context):
    response = logs.filter_log_events(
        logGroupName="/ai-devops/nginx/access",
        startTime=int(
            (datetime.now(timezone.utc) - timedelta(hours=24)).timestamp() * 1000
        ),
        limit=10
    )

    messages = [
        item["message"] for item in response.get("events", [])
    ]

    if not messages:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "No recent Nginx logs found"
            })
        }

    prompt = (
        "You are an AWS DevOps troubleshooting assistant. "
        "Analyze these Nginx access logs. Explain any problems "
        "in simple English and suggest safe troubleshooting steps. "
        "Do not claim a problem exists unless the logs support it. "
        "Do not execute commands.\n\n"
        + "\n".join(messages)
    )

    ai_response = bedrock.converse(
        modelId="amazon.nova-lite-v1:0",
        messages=[
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],
        inferenceConfig={
            "maxTokens": 350,
            "temperature": 0.2
        }
    )

    analysis = ai_response["output"]["message"]["content"][0]["text"]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "logs_analyzed": len(messages),
            "ai_analysis": analysis
        })
    }
