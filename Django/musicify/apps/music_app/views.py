from django.shortcuts import render, redirect

def index(request):
    return render(request, 'music_app/index.html')
