from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User

def index(request):
    if 'user_id' in request.session:
        return redirect('belt:home')
    return render(request, 'login/index.html')



def authenticate(request):
    server_email = request.POST['html_email']
    server_password = request.POST['html_password']
    try:
        user = User.objects.get(email=server_email)
        if user.password == server_password:
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
        return redirect('belt:book_home')
    except:
        messages.add_message(request, messages.ERROR, 'EMAIL DOES NOT EXIST!')


    messages.add_message(request, messages.ERROR, 'INVALID LOGIN!')
    return redirect('login:home')



def register(request):
    server_email = request.POST['html_email']
    server_password = request.POST['html_password']
    server_confirm = request.POST['html_confirm']

    if server_confirm == server_password:
        try:
            user = User.objects.create(email=server_email, password=server_password)
            print "--------->", user.id
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            return redirect('belt:home')
        except:
            messages.add_message(request, messages.ERROR, 'EMAIL ALREADY EXISTS!')
            return redirect('login:home')
    else:
        messages.add_message(request, messages.ERROR, 'PASSWORDS DO NOT MATCH!')
        return redirect('login:home')

def logout(request):
    request.session.clear()
    return redirect('login:home')
