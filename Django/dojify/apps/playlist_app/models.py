from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User
from ..music_app.models import Song

class Playlist(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Addition(models.Model):
    playlist = models.ForeignKey(Playlist, related_name='songs')
    song = models.ForeignKey(Song, related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Listener(models.Model):
    playlist = models.ForeignKey(Playlist, related_name='users')
    user = models.ForeignKey(User, related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
