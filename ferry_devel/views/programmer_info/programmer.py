#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect

from django.conf import settings
import os

def go_programmer_festival(request):
    return render_to_response('programmer_festival.html',locals())
