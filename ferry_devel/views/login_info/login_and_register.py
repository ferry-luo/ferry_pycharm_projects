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

@csrf_exempt
# 默认路径访问登录页面
def login(request):
    return render_to_response("maternal_baby_mall_info/html/login.html",locals())

@csrf_exempt
# 默认路径访问注册页面
def register(request):
    return render_to_response("register.html",locals())



@csrf_exempt
# 获取注册请求及处理
def register_handle(request):
    # 把用户名和密码注册到数据库中
    user_name = request.POST['user']
    user_pwd = request.POST['password']
    user_nickname = request.POST['nickname']
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if(user_name == "" or user_pwd == ""):
        return render(request, 'register.html', {
            "result_register":{
                "message":"用户名和密码都不能为空",
                "data":[]
            }
        })
    # 连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect(host="localhost",port=3306,user="root",password="123456",database="ferry_test",charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    #先查数据库表，如果用户名已存在，注册失败
    sql_1 = "SELECT user_name FROM ferry_user WHERE user_name = '%s'" % (user_name)

    # SQL 插入语句
    # sql = "INSERT INTO user(user, pwd, nick_name) VALUES (" + request.args.get('user') + ", " + request.args.get('password') + ")"
    sql = "INSERT INTO ferry_user(user_name, user_pwd, user_nickname, create_time) VALUES ('%s', '%s', '%s', '%s')" % (
        user_name, user_pwd, user_nickname, create_time)
    try:
        cursor.execute(sql_1)
        result_sql_1 = cursor.fetchall()
        #print(len(result_sql_1))
        if len(result_sql_1) == 1:
            return render(request, 'register.html', {
                "result_register": {
                    "message": "用户名已存在",
                    "data": []
                }
            })
        else:
            # 执行insert into语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            # 注册成功之后跳转到登录页面
            return render_to_response('login.html', locals())
    except:
        # 抛出错误信息
        traceback.print_exc()
        # 如果发生错误则回滚
        db.rollback()
        return HttpResponse('注册失败')
    # 关闭数据库连接
    db.close()

@csrf_exempt
#获取登录请求及处理
def login_handle(request):
    # 查询用户名及密码是否匹配及存在
    # 连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                         use_unicode=True, charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    user_name = request.POST['user']
    user_pwd = request.POST['password']

    sql = "select * from ferry_user where user_name='%s' and user_pwd='%s'" % (user_name, user_pwd)
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        print(len(results))
        result_data = {}
        if (user_name == "" or user_pwd == ""):
            return render(request, 'maternal_baby_mall_info/html/login.html', {
                "result_login":{
                    "message": "用户名和密码都不能为空",
                    "data":[]
                }
            })
        if len(results) == 1:
            for row in results:
                result_data["userid"] = row[0]
                result_data["username"] = row[1]
                result_data["password"] = row[2]
                result_data["nickname"] = row[3]
                result_data["time"] = row[4]
            return render(request, 'maternal_baby_mall_info/html/index.html', {
                "result_login":{
                    "message":"登录成功",
                    "data":[
                        {
                            "userid":result_data["userid"],
                            "username":result_data["username"],
                            "password":result_data["password"],
                            "nickname":result_data["nickname"],
                            "time":result_data["time"]
                        }
                    ]
                }
            })
        else:
            #return HttpResponse('用户名或密码不正确')
            return render(request, 'maternal_baby_mall_info/html/login.html', {
                "result_login":{
                    "message": "用户名或密码不正确",
                    "data":[]
                }
            })
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()

@csrf_exempt
def logout(request):
    return render(request,'maternal_baby_mall_info/html/logout.html')