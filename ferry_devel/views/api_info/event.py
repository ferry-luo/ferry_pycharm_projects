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

'''
我们在后台进行数据获取时，有两种方法（以username为例）：request.POST[‘username’]与request.POST.get(‘username’)，那么这两者有什么不同之处呢？
如果传递过来的数值不为空，那么这两种方法都没有错误，可以得到相同的结果。但是如果传递过来的数值为空，那么request.POST[‘username’]则会提示Keyerror错误，而request.POST.get(‘username’)则不会报错，而是返回一个none。
'''

@csrf_exempt
#将选择的发布会状态对应数据库表event的event_status
def event_status_to_number(str):
    if(str == "-请选择-" or str == "未开始"):
        event_status_number = 1
    if(str == "进行中"):
        event_status_number = 2
    if(str == "已结束"):
        event_status_number = 3
    if(str == "取消"):
        event_status_number = 4
    return event_status_number

#将据库表event的event_status对应发布会状态
@csrf_exempt
def event_status_to_string(num):
    if(num == 1):
        event_status_string = "未开始"
    if(num == 2):
        event_status_string = "进行中"
    if(num == 3):
        event_status_string = "已结束"
    if(num == 4):
        event_status_string = "取消"
    return event_status_string

@csrf_exempt
#
def add_event(request):
    return render(request, "add_event.html", {
        "result_add_event": {
            "status_list": [u'-请选择-',u'未开始', u'进行中', u'已结束', u'取消']
        }
    })


@csrf_exempt
# 添加发布会接口
def add_event_handle(request):
    # request.POST.get('sth', 'default_value')，如果sth不存在的话，指定默认值default_value
    event_id = request.POST.get("event_id", "")
    event_name = request.POST.get("event_name", "")
    event_limit = request.POST.get("event_limit", "")
    event_status = request.POST.get("event_status", "")
    event_address = request.POST.get("event_address", "")
    event_start_time = request.POST.get("event_start_time", "")

    if (
            event_id == "" or event_name == "" or event_limit == "" or event_status == "" or event_address == "" or event_start_time == ""):
        # return JsonResponse({
        #     "status": 10021,
        #     "message": "parameter error"
        # }, content_type="application/json")
        return render(request, "add_event.html", {
            "result_add_event": {
                "status": 10021,
                "message": "参数错误，请确保各项都已填写。",
                "status_list": [u'-请选择-',u'未开始', u'进行中', u'已结束', u'取消']
            }
        })

    # django的objects.filter方法是从数据库的取得匹配的结果，返回一个对象列表，如果记录不存在的话，它会返回[]。 filter()括号中，等号左边是数据库表字段名，右边是从前端传来的参数
    # django的objects.get方法是从数据库的取得一个匹配的结果，返回一个对象，如果记录不存在的话，它会报错。
    # 如果id和name已存在，返回提示
    result_id = Event.objects.filter(event_id=event_id)
    if (result_id):
        # return JsonResponse({
        #     "status": 10022,
        #     "message": "event id is already exist"
        # }, content_type="application/json")
        return render(request, "add_event.html", {
            "result_add_event": {
                "status": 10022,
                "message": "发布会ID已存在",
                "status_list": [u'-请选择-',u'未开始', u'进行中', u'已结束', u'取消']
            }
        })
    result_name = Event.objects.filter(event_name=event_name)
    if (result_name):
        # return JsonResponse({
        #     "status": 10023,
        #     "message": "event name is already exist"
        # }, content_type="application/json")
        return render(request, "add_event.html", {
            "result_add_event": {
                "status": 10022,
                "message": "发布会标题已存在",
                "status_list": [u'-请选择-',u'未开始', u'进行中', u'已结束', u'取消']
            }
        })
    # 由于status不是必传字段，所以判断如果为空，则将status设为1，表示开启状态
    if (event_status == "-请选择-"):
        event_status_number = 1
    # 将数据插入Event表，插入过程中如果日期格式有误，则抛出ValidationError异常，返回相应的提示。否则，插入成功
    try:
        Event.objects.create(event_id=event_id, event_name=event_name, event_limit=event_limit,
                             event_address=event_address, event_status=event_status_to_number(event_status),
                             event_start_time=event_start_time)
    except ValidationError as e:
        error = "start_time format error.It must be in YYYY-MM-DD HH:MM:SS format"
        return JsonResponse({
            "status": 10024,
            "message": error
        }, content_type="application/json")
    # 无异常时
    else:
        return render(request, "add_event.html", {
            "result_add": {
                "status": 200,
                "message": "添加成功",
                "status_list": [u'-请选择-',u'未开始', u'进行中', u'已结束', u'取消']
            }
        })
        # return JsonResponse({
        #     "status": 200,
        #     "message": "add event success"
        # }, content_type="application/json")

@csrf_exempt
# 查询发布会默认页面
def get_event(request):
    return render(request, "get_event.html")

@csrf_exempt
# 查询发布会接口
def get_event_handle(request):
    event_id = request.POST.get("event_id", "")
    event_name = request.POST.get("event_name", "")
    # 如果发布会ID和发布会标题都为空
    if (event_id == "" and event_name == ""):
        return render(request, "get_event.html", {
            "result": {
                "status": 10021,
                "message": "发布会ID和发布会标题，至少要输入一项，进行查询"
            },
        })
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
            return render(request, "get_event.html", {
                "result": {
                    "status": 200,
                    "message": "查询成功",
                    "data": [result_event]
                }
            })
            # return JsonResponse({
            #     "status": 200,
            #     "message": "查询成功"
            # }, content_type="application/json")
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
            return render(request, "get_event.html", {
                "result": {
                    "status": 200,
                    "message": "查询成功",
                    "data": [result_event]
                },
            })
            # return JsonResponse({
            #     "status":200,
            #     "message":"查询成功",
            #     "data":datas
            # },content_type="application/json")
        else:
            return render(request, "get_event.html", {
                "result": {
                    "status": 10022,
                    "message": "查询结果为空",
                    "data": []
                },
            })
            # return JsonResponse({
            #     "status": 10022,
            #     "message": "查询结果为空"
            # }, content_type="application/json")

@csrf_exempt
# 导出数据到excel
def export_event(request):
    event_list = []
    check_id_s = request.GET.get("check_id_s")
    if (len(check_id_s) > 0):
        # results = Event.objects.raw("select * from Event where event_id in (" + check_id_s + ")")
        # for r in results:
        #     result_export_event = Event.objects.filter(event_id = r.event_id)
        #     event_list.append([r.event_id,r.event_name,r.event_limit,r.event_address,r.event_start_time])
        result = Event.objects.get(event_id=check_id_s[0])
        result_export_event = {}
        result_export_event["get_event_name"] = result.event_name
        result_export_event["get_event_limit"] = result.event_limit
        result_export_event["get_event_address"] = result.event_address
        result_export_event["get_event_start_time"] = result.event_start_time

        # 建立文件
        workbook = xlwt.Workbook(encoding="utf-8")
        # 建立sheet
        worksheet = workbook.add_sheet("event_sheet")
        # 写入
        worksheet.write(0, 0, "发布会名称")
        worksheet.write(0, 1, "发布会限制人数")
        worksheet.write(0, 2, "发布会地址")
        worksheet.write(0, 3, "发布会开始时间")
        worksheet.write(1, 0, result_export_event["get_event_name"])
        worksheet.write(1, 1, result_export_event["get_event_limit"])
        worksheet.write(1, 2, result_export_event["get_event_address"])
        worksheet.write(1, 3, result_export_event["get_event_start_time"].strftime("%Y-%m-%d %H:%M"))

        # 创建操作二进制数据的对象
        bio = BytesIO()
        # 将Excel数据写入内存
        workbook.save(bio)
        # 设置文件读取的偏移量，0表示从头读起
        bio.seek(0)
        response = HttpResponse(bio.getvalue(), content_type="application/vnd.ms-excel")
        response["Content-Disposition"] = "attachment;filename=%s.xls" % (
                "event_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        response.write(bio.getvalue())
        return response

@csrf_exempt
# 处理导入的Excel文件
def import_event(request):
    result_upload = {}
    if (request.method == "POST" and request.FILES.get("event_excel")):
        event_excel_file = request.FILES["event_excel"]
        file_name = os.path.join(settings.BASE_DIR + "/static/upload/event/", event_excel_file.name)
        print(file_name)
        try:
            event_excel_file_path = default_storage.save(
                file_name, event_excel_file)
            # print(event_excel_file_path)

            event_excel_file_url = "http://47.94.202.0:8000/static/upload/event/" + \
                                   event_excel_file_path.split("/")[-1]
            # return JsonResponse({
            #     "result_upload": {
            #         "status": 0,
            #         "message": "上传成功",
            #         "data": [
            #             {
            #                 "excel_url": event_excel_file_url,
            #                 "excel_name": event_excel_file_path.split("/")[-1]
            #             }
            #         ]
            #     }
            # })
            return render(request, "get_event.html", {
                "result_upload": {
                    "status": 0,
                    "message": "上传成功",
                    "data": [
                        {
                            "excel_url": event_excel_file_url,
                            "excel_name": event_excel_file_path.split("/")[-1]
                        }
                    ]
                }
            })
        except IOError:
            result_upload["message"] = "上传失败"
            return render(request, "get_event.html", {"result_upload": result_upload})
    else:
        result_upload["message"] = "上传失败"
        # return HttpResponse("上传失败")
        return render(request, "get_event.html", {"result_upload": result_upload})

@csrf_exempt
# 删除数据
def delete_event(request):
    check_id_s = request.GET.get("check_id_s")
    # 连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                         charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    if (len(check_id_s) > 0):
        sql = "delete from testmodel_event where event_id in (" + check_id_s + ")"
        cursor.execute(sql)
        db.commit()
        return render(request, "get_event.html")
