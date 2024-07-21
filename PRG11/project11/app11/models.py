from django.db import models

# Create your models here.

ccreds = ((1,0), (2,1), (3,2), (4,3), (5,4))
sems = ((1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8))

class Course(models.Model):
    course_code = models.CharField(max_length=14, blank=False, null=False, unique=True)
    course_name = models.CharField(max_length=70,blank=False, null=False)
    course_credits = models.IntegerField(choices=ccreds)

    def __str__(self):
        return self.course_name
    
    
class Student(models.Model):
    student_usn = models.CharField(max_length=10, blank=False, null=False, unique=True)
    student_name = models.CharField(max_length=80,blank=False, null=False)
    student_sem = models.IntegerField(choices=sems)
    enrollment = models.ManyToManyField(Course)

    def __str__(self):
        return  self.student_name+" ("+self.student_usn+")"
