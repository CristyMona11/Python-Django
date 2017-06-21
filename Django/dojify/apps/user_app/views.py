import re
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User, Friend

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    if 'user_id' in request.session:
        return redirect('playlist:home')
    return render(request, 'user_app/index.html')

def register(request):
    if request.method == 'POST':
        server_first = request.POST['html_first_name']
        server_last = request.POST['html_last_name']
        server_email = request.POST['html_email']
        server_password = request.POST['html_password']
        server_confirm = request.POST['html_confirm']

        is_valid=True

        if len(server_first) < 2 or len(server_last)< 2:
            messages.error(request, 'First or last name too short!!!')
            is_valid=False

        if EMAIL_REGEX.search(server_email) is None:
            messages.error(request, 'Invalid Email!')
            is_valid=False

        if (server_confirm != server_password) or len(server_confirm) <5:
            messages.error(request, 'Passwords do not match!')
            is_valid=False

        if is_valid:
            try:
                #where you update and throw info in database
                user = User.objects.create(first_name=server_first, last_name=server_last, email=server_email, password=server_password)
                #set up your session
                request.session['user_id'] = user.id
                request.session['user_name'] = user.first_name + ' ' + user.last_name
                request.session['email'] = user.email
                return redirect('playlist:home')
            except:
                messages.error(request, 'email already exists')
                return redirect('user:home')
        else:
            return redirect('user:home')
    else:
        return redirect('user:home')

def login(request):
    if request.method == 'POST':
        server_email = request.POST['html_email']
        server_password = request.POST['html_password']
        try:
            user = User.objects.get(email = server_email)
            if user.password == server_password:
                request.session['user_id'] = user.id
                request.session['user_name'] = user.first_name + ' ' + user.last_name
                return redirect('playlist:home')
            else:
                messages.error(request, 'Invalid Password')
                return redirect('user:home')
        except:
            messages.error(request, 'Email does not exist!')
            return redirect('user:home')

def profile(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'user_app/profile.html', context)

def edit(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'user_app/edit.html', context)

def update(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    if request.method == 'POST':
        new_first_name = request.POST['html_first_name']
        new_last_name = request.POST['html_last_name']
        new_password = request.POST['html_password']
        new_confirm = request.POST['html_confirm']
        id = request.session['user_id']
        if new_password == new_confirm:
            try:
                user = User.objects.get(id=id)
                user.first_name = new_first_name
                user.last_name = new_last_name
                user.password = new_password
                user.save()
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['password'] = user.password
                request.session['user_name'] = user.first_name + ' ' + user.last_name
                return redirect('user:profile')
            except:
                messages.error(request, 'Invalid Login!')
                return redirect('user:edit')
        else:
            messages.error(request, 'Passwords do NOT match!')
            return redirect('user:edit')
    return redirect('playlist:home', context)

def follower(request):
    context = {
        'not_following': User.objects.exclude(followers__follower_id=request.session['user_id']).exclude(id=request.session['user_id']),
        'following': User.objects.filter(followers__follower_id=request.session['user_id'])
    }
    return render(request, 'user_app/followers.html', context)

def follow(request, follower_id, followee_id):
        friend = Friend.objects.create(follower_id=follower_id, followee_id=followee_id)
        return redirect('user:follower')

def unfollow(request, follower_id, followee_id):
        friend = Friend.objects.filter(follower_id=follower_id, followee_id=followee_id).delete()
        return redirect('user:follower')

def logout(request):
    request.session.clear()
    return redirect('user:home')
