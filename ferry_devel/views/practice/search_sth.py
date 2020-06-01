#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render


#提交数据时使用到get方法，视图显示和请求处理分成两个函数处理。
def search(request):
    if 'question' in request.GET and request.GET['question']:
        message = '你搜索的内容是：'+request.GET['question']
    else:
        message = '你没有输入任何内容进行搜索'
    return HttpResponse(message)

def search_form(request):
    return render_to_response('search_form.html')

#更常用post方法，视图显示和请求处理只用一个函数处理。
def search_post(request):
    content={}
    if request.POST:
        x = request.POST['question']
        if x == "蔡徐坤":
            content['c'] = x
    return render(request,'search_form2.html',content)
