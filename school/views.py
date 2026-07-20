from django.shortcuts import render

def home(request):
    return render(request, 'school/home.html')

def about(request):
    return render(request, 'school/about.html')