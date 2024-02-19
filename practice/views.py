from django.shortcuts import render, HttpResponseRedirect, redirect,HttpResponse
from .forms import FillDetailsForm, SignUpForm
from django.contrib import messages
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json
import pymysql
import os
from io import StringIO
import boto3 #boto3 library to invoke the Lambda function
from .handler import invoke_lambda_function, invoke_email_lambda_function

# Create your views here.
#function to render home
def home(r):
    return render(r,'practice/home.html')

# client = boto3.client('lambda')
#function to handle form
def fillform(r):
    form=FillDetailsForm()
    if r.method == 'POST':
        form = FillDetailsForm(r.POST, r.FILES)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = r.POST['email']
        if form.is_valid():
            #check for email validation
            if not(re.fullmatch(regex, email)):
                messages.error(r,"InValid Email")
                return redirect('/form')
            else:
                form.save()
                messages.success(r, 'Your Form has been submitted successfully!')
                #lambda trigger function to invoke lambda as soon as user saves it's data to database
                invoke_lambda_function()
                return HttpResponseRedirect('/form/')
    return render(r,'practice/practice.html',{'form':form})

def handlesignup(r):
    return render(r,'practice/signup.html')

def handlelogin(r):
    return render(r,'practice/login.html')

def signup(r):
    form = SignUpForm()
    if r.method == 'POST':
        form = SignUpForm(r.POST)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        name = r.POST['name']
        email = r.POST['email']
        username = r.POST['username']
        pass1 = r.POST['pass1']
        pass2 = r.POST['pass2']

        #check for username
        if len(username) > 10:
            messages.error(r,"Username must be under 10 chracter")
            return redirect('/handlesignup')
        if not username.isalnum():
            messages.error(r,"Username must not contain any special character")
            return redirect('/handlesignup')
        #check for email validation
        if not(re.fullmatch(regex, email)):
            messages.error(r,"InValid Email")
            return redirect('/form')
        
        #check for password
        if len(pass1) < 8 or pass1 != pass2:
            messages.error(r,"Password do not match")
            return redirect('/handlesignup')
        if not re.findall('\d', pass1):
            messages.error(r,"The password must contain at least 1 digit, 0-9.")
            return redirect('/handlesignup')
        if not re.findall('[A-Z]', pass1):
            messages.error(r,"The password must contain at least 1 uppercase letter, A-Z.")
            return redirect('/handlesignup')
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', pass1):
            messages.error(r,"The password must contain at least 1 special character: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?")
            return redirect('/handlesignup')
        
        #create user
        user = User.objects.create_user(username, email, pass1)
        user.name = name
        user.save()
        form.save()
        invoke_email_lambda_function()
        messages.success(r,"Your accoount has been successfully created, please verify your email for aws authentication")
        return redirect('/')

    else:
        return HttpResponse('Not Found')

def loginn(r):
    if r.method == 'POST':
        loginUsername = r.POST['loginusername']
        loginpass = r.POST['loginpass']

        user = authenticate(username = loginUsername, password=loginpass)

        if user is not None:
            login(r,user)
            messages.success(r,'You have been successfully logged in.')
            return redirect('/form/')
        else:
            messages.error(r,'Invalid Credentials, Please try again')
            return redirect('/')
    return HttpResponse('404 - Not Found')

def logoutt(r):
    logout(r)
    messages.error(r,'You have been successfully logged out.')
    return redirect('/')