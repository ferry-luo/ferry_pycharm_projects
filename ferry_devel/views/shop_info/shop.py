#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response

def go_shopping(request):
    return render_to_response('shopping.html',locals())