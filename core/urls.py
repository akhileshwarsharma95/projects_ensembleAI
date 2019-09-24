from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=u'index'),
    path('core/another', views.another, name=u'another'),
    path('core/about', views.about, name=u'about'),

    path('core/contact', views.contact, name=u'contact'),
    path('core/login', views.login_form1, name=u'login_form1'),
    path('core/student', views.sdashboard, name=u'sdashboard'),

    path('core/log-in', views.login_form2, name=u'login_form2'),
    path('core/logout', views.logout, name=u'logout'),
]
