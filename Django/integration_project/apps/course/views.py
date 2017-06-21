from django.shortcuts import render, redirect, HttpResponse
from .models import Course, User, Enrollments
from datetime import datetime as dt
from django.db.models import Count


def index(request):
    if 'student_id' in request.session:
        context = {

            "courses": Course.objects.all(),
        }
        return render(request, 'course/index.html', context)
    else:
        return redirect('login:index')

def submit(request):
    if request.method == "POST":
        course=Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
    return redirect('courses:index')

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

def login(request):
    return redirect('login:index')

def add(request):
    context = {
        "students": User.objects.all(),
        "courses": Course.objects.all().annotate(student_count=Count('enrollments__student')),
    }
    return render(request, 'course/user.html', context)

def added(request):
    student_id = request.POST['user']
    course_id = request.POST['courses']
    Enrollments.objects.create(student_id= student_id, course_id = course_id)
    return redirect('courses:add')
