from django.shortcuts import render, redirect
from core.models import Course, GECourse, Student, Teachers, Essay
from django.http import HttpResponseRedirect, HttpResponse ,JsonResponse
from core.essay_process import essay_process
import random

def index(request):
    # c = Course()
    # c.name = "EMS"
    # c.category = "Physical science"
    # c.save()

    course_list = Course.objects.values('id', 'name', 'category')
    context = {}
    context['course_list'] = course_list
    return render(request, 'index.html', context)

def another(request):
    return render(request, 'another.html',{})

def about(request):
    return render(request, 'about.html',{})


def contact(request):
    context = {}
    # context['name'] = 20
    return render(request, 'contact.html', context)

def login_form1(request):
    try:
        pass
    except Exception as err:
        print("afdew")
    try:
        student_id = request.COOKIES['student_id']
        student_id = int(student_id)
        if student_id > 0:
            return redirect('sdashboard')
    except:
        pass
    context = {}
    context['error'] = ''
    context['email'] = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        this_student = Student.objects.filter(email=email)
        if len(this_student) == 0:
            context['error'] = "You are not registered yet. Please sign up!"
        else:
            this_password = this_student[0].password
            this_id = this_student[0].id
            if this_password != password:
                context['error'] = "Incorrect Password!"
                context['email'] = email
            else:
                response = redirect('sdashboard')
                response.set_cookie('student_id', this_id, path='')
                return response

    return render(request, 'login_form1.html',context)

def sdashboard(request):
    context = {}
    is_submitted = 0
    grade = ""
    try:
        student_id = request.COOKIES['student_id']
        student_id = int(student_id)
        if not student_id > 0:
            return redirect('login_form1')
    except:
        return redirect('login_form1')
    if request.method == 'POST':
        title = request.POST.get('title')
        essay = request.POST.get('essay')
        file = request.POST.get('file')
        grade = random.choice(['CS1', 'CS2'])
        essay_obj = Essay()
        essay_obj.student = Student.objects.get(id=student_id)
        essay_obj.text = essay
        essay_obj.title = title
        essay_obj.grade = grade
        essay_obj.feedback = ""
        essay_obj.save()
        # print(essay, file)
        is_submitted = 1
        new_essay = essay_process(essay)

    essay_history = Essay.objects.filter(student_id=student_id)
    context['essay_history'] = essay_history
    context['is_submitted'] = is_submitted
    context['grade'] = grade
    print(essay_history)
    return render(request, 'sdashboard.html', context)

def logout(request):
    response = redirect('login_form1')
    response.set_cookie('student_id', -1, path='')
    return response

def login_form2(request):
    return render(request, 'login_form2.html',{})
