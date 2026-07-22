from django.shortcuts import render, redirect
from .models import School, Classroom, Teacher, Student
from .forms import SchoolForm
from django.shortcuts import render, redirect, get_object_or_404

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

def dashboard(request):
    context = {
        "school_count": School.objects.count(),
        "classroom_count": Classroom.objects.count(),
        "teacher_count": Teacher.objects.count(),
        "student_count": Student.objects.count(),
    }

    return render(request, "school/dashboard.html", context)

def school_list(request):
    schools = School.objects.all()

    return render(
        request,
        "school/schools/list.html",
        {"schools": schools}
    )

def school_add(request):

    if request.method == "POST":

        form = SchoolForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("school_list")

    else:
        form = SchoolForm()

    return render(
        request,
        "school/schools/add.html",
        {"form": form}
    )

def school_edit(request, id):

    school = get_object_or_404(School, id=id)

    if request.method == "POST":
        form = SchoolForm(request.POST, instance=school)

        if form.is_valid():
            form.save()
            return redirect("school_list")

    else:
        form = SchoolForm(instance=school)

    return render(
        request,
        "school/schools/edit.html",
        {"form": form}
    )

def school_delete(request, id):

    school = get_object_or_404(School, id=id)

    if request.method == "POST":
        school.delete()
        return redirect("school_list")

    return render(
        request,
        "school/schools/delete.html",
        {"school": school}
    )