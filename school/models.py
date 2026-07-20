from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    principal = models.CharField(max_length=100)
    established_year = models.IntegerField()

    def __str__(self):
        return self.name
    
class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)
    room_number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.class_name