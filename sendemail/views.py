# coding:utf-8
from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail
from django.http import HttpResponse
# Create your views here.

def sendemail(request):
    res = send_mail('Subject here','Here is the message', 'cdy19861111@163.com', ['305139630@qq.com'],fail_silently=False)
    return HttpResponse('%s'%res)

def index(request):
    return HttpResponse(u"send email page")

# def contact(request):


