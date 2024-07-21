from django.contrib import admin

from app6.models import Course, Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_usn", "student_name", "student_sem",)
    ordering = ("student_sem",)
    search_fields = ("student_name", "student_usn",)
admin.site.register(Course)

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ("course_code", "course_name", "course_credits")
#     search_fields = ("student_name", "student_usn")
# admin.site.register(Course)