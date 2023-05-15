from django.db import models

# Create your models here.
class student(models.Model):
    sname=models.CharField(max_length=100)
    marks=models.IntegerField()
    subject=models.CharField(max_length=100)
