from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    context={
        "users": User.objects.all(),
    }
    return render(request, 'login/index.html', context)

def authorize(request):
    context={
        "users": User.objects.all(),
    }
    is_valid = True
    if len(request.POST['email'])<1:
        messages.add_message(request, messages.ERROR, 'Oops!You forgot your email.')
        is_valid = False
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.add_message(request,messages.ERROR,"Invalid Email Address!")
        is_valid = False
    if len(request.POST['first_name'])<2:
        messages.add_message(request, messages.ERROR, 'Oops!You forgot your first name.')
        is_valid = False
    if str.isalpha(str(request.POST['first_name'])) is False:
        messages.add_message(request, messages.ERROR, 'Please make sure your first name does not contain any numbers.')
        is_valid = False
    if len(request.POST['last_name'])<2:
        messages.add_message(request, messages.ERROR, 'Oops!You forgot your last name.')
        is_valid = False
    if str.isalpha(str(request.POST['last_name'])) is False:
        messages.add_message(request, messages.ERROR, 'Please make sure your last name does not contain any numbers.')
        is_valid = False
    if len(request.POST['password'])<1:
        messages.add_message(request, messages.ERROR, 'Oops!You forgot your password.')
        is_valid = False
    if len(request.POST['password'])<8:
        messages.add_message(request, messages.ERROR, 'Your password must be more than eight characters.')
        is_valid = False
    if request.POST['password'] != request.POST['confirm']:
        messages.add_message(request, messages.ERROR,'Your passwords do not match!!!')
        is_valid = False
        return redirect('login:index')
    elif is_valid:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        messages.add_message(request,messages.SUCCESS, 'Successfully Registered!')
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        request.session['student_id']=user.id
        return redirect('login:success')

def login(request):
    server_email=request.POST['email']
    if len(request.POST['email'])<1:
        messages.add_message(request, messages.ERROR, 'Oops!You forgot your email.')
        is_valid = False
    if len(request.POST['password'])<1:
        messages.add_message(request, messages.ERROR, 'Oops!You forgot your password.')
        is_valid = False
        return redirect('login:index')

    user= User.objects.get(email=server_email)
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), user.password.encode())
    if user.password == pw_hash:
        request.session['student_id']=user.id
        return redirect('login:success')
    else:
        messages.add_message(request, messages.ERROR, 'Invalid login')
        return redirect('login:index')
def success(request):
        context={
            "users": User.objects.all(),
        }
        return render(request, 'login/success.html')

def logout(request):
    request.session.clear()
    return redirect('login:index')        
