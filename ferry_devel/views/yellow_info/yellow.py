#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect

from django.conf import settings
import os

def go_yellow_amusement(request):
    return render_to_response('yellow_amusement.html',locals())

def go_contact_us(request):
    return render_to_response('contact_us.html',locals())

def go_yellow_happy(request):
    return render_to_response('yellow_happy.html',locals())

def go_yellow_website(request):
    try:
        if request.GET:
            user_choose = request.GET["sex_choice"]
            if user_choose == "女":
                return render_to_response('yellow_amusement.html', locals())
            '''其他东西改为用前端判断
            if user_choose == "-请选择-":
                return HttpResponse("请选择有效性别再提交")
            else:
                return HttpResponse("您不能进一步浏览娱乐网页")
            '''
        return render_to_response('user_form.html',locals())
    except Exception as e:
        return HttpResponse(e)