from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('schools/', views.schools, name='schools'),
    path('classrooms/', views.classrooms, name='classrooms'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
    "dashboard/schools/",
    views.school_list,
    name="school_list"
),
path(
    "dashboard/schools/add/",
    views.school_add,
    name="school_add"
),
path(
    "dashboard/schools/edit/<int:id>/",
    views.school_edit,
    name="school_edit"
),
path(
    "dashboard/schools/delete/<int:id>/",
    views.school_delete,
    name="school_delete"
),
] 