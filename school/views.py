from django.shortcuts import render, redirect
from .models import School, Classroom, Teacher, Student
from .forms import ClassroomForm, TeacherForm, StudentForm
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

        name = request.POST.get("name")
        principal = request.POST.get("principal")
        address = request.POST.get("address")
        established_year = request.POST.get("established_year")

        School.objects.create(
            name=name,
            principal=principal,
            address=address,
            established_year=established_year
        )

        return redirect("school_list")

    return render(request, "school/schools/add.html")

@login_required(login_url="login")
def school_edit(request, id):

    school = get_object_or_404(School, id=id)

    if request.method == "POST":

        school.name = request.POST.get("name")
        school.principal = request.POST.get("principal")
        school.address = request.POST.get("address")
        school.established_year = request.POST.get("established_year")

        school.save()

        return redirect("school_list")

    return render(
        request,
        "school/schools/edit.html",
        {
            "school": school
        }
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

        school_id = request.POST.get("school")
        class_name = request.POST.get("class_name")
        room_number = request.POST.get("room_number")
        capacity = request.POST.get("capacity")

        school = School.objects.get(id=school_id)

        Classroom.objects.create(
            school=school,
            class_name=class_name,
            room_number=room_number,
            capacity=capacity
        )

        return redirect("classroom_list")

    schools = School.objects.all()

    return render(
        request,
        "school/classrooms/add.html",
        {
            "schools": schools
        }
    )

@login_required(login_url="login")
def classroom_edit(request, id):

    classroom = get_object_or_404(Classroom, id=id)

    if request.method == "POST":

        school_id = request.POST.get("school")
        classroom.school = School.objects.get(id=school_id)

        classroom.class_name = request.POST.get("class_name")
        classroom.room_number = request.POST.get("room_number")
        classroom.capacity = request.POST.get("capacity")

        classroom.save()

        return redirect("classroom_list")

    schools = School.objects.all()

    return render(
        request,
        "school/classrooms/edit.html",
        {
            "classroom": classroom,
            "schools": schools,
        }
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

        classroom_id = request.POST.get("classroom")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        subject = request.POST.get("subject")
        email = request.POST.get("email")

        classroom = Classroom.objects.get(id=classroom_id)

        Teacher.objects.create(
            classroom=classroom,
            first_name=first_name,
            last_name=last_name,
            subject=subject,
            email=email
        )

        return redirect("teacher_list")

    classrooms = Classroom.objects.all()

    return render(
        request,
        "school/teachers/add.html",
        {
            "classrooms": classrooms
        }
    )


@login_required(login_url="login")
def teacher_edit(request, id):

    teacher = get_object_or_404(Teacher, id=id)

    if request.method == "POST":

        classroom_id = request.POST.get("classroom")

        teacher.classroom = Classroom.objects.get(id=classroom_id)
        teacher.first_name = request.POST.get("first_name")
        teacher.last_name = request.POST.get("last_name")
        teacher.subject = request.POST.get("subject")
        teacher.email = request.POST.get("email")

        teacher.save()

        return redirect("teacher_list")

    classrooms = Classroom.objects.all()

    return render(
        request,
        "school/teachers/edit.html",
        {
            "teacher": teacher,
            "classrooms": classrooms,
        }
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