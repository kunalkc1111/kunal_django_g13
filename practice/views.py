from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import FillDetailsForm
from django.contrib import messages
import re

# Create your views here.
def home(r):
    return render(r,'practice/home.html')



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
                return redirect('form/')
            #check for number validation
            if not phone_no.isdigit() or len(phone_no) > 10 or len(phone_no) < 10:
                messages.error(r,"InValid Number")
                return redirect('form/')
            else:
                form.save()
                messages.success(r, 'Your Form has been submitted successfully!')
                return HttpResponseRedirect('/form')
    return render(r,'practice/practice.html',{'form':form})