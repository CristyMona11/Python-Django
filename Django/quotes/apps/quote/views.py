from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib import messages
from datetime import datetime as dt
from django.db.models import Count

def index(request):
    return render(request, 'login/index.html')

def quote_home(request):
    if 'user_log_id' in request.session:
        context = {
            'quotes': Quote.objects.all(),
            }
        return render(request, 'quote/list.html', context)

def add_quote(request, id):
    if request.method == "POST":
        quote=Quote.objects.create(quoted_by=request.POST['quoted_by'], message=request.POST['message'])
    return redirect('quote:quote_home')

def add_fave(request):
    if request.method =="POST":
        quote=Quote.objects.create(quoted_by=request.POST['quoted_by'], message=request.POST['message'])
        return redirect('quote:quote_home')

def view_user(request):

    return render(request, 'quote/view_user.html')

def logout(request):
    request.session.clear()
    return redirect('login:home')
