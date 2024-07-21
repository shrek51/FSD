from django.http import JsonResponse
from django.shortcuts import render

from app10.models import Course, Student, StudentForm

# Create your views here.

def registerstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        courses = Course.objects.all()
        form= StudentForm()
        return render(request, 'student_registration.html', {'courses': courses,'form': form})

def studentlist(request):
    students = Student.objects.all()
    return render(request, 'studentlist.html', {'students': students})
