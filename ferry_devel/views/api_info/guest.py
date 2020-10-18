#encoding=utf-8
from ferry_devel import settings
from django.http import JsonResponse
from TestModel.models import Event
from TestModel.models import Guests
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
import time

#添加嘉宾
@csrf_exempt
def add_guest(request):
    return render(request,"add_guest.html")

#添加嘉宾接口
@csrf_exempt
def add_guest_handle(request):
    event_id = request.POST.get("event_id","")
    phone = request.POST.get("phone","")
    ch_name = request.POST.get("ch_name","")
    #判断发布会ID和手机号码这两个必填项是否填写
    if(event_id == "" or phone == ""):
        return render(request,"add_guest.html",{
            "result_add_guest":{
                "status":10021,
                "message":"发布会ID和嘉宾手机号码都不能为空"
            }
        })
    #判断输入的发布会ID在Event表是否存在（可通过执行sql语句取得结果，也可用objects.filter）
    db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                         charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from testmodel_event where event_id = " + event_id
    cursor.execute(sql)
    db.commit()
    result_event_id = cursor.fetchall() #fetchall()返回元组类型
    if(result_event_id == ()):
        return render(request,"add_guest.html",{
            "result_add_guest": {
                "status": 10022,
                "message": "发布会ID不存在"
            }
        })

    # 判断输入的手机号码的位数是否符合11位
    if(len(phone) != 11):
        return render(request,"add_guest.html",{
            "result_add_guest":{
                "status": 10023,
                "message": "手机号码非法，必须为11位的手机号码"
            }
        })
    #判断发布会ID与手机号码两个维度是否对应已有数据，也就是如果已有人用这个手机号码关联到该发布会，不能添加重复的嘉宾
    result = Guests.objects.filter(phone = phone,event_id_id = event_id)
    if(result):
        return render(request,"add_guest.html",{
            "result_add_guest": {
                "status": 10024,
                "message": "已经有用户用这个手机号码关联到该发布会"
            }
        })
    try:
        Guests.objects.create(phone = phone,ch_name = ch_name,event_id_id = event_id)
    except Exception as e:
        return render(request,"add_guest.html",{
            "result_add_guest": {
                "status": 10025,
                "message": e
            }
        })
    else:
        return render(request,"add_guest.html",{
            "result_add_guest":{
                "status":10000,
                "message":"添加成功"
            }
        })

#发布会签到
@csrf_exempt
def guest_sign(request):
    return render(request,"guest_sign.html")
#发布会签到接口
@csrf_exempt
def guest_sign_handle(request):
    event_id = request.POST.get("event_id","")
    phone = request.POST.get("phone","")
    ch_name = request.POST.get("ch_name","")
    #判断发布会ID和手机号码两个必填项是否填写
    if(event_id == "" or phone == ""):
        return render(request,"guest_sign.html",{
            "result_guest_sign":{
                "status":10021,
                "message":"发布会ID和手机号码都不能为空"
            }
        })
    #判断输入的发布会ID在Event表是否存在
    result_event_id = Event.objects.filter(event_id = event_id)
    if(not result_event_id):
        return render(request,"guest_sign.html",{
            "result_guest_sign":{
                "status":10022,
                "message":"发布会ID不存在"
            }
        })
    #判断发布会在当前是否已开始
    event_start_time = Event.objects.get(event_id = event_id).event_start_time
    print(event_start_time)
    etime = str(event_start_time).split("+")
    timeArray = time.strptime(etime[0],"%Y-%m-%d %H:%M:%S")
    e_time = int(time.mktime(timeArray))

    now_time = time.time()
    ntime = str(now_time).split(".")
    ntimeArray = ntime[0]
    n_time = int(ntimeArray)

    if(n_time >= e_time):
        return render(request,"guest_sign.html",{
            "result_guest_sign":{
                "status":10023,
                "message":"发布会已开始，不能签到"
            }
        })
    #判断手机号码是否存在于嘉宾表
    #由于：django的objects.get方法是从数据库的取得一个匹配的结果，返回一个对象，如果记录不存在的话，它会报错。
    #故：不能用objects.get取结果来做判断，要用objects.filter
    result_phone = Guests.objects.filter(phone = phone)
    if(not result_phone):
        return render(request,"guest_sign.html",{
            "result_guest_sign":{
                "status":10024,
                "message":"该手机号码未被作为某发布会的嘉宾标识"
            }
        })
    #判断发布会ID与手机号码能否对应
    #由于：django的objects.get方法是从数据库的取得一个匹配的结果，返回一个对象，如果记录不存在的话，它会报错。
    #故：不能用objects.get取结果来做判断，要用objects.filter
    result = Guests.objects.filter(event_id = event_id,phone = phone)
    if(not result):
        return render(request,"guest_sign.html",{
            "result_guest_sign":{
                "status":10025,
                "message":"此发布会与该手机号码无关联"
            }
        })
    #判断是否已签到
    result_sign = Guests.objects.get(event_id = event_id,phone = phone).sign
    if(result_sign):
        return render(request,"guest_sign.html",{
            "result_guest_sign": {
                "status": 10026,
                "message": "已经签到过，无需重复"
            }
        })
    else:
        Guests.objects.filter(event_id = event_id,phone = phone).update(sign = True)
        return render(request,"guest_sign.html",{
            "result_guest_sign": {
                "status": 10000,
                "message": "签到成功"
            }
        })
