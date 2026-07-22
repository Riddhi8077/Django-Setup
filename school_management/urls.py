from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('school.urls')),
    path("dashboard/", include("dashboard.urls")),
]