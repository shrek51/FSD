from django.db import models

from django.core.validators import ValidationError
# Create your models here.

genders = (("M", "Male"), ("F", "Female"))
def valid_sem(value):
    if value<1 or value>8:
        raise ValidationError("Invalid sem! Enter sem value between 1 and 8 only.")
    
class Course(models.Model):
    course_code = models.CharField(max_length=14, blank=False, null=False, unique=True)
    course_name = models.CharField(max_length=70, blank=False, null=False)
    course_credits = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return self.course_code + " (" + self.course_name + ")"
    
class Student(models.Model):
    student_usn = models.CharField(max_length=10, blank=False, null=False, unique=True)
    student_name = models.CharField(max_length=80, blank=False, null=False)
    student_sem = models.IntegerField(blank=False, null=False, validators=[valid_sem])
    student_gender = models.CharField(max_length=1, blank=False, null=False, choices=genders)
    enrolment = models.ManyToManyField(Course)
    