from django.http import HttpResponse
from django.shortcuts import render

from app11.models import Course, Student

# Create your views here.

def course_search_with_ajax(request):
    if request.method=="POST": 
        courseid=request.POST.get("coursename") 
        s=Student.objects.all() 
        
        student_list=list() 
        
        for student in s: 
            if student.enrollment.filter(id=courseid): 
                student_list.append(student) 
                
        if len(student_list)==0: 
            return HttpResponse("<h1 style='color:red'>No Students enrolled</h1>") 
        else:
            return render(request,"selected_students_ajax.html",{"student_list":student_list}) 
    
    else: 
        my_courses=Course.objects.all()
        return render(request,"course_search_ajax.html",{"courses":my_courses})
