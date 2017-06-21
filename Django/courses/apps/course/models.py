from __future__ import unicode_literals
from django.db import models

class Course(models.Model):
    course_name= models.CharField(max_length=60)
    description = models.CharField(max_length= 255)
    created_at = models.CharField(max_length= 60)
    class Meta:
        db_table="course"
