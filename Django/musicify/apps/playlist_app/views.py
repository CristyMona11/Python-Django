from django.shortcuts import render, redirect

def index(request):
    return render(request, 'playlist_app/index.html')
