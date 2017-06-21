from django.shortcuts import render, redirect
from .models import Course
from datetime import datetime as dt


def index(request):
    context = {
        "courses": Course.objects.all(),
    }
    return render(request, 'course/index.html', context)

def submit(request):
    if request.method == "POST":
        course=Course(course_name=request.POST['course_name'], description=request.POST['description'], created_at=(dt.now()).strftime('%m/%d/%Y'))
        course.save()
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'course/index.html', context)

def remove(request, id):
    context = {
        "courses": Course.objects.filter(id=id)
    }
    return render(request, 'course/delete.html', context)


def deleted(request, id):
    Course.objects.filter(id=id).delete()
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'course/index.html', context)

def keep(request):
    return redirect('courses:index')
