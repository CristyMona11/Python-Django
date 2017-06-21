from __future__ import unicode_literals
from ..user_app.models import User
from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Album(models.Model):
    title = models.CharField(max_length=64)
    artist = models.ForeignKey(Artist, related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Song(models.Model):
    title = models.CharField(max_length=64)
    album = models.ForeignKey(Album, related_name='songs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Fan(models.Model):
    artist = models.ForeignKey(Artist, related_name='users')
    user = models.ForeignKey(User, related_name='artists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
