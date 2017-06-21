from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    context = {
        "emails": Email.objects.all()
    }
    return render(request, 'valid/index.html', context)

def authorize(request):
    context = {
        "emails": Email.objects.all()
    }
    email=request.POST['email']
    if not EMAIL_REGEX.match(email):
        messages.add_message(request,messages.ERROR, 'INVALID EMAIL ADDRESS!!!')
        return redirect('/')
    else:
        Email.objects.create(email=email)
        messages.add_message(request,messages.SUCCESS, 'Thank you for entering a valid email address.')
        return render(request, 'valid/success.html', context)
