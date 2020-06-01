#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    return HttpResponse("你好，世界")

def hello(request):
    context = {}
    context['hello'] = 'Hello,Ferry'
    #render_to_response使用了一个字典context作为参数，context字典中元素的键'hello'对应了模板中的变量'{{hello}}'
    return render_to_response('hello.html', context)

def introduce(request):
    return HttpResponse("大家好！我是练习时长两年半的个人练习生蔡徐坤，喜欢唱、跳、rap、篮球。")

def see_image(request):
    i = {}
    i['image'] = '/static/image/照骗.jpg'
    return render_to_response('display_image.html',i)

def see_img_float(request):
    return render_to_response('CSS的浮动.html',locals())

def see_img_splicing(request):
    return render_to_response('CSS的图像拼合技术.html',locals())

def see_loading(request):
    return render_to_response('JS实现加载等待“转圈圈”.html',locals())