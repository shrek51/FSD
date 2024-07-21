from django.contrib import admin

from app8.models import Course, Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["student_name", "student_usn", "student_sem", "student_gender"]
    ordering = ["student_sem"]
    search_fields = ["student_name", "student_usn"]
    
admin.site.register(Course)