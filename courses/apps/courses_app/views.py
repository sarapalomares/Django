from django.shortcuts import render, redirect, HttpResponse
from . import models

# Create your views here.
def index(request):
    getcourses = models.Course.objects.all()
    print getcourses
    context = {
        'courses': getcourses,
    }
    return render(request, "courses_app/index.html", context)

def add(request):
    print request.POST
    course_name = request.POST['name']
    course_description = request.POST['description']
    models.Course.objects.create(name= course_name, description= course_description)
    return redirect('/')

def edit(request, course_id):
    getcourses = models.Course.objects.get(id = course_id)
    context = {
        'id': course_id,
        'course': getcourses,
    }
    return render(request, "courses_app/edit.html", context)

def destroy(request, course_id):
    getcourses = models.Course.objects.get(id = course_id)
    getcourses.delete()
    return redirect('/')
