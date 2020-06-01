# !/usr/bin/python3.5
#encoding:utf-8
# 导入数据库模块
import pymysql
from django.http import HttpResponse
from django.shortcuts import render
from time import sleep
from django.shortcuts import render_to_response
import datetime
import traceback
import json
from django.views.decorators.csrf import csrf_exempt
import re
from ferry_devel.views.maternal_baby_mall_info import to_unicode

@csrf_exempt
# 访问搜索到的某商品页
def mall_search(request):
    title = request.GET["title"]

    #把前端传来用户输入的内容中的非字母、非数字、非汉字、非下划线去掉，且把列表中元素转成字符串
    title = re.split(r'\W+',title)
    title = "".join(title)

    if(title == ""):
        return render(request,"maternal_baby_mall_info/html/index.html")
    # 方案1
    # 只要title为“上”、“衣”、“上衣”，就能检索出“上衣”，“上衣”的unicode为\u4e0a\u8863
    # elif(title in re.findall("[\u4e0a\u8863]",title) or title == "上衣"):
    #     return render(request,"maternal_baby_mall_info/html/上衣.html")

    # 方案2
    # elif (title in re.findall("[to_unicode('上衣')]", title) or title == "上衣"):
    #     return render(request, "maternal_baby_mall_info/html/上衣.html")
    # elif(title in re.findall("[to_unicode('摇篮')]",title) or title == "摇篮"):
    #     return render(request,"maternal_baby_mall_info/html/摇篮.html")

    #方案3
    # elif(re.findall("上衣", title, re.M)):
    #     return render(request, "maternal_baby_mall_info/html/上衣.html")
    # elif(re.findall("摇篮",title,re.M)):
    #     return render(request,"maternal_baby_mall_info/html/摇篮.html")

    #方案4
    elif(re.search("上衣",title,re.M)):
        return render(request, "maternal_baby_mall_info/html/上衣.html")
    elif(re.search("摇篮",title,re.M)):
        return render(request, "maternal_baby_mall_info/html/摇篮.html")