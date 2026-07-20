from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    principal = models.CharField(max_length=100)
    established_year = models.IntegerField()

    def __str__(self):
        return self.name