from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User

def index(request):
    if 'user_id' in request.session:
        return redirect('playlist:home')
    return render(request, 'user_app/index.html')


def authenticate(request):
    email = request.POST['html_email']
    password = request.POST['html_password']
    try:
        user = User.objects.get(email=email)
        if user.password == password:
            request.session['user_id'] = user.id
            request.session['html_email'] = user.email
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('playlist:home')
        else:
            messages.add_message(request, messages.ERROR, 'INVALID PASSWORD!')
            return redirect('user:home')
    except:
        messages.add_message(request, messages.ERROR, 'EMAIL DOES NOT EXIST!')
        return redirect('user:home')

def register(request):
    first_name = request.POST ['first_name']
    last_name = request.POST ['last_name']
    email = request.POST['html_email']
    password = request.POST['html_password']
    confirm = request.POST['html_confirm']
    if len(first_name)<1:
        messages.add_message(request, messages.ERROR, 'FIRST NAME IS EMPTY!')
    if len(last_name)<1:
        messages.add_message(request, messages.ERROR, 'LAST NAME IS EMPTY!')
    if len(email)<1:
        messages.add_message(request, messages.ERROR, 'EMAIL IS EMPTY!')
    if len(password)<1:
        messages.add_message(request, messages.ERROR, 'PASSWORD FIELD IS EMPTY!')
    if confirm == password:
        try:
            user = User.objects.create(email=email, password=password, first_name=first_name, last_name=last_name)
            request.session['user_id'] = user.id
            request.session['html_email'] = user.email
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('playlist:home')
        except:
            messages.add_message(request, messages.ERROR, 'EMAIL ALREADY EXISTS!')
            return redirect('user:home')
    else:
        messages.add_message(request, messages.ERROR, 'PASSWORDS DO NOT MATCH!')
        return redirect('user:home')

def profile(request):
    return render(request, 'user_app/profile.html')

def edit(request):
    if request.method == "POST":
        new_first_name = request.POST['first_name']
        new_last_name = request.POST['last_name']
        new_password = request.POST['html_password']
        confirm_password = request.POST['html_confirm']
        if new_password == confirm_password:
            try:
                user = User.objects.get(id=request.session['user_id'])
                print user.first_name
                user.first_name = new_first_name
                user.last_name = new_last_name
                user.password = new_password
                user.save()
                request.session['html_password'] = user.password
                request.session['last_name'] = user.last_name
                request.session['first_name'] = user.first_name
            except:
                messages.add_message(request, messages.ERROR, 'INVALID LOGIN!')
                return redirect('user:edit')
        else:
            messages.add_message(request, messages.ERROR, 'PASSWORDS DO NOT MATCH!')
            return redirect('user:edit')
    return render(request, 'user_app/edit.html')

def logout(request):
    request.session.clear()
    return redirect('user:home')
