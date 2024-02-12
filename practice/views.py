from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import FillDetailsForm
from django.contrib import messages
import re
import json
import pymysql
import os
from io import StringIO
import boto3 #boto3 library to invoke the Lambda function
from .handler import invoke_lambda_function

# Create your views here.
#function to render home
def home(r):
    return render(r,'practice/home.html')

# client = boto3.client('lambda')
#function to handle form
def fillform(r):
    form = FillDetailsForm()
    if r.method == 'POST':
        form = FillDetailsForm(r.POST, r.FILES)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = r.POST['email']
        phone_no = r.POST['phone_no']
        if form.is_valid():
            #check for email validation
            if not(re.fullmatch(regex, email)):
                messages.error(r,"InValid Email")
                return redirect('/form')
            #check for number validation
            if not phone_no.isdigit() or len(phone_no) > 10 or len(phone_no) < 10:
                messages.error(r,"InValid Number")
                return redirect('/form')
            else:
                form.save()
                messages.success(r, 'Your Form has been submitted successfully!')
                #lambda trigger function to invoke lambda as soon as user saves it's data to database
                invoke_lambda_function()
                return HttpResponseRedirect('/form')
    return render(r,'practice/practice.html',{'form':form})




# #function to invoke lambda as soon as user saves it's data to database
# def invoke_lambda_function():
#     # AWS Lambda configuration
#     aws_access_key_id = 'AKIAYS2NWXSI6WFXEPM6'
#     aws_secret_access_key = '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'
#     aws_region = 'ap-south-1'
#     lambda_function_name = 'databaseToS3'

#     # Create a Lambda client
#     lambda_client = boto3.client(
#         'lambda',
#         aws_access_key_id=aws_access_key_id,
#         aws_secret_access_key=aws_secret_access_key,
#         region_name=aws_region
#     )

#     # Payload to send to Lambda function (if needed)
#     payload = {
#         "key1": "value1",
#         "key2": "value2",
#         "key3": "value3"
#     }

#     try:
#         # Invoke Lambda function
#         response = lambda_client.invoke(
#             FunctionName=lambda_function_name,
#             InvocationType='Event',  # Use 'RequestResponse' for synchronous invocation
#             Payload=json.dumps(payload) if payload else None
#         )

#         # Log response (optional)
#         print("Lambda Response:", response)

#     except Exception as e:
#         # Handle exception (log or raise, depending on your requirements)
#         print(f"Error invoking Lambda function: {str(e)}")