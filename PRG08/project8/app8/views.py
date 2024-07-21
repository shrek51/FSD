from django.shortcuts import render
from app8.models import Student, Course
from django.views.generic import ListView, DetailView

# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = "student_gen_list.html"
    
class StudentDetailView(DetailView):
    model = Student
    template_name = "student_gen_detail.html"