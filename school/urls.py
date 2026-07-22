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
] 