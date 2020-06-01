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

@csrf_exempt
def information(request):
    return render(request,'maternal_baby_mall_info/html/information.html')