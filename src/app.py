import json
import boto3
import os

sns = boto3.client('sns')
TOPIC_ARN = os.environ.get('TOPIC_ARN')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    message = f"New object uploaded: {key} to bucket: {bucket}"
    print("Sending message:", message)

    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message,
        Subject="New S3 Upload Notification"
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent')
    }
