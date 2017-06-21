from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=80)
    alias = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
