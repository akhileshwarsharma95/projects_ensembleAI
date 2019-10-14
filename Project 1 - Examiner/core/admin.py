from django.contrib import admin

from django.apps import AppConfig
from core.models import Course, GECourse, Student, Teachers, Essay

class CoreConfig(AppConfig):
    name = 'core'

class CourseAdmin(admin.ModelAdmin):
    list_display=['name', 'category']

class GECourseAdmin(admin.ModelAdmin):
    list_display=['name']

class StudentAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name']

class TeachersAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name']

class EssayAdmin(admin.ModelAdmin):
    list_display=['student_id', 'created_on','text','grade']

admin.site.register(Course, CourseAdmin)
admin.site.register(GECourse, GECourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Essay, EssayAdmin)
