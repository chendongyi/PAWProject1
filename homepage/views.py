# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return HttpResponse(u"欢迎来到主页haha")


def newpage(request):
    return HttpResponse(u"welcome")

