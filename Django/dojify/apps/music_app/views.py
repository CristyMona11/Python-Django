from django.shortcuts import render, redirect
from models import Artist, Album, Song
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'music_app/add_artist.html')

def add_artist(request):
    context = {
        'artists': Artist.objects.all(),
        'albums': Album.objects.all()
    }
    return render(request, 'music_app/add_artist.html', context)


def added_artist(request):
    if request.method == 'POST':
        server_artist = request.POST['artist']
        server_album = request.POST['album']

        is_valid=True

        if len(server_artist) <2 or len(server_album)<2:
            messages.error(request, 'Artist or Album name too short.')
            is_valid = False
        if is_valid:
            try:
                artist = Artist.objects.create(name=server_artist)
                album = Album.objects.create(artist = artist, title=server_album)
                return redirect('music:added_artist')
            except:
                artist = Artist.objects.create(name=server_artist)
                album = Album.objects.create(artist = artist, title=server_album)
                return redirect('music:added_artist')
        else:
            return redirect('music:added_artist')
    else:
        return redirect('music:added_artist')

def added_song(request, album_id):
    if request.method == 'POST':
        server_song = request.POST['add_song']

        is_valid = True

        if len(server_song)<1:
            messages.error(request, 'You forgot a song name!')
            is_valid = False
        if is_valid:
            song = Song.objects.create(title=server_song, album_id=album_id)
            return redirect('music:added_song', album_id=album_id)
    context = {
        'songs': Song.objects.filter(album_id=album_id).order_by('-created_at'),
        'albums': Album.objects.get(id=album_id)
    }
    return render(request, 'music_app/add_song.html', context)
