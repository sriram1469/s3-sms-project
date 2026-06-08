import boto3
import os

sns = boto3.client('sns')

def lambda_handler(event, context):
    # Extract file name from S3 event
    file_name = event['Records'][0]['s3']['object']['key']
    message = f"Your file {file_name} has been uploaded successfully."
    
    # Publish SMS using sns.publish
    sns.publish(
        PhoneNumber=os.environ['USER_PHONE'],
        Message=message
    )
    return {"status": "success"}
