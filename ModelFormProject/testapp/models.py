from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=15)
    sid=models.IntegerField()
    marks=models.IntegerField()
    address=models.CharField(max_length=30)
