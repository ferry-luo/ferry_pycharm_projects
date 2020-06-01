#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect

from django.conf import settings
import os

def go_confession(request):
    return render_to_response('confession_to_yixiu.html',locals())