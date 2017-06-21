from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User

def index(request):
    if 'user_id' in request.session:
        return redirect('wish:home')
    return render(request, 'login/index.html')

def register(request):
    if request.method == 'POST':
        server_name = request.POST['html_name']
        server_username = request.POST['html_username']
        server_password = request.POST['html_password']
        server_confirm = request.POST['html_confirm']
        server_date = request.POST['html_date']

        is_valid=True

        if len(server_name) < 3 or len(server_username)< 3:
            messages.error(request, 'First or last name too short!!!')
            is_valid=False

        if (server_confirm != server_password) or len(server_confirm) <5:
            messages.error(request, 'Passwords do not match!')
            is_valid=False

        if is_valid:
            try:
                user = User.objects.create(name=server_name, username=server_username, password=server_password, hiredate=server_date)
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['user_username'] = user.username
                return redirect('wish:home')
            except:
                messages.error(request, 'user already exists')
                return redirect('login:home')
        else:
            return redirect('login:home')
    else:
        return redirect('login:home')

def login(request):
    if request.method == 'POST':
        server_username = request.POST['html_username']
        server_password = request.POST['html_password']
        try:
            user = User.objects.get(username = server_username)
            if user.password == server_password:
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['user_username'] = user.username
                return redirect('wish:home')
            else:
                messages.error(request, 'Invalid Password')
                return redirect('login:home')
        except:
            messages.error(request, 'User does not exist!')
            return redirect('login:home')

def logout(request):
    request.session.clear()
    return redirect('login:home')
