from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import *
from django.contrib import messages
from django.db.models import Count

def index(request):
    context = {
        'title': 'The World\'s Greatest Playlist Manager',
        'playlists': Playlist.objects.all().annotate(song_count=Count('songs__playlist'))
    }
    return render(request, 'playlist_manager/index.html', context)

def add_playlist(request):
    playlist_name= request.POST['playlist_name']
    try:
        Playlist.objects.create(name=playlist_name, rating=0)
    except:
        messages.error(request, "Name is duplicate!!! Be original!")
    return redirect('pytunes:index')

def add_song(request, playlist_id):#handles a post and a GET request.
    if request.method == 'POST':#this is what we have to do to get the song becuase it was a GET method to GET the song and POST it.
        addsong = request.POST['song_name']
        try:
            Song.objects.create(title=addsong, playlist_id=playlist_id)#trying to get a song object
        except:
            messages.error(request, 'Same song!')
        route_parameters= {'playlist_id': playlist_id}
        url = reverse('pytunes:addsong', kwargs=route_parameters)
        return redirect(url)
    context= {#This is outside of the if and we need it because we are GETTING information
        'playlist': Playlist.objects.get(id=playlist_id),#this is to show what playlist id we chose when we load the page
        'songs': Song.objects.filter(playlist_id=playlist_id)
    }
    return render(request, 'playlist_manager/songs.html', context)
