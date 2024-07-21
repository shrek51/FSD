from django.contrib import admin
from app9.models import Student

# Register your models here.

@admin.register(Student)
class AddStudentAdmin(admin.ModelAdmin):
    list_display = ('name', "email")
    ordering = ("name",)
    search_fields = ("name",)
