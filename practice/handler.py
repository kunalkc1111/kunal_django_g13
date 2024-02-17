import json
import pymysql
import os
from io import StringIO
import boto3 #boto3 library to invoke the Lambda function

access_key_id = 'AKIAYS2NWXSI6WFXEPM6'
secret_access_key = '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'
region = 'ap-south-1'

#function to invoke lambda as soon as user saves it's data to database
def invoke_lambda_function():
    # AWS Lambda configuration
    aws_access_key_id = access_key_id
    aws_secret_access_key = secret_access_key
    aws_region = region

    # Specify the ARN of your Lambda function
    lambda_function_arn = 'arn:aws:lambda:ap-south-1:590184103057:function:databaseToS3'

    # Create a Lambda client
    lambda_client = boto3.client(
        'lambda',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )

    try:
        # Invoke Lambda function
        response = lambda_client.invoke(
            FunctionName=lambda_function_arn,
            InvocationType='Event',  # Use 'RequestResponse' for synchronous invocation
        )

        # Log response (optional)
        print("Lambda Response:", response)

    except Exception as e:
        # Handle exception (log or raise, depending on your requirements)
        print(f"Error invoking Lambda function: {str(e)}")


def invoke_email_lambda_function():
    # AWS Lambda configuration
    aws_access_key_id = access_key_id
    aws_secret_access_key = secret_access_key
    aws_region = region

    # Specify the ARN of your Lambda function
    lambda_function_arn = 'arn:aws:lambda:ap-south-1:590184103057:function:verifyEmailSES'

    # Create a Lambda client
    lambda_client = boto3.client(
        'lambda',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )

    try:
        # Invoke Lambda function
        response = lambda_client.invoke(
            FunctionName=lambda_function_arn,
            InvocationType='Event',  # Use 'RequestResponse' for synchronous invocation
        )

        # Log response (optional)
        print("Lambda Response:", response)

    except Exception as e:
        # Handle exception (log or raise, depending on your requirements)
        print(f"Error invoking Lambda function: {str(e)}")