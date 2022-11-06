from django.db import models
from django.contrib.auth.models import User



class Classroom(models.Model):
    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    year = models.IntegerField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, name="classrooms")


class Student(models.Model):
    pass
