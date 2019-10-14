from django.db import models
from datetime import datetime
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=250, default='')
    category = models.CharField(max_length=250, default='')

class GECourse(models.Model):
    name = models.CharField(max_length=250, default='')

class Student(models.Model):
    registration_num = models.CharField(max_length=250, default='')
    email =  models.CharField(max_length=250, default='')
    first_name = models.CharField(max_length=250, default='')
    last_name = models.CharField(max_length=250, default='')
    password = models.CharField(max_length=2000, default='')
    course = models.ForeignKey(Course, default=None, null=True, on_delete=models.CASCADE)
    ge_course = models.ForeignKey(GECourse, default=None, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=250, default='')
    gender = models.CharField(max_length=250, default='')

class Teachers(models.Model):
    registration_num = models.CharField(max_length=250, default='')
    email =  models.CharField(max_length=250, default='')
    first_name = models.CharField(max_length=250, default='')
    last_name = models.CharField(max_length=250, default='')
    password = models.CharField(max_length=2000, default='')
    initials = models.CharField(max_length=250, default='')
    ge_course = models.ForeignKey(GECourse, default=None, null=True, on_delete=models.CASCADE,)
    department_name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    gender = models.CharField(max_length=250, default='')
    
class Essay(models.Model):
    student=models.ForeignKey(Student, default=None, null=True, on_delete=models.CASCADE,)
    text=models.CharField(max_length=5000, default='', null=True)
    title=models.CharField(max_length=5000, default='', null=True)
    created_on=models.DateTimeField(default=datetime.now(), blank=True)
    grade=models.CharField(max_length=50, default='', null=True)
    feedback=models.CharField(max_length=2000, default='', null=True)
