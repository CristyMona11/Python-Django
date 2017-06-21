from __future__ import unicode_literals
from django.db import models
from ..login.models import User

class Quote(models.Model):
    quoted_by=models.CharField(max_length=64)
    message=models.CharField(max_length=255)
    user_log = models.ForeignKey(User, related_name="user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
