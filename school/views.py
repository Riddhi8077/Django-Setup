from django.shortcuts import render, redirect
from .models import School, Classroom, Teacher, Student
from .forms import SchoolForm, ClassroomForm, TeacherForm, StudentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required(login_url="login")
def dashboard(request):
    context = {
        "school_count": School.objects.count(),
        "classroom_count": Classroom.objects.count(),
        "teacher_count": Teacher.objects.count(),
        "student_count": Student.objects.count(),
    }

    return render(request, "school/dashboard.html", context)

@login_required(login_url="login")
def school_list(request):
    schools = School.objects.all()

    return render(
        request,
        "school/schools/list.html",
        {"schools": schools}
    )

@login_required(login_url="login")
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

@login_required(login_url="login")
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

@login_required(login_url="login")
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

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid Username or Password")

    return render(request, "school/login.html")

@login_required(login_url="login")
def classroom_list(request):
    classrooms = Classroom.objects.all()

    return render(
        request,
        "school/classrooms/list.html",
        {"classrooms": classrooms}
    )

@login_required(login_url="login")
def classroom_add(request):

    if request.method == "POST":

        form = ClassroomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("classroom_list")

    else:
        form = ClassroomForm()

    return render(
        request,
        "school/classrooms/add.html",
        {"form": form}
    )

@login_required(login_url="login")
def classroom_edit(request, id):

    classroom = get_object_or_404(Classroom, id=id)

    if request.method == "POST":

        form = ClassroomForm(request.POST, instance=classroom)

        if form.is_valid():
            form.save()
            return redirect("classroom_list")

    else:
        form = ClassroomForm(instance=classroom)

    return render(
        request,
        "school/classrooms/edit.html",
        {"form": form}
    )

@login_required(login_url="login")
def classroom_delete(request, id):

    classroom = get_object_or_404(Classroom, id=id)

    if request.method == "POST":
        classroom.delete()
        return redirect("classroom_list")

    return render(
        request,
        "school/classrooms/delete.html",
        {"classroom": classroom}
    )

@login_required(login_url="login")
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(
        request,
        "school/teachers/list.html",
        {"teachers": teachers}
    )


@login_required(login_url="login")
def teacher_add(request):

    if request.method == "POST":

        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("teacher_list")

    else:
        form = TeacherForm()

    return render(
        request,
        "school/teachers/add.html",
        {"form": form}
    )


@login_required(login_url="login")
def teacher_edit(request, id):

    teacher = get_object_or_404(Teacher, id=id)

    if request.method == "POST":

        form = TeacherForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return redirect("teacher_list")

    else:
        form = TeacherForm(instance=teacher)

    return render(
        request,
        "school/teachers/edit.html",
        {"form": form}
    )


@login_required(login_url="login")
def teacher_delete(request, id):

    teacher = get_object_or_404(Teacher, id=id)

    if request.method == "POST":
        teacher.delete()
        return redirect("teacher_list")

    return render(
        request,
        "school/teachers/delete.html",
        {"teacher": teacher}
    )

@login_required(login_url="login")
def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "school/students/list.html",
        {"students": students}
    )


@login_required(login_url="login")
def student_add(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(
        request,
        "school/students/add.html",
        {"form": form}
    )


@login_required(login_url="login")
def student_edit(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "school/students/edit.html",
        {"form": form}
    )


@login_required(login_url="login")
def student_delete(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(
        request,
        "school/students/delete.html",
        {"student": student}
    )

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("login")