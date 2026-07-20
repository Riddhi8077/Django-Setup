from django.shortcuts import render
from .models import Teacher

def home(request):
    return render(request, 'school/home.html')

def about(request):
    return render(request, 'school/about.html')

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teachers.html', {
        'teachers': teachers
    })