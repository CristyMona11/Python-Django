from __future__ import unicode_literals
from django.db import models
from ..login.models import User

class Book(models.Model):
    book_title = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reviews(models.Model):
        review = models.CharField(max_length= 255)
        rating = models.IntegerField()
        book = models.ForeignKey(Book, related_name="reviews")
        user = models.ForeignKey(User, related_name="user")
