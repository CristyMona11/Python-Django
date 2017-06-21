from __future__ import unicode_literals
from django.db import models
from ..login.models import User

class Course(models.Model):
    course_name= models.CharField(max_length=60)
    description = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)

class Enrollments(models.Model):
    course = models.ForeignKey(Course, related_name="enrollments")
    student = models.ForeignKey(User, related_name="user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
