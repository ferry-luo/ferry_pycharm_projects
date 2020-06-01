# encoding:utf-8
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
#是否包邮，状态转换为文字
def free_shipping_to_string(num):
    if(num == 0):
        free_shipping_string = "否"
    if(num == 1):
        free_shipping_string = "是"
    return free_shipping_string
@csrf_exempt
#商品详情页
def commodity_details(request):
    db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                         use_unicode=True, charset="utf8")
    cursor = db.cursor()
    shop_code = request.GET.get("shop_code")
    if (len(shop_code) > 0):
        datas = {}
        sql = "select * from shopping_mall where shop_code='%s' " % (shop_code)
        try:
            cursor.execute(sql)
            result_sql = cursor.fetchall()
            if(len(result_sql) == 1):
                for row in result_sql:
                    datas["shop_code"] = row[0]
                    datas["shop_name"] = row[1]
                    datas["shop_price"] = row[2]
                    datas["free_shipping"] = free_shipping_to_string(row[3])
                return render(request, "maternal_baby_mall_info/html/details_" + shop_code +".html",{
                    "result":{
                        "status":1000,
                        "message":"查询商品详情成功",
                        "data":[
                            {
                                "shop_code": datas["shop_code"],
                                "shop_name": datas["shop_name"],
                                "shop_price": datas["shop_price"],
                                "free_shipping": datas["free_shipping"]
                            }
                        ]
                    }
                })
        except:
            traceback.print_exc()
            db.rollback()
