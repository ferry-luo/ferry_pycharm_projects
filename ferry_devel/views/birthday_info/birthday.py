#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect

from django.conf import settings
import os


def go_birthday_PTY_0301(request):
    return render_to_response('birthday_PTY_0301.html',locals())

