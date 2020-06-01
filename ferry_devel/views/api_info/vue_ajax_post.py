# encoding:utf-8
from ferry_devel import settings
from django.http import JsonResponse
from TestModel.models import Event
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import pymysql
import xlsxwriter
import xlwt
import datetime
from excel_response3 import ExcelResponse
from io import BytesIO
from io import StringIO
from django.http import HttpResponse
from django.core.files.storage import default_storage
import os
import json

'''
我们在后台进行数据获取时，有两种方法（以username为例）：request.POST[‘username’]与request.POST.get(‘username’)，那么这两者有什么不同之处呢？
如果传递过来的数值不为空，那么这两种方法都没有错误，可以得到相同的结果。但是如果传递过来的数值为空，那么request.POST[‘username’]则会提示Keyerror错误，而request.POST.get(‘username’)则不会报错，而是返回一个none。
'''


# 将据库表event的event_status对应发布会状态
@csrf_exempt
def event_status_to_string(num):
    if (num == 1):
        event_status_string = "未开始"
    if (num == 2):
        event_status_string = "进行中"
    if (num == 3):
        event_status_string = "已结束"
    if (num == 4):
        event_status_string = "取消"
    return event_status_string

@csrf_exempt
# 查询发布会接口
def get_event_handle(request):
    #用json.loads()函数是将json格式数据转换为字典
    event_data = json.loads(request.body)
    event_id = event_data["event_id"]
    event_name = event_data["event_name"]
    print(event_data)
    # 如果发布会ID和发布会标题都为空
    if (event_id == "" and event_name == ""):
        return JsonResponse({
            "result": {
                "status": 10021,
                "message": "发布会ID和发布会标题，至少要输入一项，进行查询"
            },
        }, content_type="application/json")

    # 如果发布会ID不为空
    if (event_id != ""):
        result_event = {}
        try:
            result = Event.objects.get(event_id=event_id)
        except Exception as e:
            return JsonResponse({
                "status": 10022,
                "message": e
            }, content_type="application/json")
        # 无异常时
        else:
            result_event["get_event_id"] = result.event_id
            result_event["get_event_name"] = result.event_name
            result_event["get_event_limit"] = result.event_limit
            result_event["get_event_status"] = event_status_to_string(result.event_status)
            result_event["get_event_address"] = result.event_address
            result_event["get_event_start_time"] = result.event_start_time
            return JsonResponse({
                "result": {
                    "status": 200,
                    "message": "查询成功",
                    "data": [result_event]
                }
            }, content_type="application/json")

    # 如果发布会名称不为空
    if (event_name != ""):
        result_event = {}
        datas = []
        # django的objects.filter方法是从数据库的取得匹配的结果，返回一个对象列表，如果记录不存在的话，它会返回[]。
        results = Event.objects.filter(event_name=event_name)
        if (results):
            for r in results:
                result_event["get_event_id"] = r.event_id
                result_event["get_event_name"] = r.event_name
                result_event["get_event_limit"] = r.event_limit
                result_event["get_event_status"] = event_status_to_string(r.event_status)
                result_event["get_event_address"] = r.event_address
                result_event["get_event_start_time"] = r.event_start_time
                datas.append(result_event)
            return JsonResponse({
                "status": 200,
                "message": "查询成功",
                "data": datas
            }, content_type="application/json")
        else:
            return JsonResponse({
                "status": 10022,
                "message": "查询结果为空"
            }, content_type="application/json")
