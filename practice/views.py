from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import FillDetailsForm
from django.contrib import messages
import re

# Create your views here.
def fillform(r):
    form = FillDetailsForm()
    if r.method == 'POST':
        email = r.POST['email']
        phone_no = r.POST['phone_no']
        form = FillDetailsForm(r.POST, r.FILES)
        if form.is_valid():
            # if not re.findall(r'^[789]\d{9}$', phone_no):
            #     messages.error(r,"Invalid Number, Please enter valid number")
            #     return redirect('/') 
            # elif not re.findall(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            #     messages.error(r,"Invalid email, Please enter valid email")
            #     return redirect('/')
            # else:
            form.save()
            messages.success(r, 'Your Form has been submitted successfully!')
            return HttpResponseRedirect('/')
    return render(r,'base.html',{'form':form})