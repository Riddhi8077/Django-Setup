from django.shortcuts import render
from .models import School, Classroom, Teacher, Student


def home(request):
    return render(request, 'school/home.html')


def about(request):
    return render(request, 'school/about.html')


def schools(request):
    schools = School.objects.all()
    return render(request, 'school/schools.html', {'schools': schools})


def classrooms(request):
    classrooms = Classroom.objects.all()
    return render(request, 'school/classrooms.html', {'classrooms': classrooms})


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teachers.html', {'teachers': teachers})


def students(request):
    students = Student.objects.all()
    return render(request, 'school/students.html', {'students': students})