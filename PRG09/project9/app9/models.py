from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, unique=True)
