from django.shortcuts import render, redirect
from .models import Book, Reviews, User
from datetime import datetime as dt

def index(request):
    return render(request, 'login/index.html')

def book_home(request):
    return render(request, 'belt/book_home.html')

def add_book(request):
    return render(request, 'belt/add_book_review.html')

def logout(request):
    request.session.clear()
    return redirect('login:home')    
