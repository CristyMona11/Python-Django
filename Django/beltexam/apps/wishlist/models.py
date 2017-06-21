from __future__ import unicode_literals
from ..login.models import User
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Gifter(models.Model):
    item = models.ForeignKey(Item, related_name='giftee')
    user = models.ForeignKey(User, related_name='gifter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
