from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User

def index(request):
    if 'user_id' in request.session:
        return redirect('quote:home')
    return render(request, 'login/index.html')



def authenticate(request):
    server_email = request.POST['html_email']
    server_password = request.POST['html_password']
    try:
        user = User.objects.get(email=server_email)
        if user.password == server_password:
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
        return redirect('quote:quote_home')
    except:
        messages.add_message(request, messages.ERROR, 'EMAIL DOES NOT EXIST!')


    messages.add_message(request, messages.ERROR, 'INVALID LOGIN!')
    return redirect('login:home')



def register(request):
    server_name = request.POST ['html_name']
    server_email = request.POST['html_email']
    server_password = request.POST['html_password']
    server_confirm = request.POST['html_confirm']
    server_dob = request.POST['dob']

    if len(server_name)<1:
        messages.add_message(request, messages.ERROR, 'NAME IS EMPTY!')
    if len(server_email)<1:
        messages.add_message(request, messages.ERROR, 'EMAIL IS EMPTY!')
    if len(server_password)<1:
        messages.add_message(request, messages.ERROR, 'PASSWORD FIELD IS EMPTY!')
    if len(server_dob)<1:
        messages.add_message(request, messages.ERROR, 'DATE OF BIRTH IS EMPTY!')
    if server_confirm == server_password:
        try:
            user = User.objects.create(email=server_email, password=server_password)
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            return redirect('quote:home')
        except:
            messages.add_message(request, messages.ERROR, 'EMAIL ALREADY EXISTS!')
            return redirect('login:home')
    else:
        messages.add_message(request, messages.ERROR, 'PASSWORDS DO NOT MATCH!')
        return redirect('login:home')

def logout(request):
    request.session.clear()
    return redirect('login:home')
