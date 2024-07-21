from django.contrib import admin

from app10.models import Course

# Register your models here.

@admin.register(Course)
class AddCourseAdmin(admin.ModelAdmin):
    list_display = ('name', "description")
    ordering = ("name",)
    search_fields = ("name",)
