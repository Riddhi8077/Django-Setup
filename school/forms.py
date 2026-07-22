from django import forms
from .models import School, Classroom, Teacher, Student
from .models import School, Classroom

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = "__all__"


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"