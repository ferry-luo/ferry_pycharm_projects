# encoding:utf-8
from ferry_devel import settings
from django.http import JsonResponse
from TestModel.models import MusicInfo, MusicDetailInfo
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import pymysql
import xlsxwriter
import xlwt
import datetime
import time
from excel_response3 import ExcelResponse
from io import BytesIO
from io import StringIO
from django.http import HttpResponse
from django.core.files.storage import default_storage
import os
import socket
from django.core.files.base import ContentFile
import pymysql

# 获取计算机名称
hostname = socket.gethostname()
# 获取本机IP
ip = socket.gethostbyname(hostname)


# 获取轮播图
def get_xusong_banner(request):
    return JsonResponse({
        "message": [
            {
                "image_src": "https://ferry1119.com:8000/static/images/xusong/xusong_banner1.jpg"
            },
            {
                "image_src": "https://ferry1119.com:8000/static/images/xusong/xusong_banner2.jpg"
            },
            {
                "image_src": "https://ferry1119.com:8000/static/images/xusong/xusong_banner3.jpg"
            }
        ],
        "meta": "获取成功！",
        "status": 200
    })


# 获取分类导航数据
def get_xusong_catitems(request):
    return JsonResponse({
        "message": [
            {
                "name": "歌曲",
                "image_src": "https://ferry1119.com:8000/static/images/xusong/yinyue_colour.png",
                "open_type": "switchTab",
                "navigator_url": "/pages/music_list/index"
            },
            {
                "name": "专辑",
                "image_src": "https://ferry1119.com:8000/static/images/xusong/专辑.png",
                "open_type": "switchTab",
                "navigator_url": "/pages/album_list/index"
            },
            {
                "name": "相册",
                "image_src": "https://ferry1119.com:8000/static/images/xusong/相册.png",
                "open_type": "switchTab",
                "navigator_url": "/pages/photo_list/index"
            }
        ],
        "meta": "获取成功！",
        "status": 200
    })


# 获取楼层数据
def get_xusong_floordata(request):
    if request.method == "GET":
        return JsonResponse({
            "message": [
                {
                    "floor_title": {
                        "name": "热门推荐",
                        "image_src": "https://ferry1119.com:8000/static/images/xusong/热门推荐.png"
                    },
                    "recommend_list": [
                        {
                            "name": "粉色信笺",
                            "image_src": "https://ferry1119.com:8000/static/images/xusong/粉色信笺.jpg",
                            "image_width": "232",
                            "open_type": "navigate",
                            "navigator_url": "/pages/music_detail/index?music_id=62"
                        },
                        {
                            "name": "清明雨上",
                            "image_src": "https://ferry1119.com:8000/static/images/xusong/惊鸿一面.jpg",
                            "image_width": "233",
                            "open_type": "navigate",
                            "navigator_url": "/pages/music_detail/index?music_id=14"
                        },
                        {
                            "name": "弹指一挥间",
                            "image_src": "https://ferry1119.com:8000/static/images/xusong/如约而至.jpg",
                            "image_width": "233",
                            "open_type": "navigate",
                            "navigator_url": "/pages/music_detail/index?music_id=31"
                        },
                        {
                            "name": "温泉",
                            "image_src": "https://ferry1119.com:8000/static/images/xusong/温泉.jpg",
                            "image_width": "233",
                            "open_type": "navigate",
                            "navigator_url": "/pages/music_detail/index?music_id=42"
                        },
                        {
                            "name": "全世界最好的你",
                            "image_src": "https://ferry1119.com:8000/static/images/xusong/雅俗共赏.jpg",
                            "image_width": "233",
                            "open_type": "navigate",
                            "navigator_url": "/pages/music_detail/index?music_id=10"
                        }
                    ]
                },
            ],
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        })


# 获取歌曲
def get_xusong_music(request):
    query = request.GET.get("query", "")
    if query == "":
        result_music = []
        try:
            db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                                 charset="utf8")
            cursor = db.cursor()
            sql = "select t1.name,t2.id,t2.name from testmodel_albuminfo t1,testmodel_musicinfo t2 where t1.id = t2.album_info_id"
            cursor.execute(sql)
            result_tuple = cursor.fetchall()
        except Exception as e:
            return JsonResponse({
                "message": None,
                "meta": {
                    "msg": e,
                    "status": 201
                }
            })
        else:
            for k in range(len(result_tuple)):
                result_music.append({
                    "music_id": result_tuple[k][1],
                    "music_name": result_tuple[k][2],
                    "music_album": result_tuple[k][0]
                })
            return JsonResponse({
                "message": {
                    "total": len(result_tuple),
                    "music": result_music,
                },
                "meta": {
                    "msg": "获取成功",
                    "status": 200
                }
            })
    elif query != "":
        result_music = []
        try:
            # result = MusicInfo.objects.filter(name__contains=query)
            db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                                 charset="utf8")
            cursor = db.cursor()
            sql = "select t1.name,t2.id,t2.name from testmodel_albuminfo t1,testmodel_musicinfo t2 where t1.id = t2.album_info_id and t2.name like '%%%s%%'" % query
            cursor.execute(sql)
            result_tuple = cursor.fetchall()
        except Exception as e:
            return JsonResponse({
                "message": None,
                "meta": {
                    "msg": e,
                    "status": 201
                }
            })
        else:
            for k in range(len(result_tuple)):
                result_music.append({
                    "music_id": result_tuple[k][1],
                    "music_name": result_tuple[k][2],
                    "music_album": result_tuple[k][0]
                })
            return JsonResponse({
                "message": {
                    "total": len(result_tuple),
                    "music": result_music
                },
                "meta": {
                    "msg": "获取成功",
                    "status": 200
                }
            })


# 获取歌曲详情
def get_xusong_music_detail(request):
    if request.method == "GET":
        music_id = request.GET.get("music_id", "")
        result_music_detail = {}
        try:
            result = MusicDetailInfo.objects.get(id=music_id)
            db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                                 charset="utf8")
            cursor = db.cursor()
            sql = "select t1.image,t1.name from testmodel_albuminfo t1,testmodel_musicdetailinfo t2 where t1.id = t2.album_info_id and t2.id = " + music_id
            cursor.execute(sql)
            result_album_image_tuple = cursor.fetchone()
        except Exception as e:
            return JsonResponse({
                "message": None,
                "meta": {
                    "msg": e,
                    "status": 201
                }
            })
        else:
            result_music_detail["album_image"] = "https://ferry1119.com:8000/media/" + result_album_image_tuple[0]
            result_music_detail["album_name"] = result_album_image_tuple[1]
            result_music_detail["music_id"] = result.id
            result_music_detail["music_name"] = result.name
            result_music_detail["music_src"] = "https://ferry1119.com:8000/media/" + result.music_src
            result_music_detail["words_of_music"] = result.words_of_music.split("\\n")
            print(result_music_detail["album_name"])
            return JsonResponse({
                "message": result_music_detail,
                "meta": {
                    "msg": "获取成功",
                    "status": 200
                }
            })


# 获取专辑
def get_xusong_album(request):
    query = request.GET.get("query", "")
    if query == "":
        result_album = []
        try:
            db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                                 charset="utf8")
            cursor = db.cursor()
            sql = "select count(t2.id),t1.image,t1.name,t1.id from testmodel_albuminfo t1,testmodel_musicinfo t2 where t1.id = t2.album_info_id group by t1.id"
            cursor.execute(sql)
            result_tuple = cursor.fetchall()
        except Exception as e:
            return JsonResponse({
                "message": None,
                "meta": {
                    "msg": e,
                    "status": 201
                }
            })
        else:
            for k in range(len(result_tuple)):
                result_album.append({
                    "album_id": result_tuple[k][3],
                    "album_image": "https://ferry1119.com:8000/media/" + result_tuple[k][1],
                    "album_name": result_tuple[k][2],
                    "number_of_songs_on_album": result_tuple[k][0]
                })
            return JsonResponse({
                "message": {
                    "total": len(result_tuple),
                    "album": result_album,
                },
                "meta": {
                    "msg": "获取成功",
                    "status": 200
                }
            })
    elif query != "":
        result_album = []
        try:
            # result = MusicInfo.objects.filter(name__contains=query)
            db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                                 charset="utf8")
            cursor = db.cursor()
            sql = "select count(t2.id),t1.image,t1.name,t1.id from testmodel_albuminfo t1,testmodel_musicinfo t2 where t1.id = t2.album_info_id and t1.name like '%%%s%%' group by t1.id" % query
            cursor.execute(sql)
            result_tuple = cursor.fetchall()
        except Exception as e:
            return JsonResponse({
                "message": None,
                "meta": {
                    "msg": e,
                    "status": 201
                }
            })
        else:
            for k in range(len(result_tuple)):
                result_album.append({
                    "album_id": result_tuple[k][3],
                    "album_image": "https://ferry1119.com:8000/media/" + result_tuple[k][1],
                    "album_name": result_tuple[k][2],
                    "number_of_songs_on_album": result_tuple[k][0],
                })
            return JsonResponse({
                "message": {
                    "total": len(result_tuple),
                    "album": result_album
                },
                "meta": {
                    "msg": "获取成功",
                    "status": 200
                }
            })


# 获取专辑详情
def get_xusong_album_detail(request):
    album_id = request.GET.get("album_id", "")
    result_album_detail = []
    try:
        db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                             charset="utf8")
        cursor = db.cursor()
        sql = "select t2.id,t2.name,t1.name from testmodel_albuminfo t1,testmodel_musicinfo t2 where t1.id = t2.album_info_id and t1.id = " + album_id
        cursor.execute(sql)
        result_tuple = cursor.fetchall()
    except Exception as e:
        return JsonResponse({
            "message": None,
            "meta": {
                "msg": e,
                "status": 201
            }
        })
    else:
        for k in range(len(result_tuple)):
            result_album_detail.append({
                "music_id": result_tuple[k][0],
                "music_name": result_tuple[k][1],
                "album_name": result_tuple[k][2],
            })
        return JsonResponse({
            "message": {
                "total": len(result_tuple),
                "music": result_album_detail
            },
            "meta": {
                "msg": "获取成功",
                "status": 200
            }
        })


# 关于我们
def get_about_us(request):
    return JsonResponse({
        "message": {
            "introduce_title": "介绍",
            "introduce_content": "<div style=\"border-bottom: 1px solid #CCCCCC;padding:5px 0;\">\
                                    <h3>软件开发</h3>\
                                    <p style=\"padding:2px 0;\">Python、HTML、CSS、JS、Vue、Angular、jQuery、小程序</p>\
                                </div>\
                                <div style=\"border-bottom: 1px solid #CCCCCC;padding:5px 0;\">\
                                    <h3>软件测试</h3>\
                                    <p style=\"padding:2px 0;\">功能测试、接口测试、性能测试、自动化测试</p>\
                                </div>"
        },
        "meta": {
            "msg": "获取成功",
            "status": 200
        }
    })


# 上传图片
def upload_photo_file(request):
    if request.method == "POST":
        # 获取文件的二进制内容
        photo_file = request.FILES["my_upload_file"]
        # 获取formData中的photo_description键的值
        photo_file_description = request.POST.get("photo_description")
        # 判断是否有文件
        if not photo_file:
            return JsonResponse({
                "message": None,
                "meta": {
                    "msg": "您没有选择文件进行上传",
                    "status": 201
                }
            })
        current_day = time.strftime("%Y%m%d", time.localtime(time.time()))
        upload_path = os.path.join(settings.BASE_DIR + "/static/media/upload/xusong", current_day)
        if not os.path.exists(upload_path):
            os.mkdir(upload_path)
        short_file_name = photo_file.name.split(".")[-2] + "." + photo_file.name.split(".")[-1]
        # photo_file_abs_path = os.path.join(upload_path, photo_file.name)
        photo_file_abs_path = os.path.join(upload_path, short_file_name)
        try:
            photo_file_path = default_storage.save(photo_file_abs_path, photo_file)
            photo_file_url = "https://ferry1119.com:8000/media/upload/xusong/" + current_day + "/" + \
                             photo_file_path.split("/")[-1]
            db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                                 charset="utf8")
            cursor = db.cursor()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            sql = "INSERT INTO testmodel_photogalleryinfo(name,photo_src,description_of_photo,add_time) VALUES('%s','%s','%s','%s')" % (
                photo_file_path.split("/")[-1], photo_file_url, photo_file_description, current_time)
            print(sql)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            return JsonResponse({
                "message": None,
                "meta": {
                    "msg": "上传失败，错误原因：" + str(e),
                    "status": 202
                }
            })
        else:
            return JsonResponse({
                "message": {
                    "file_url": photo_file_url,
                    "file_name": photo_file_path.split("/")[-1],
                    "file_description": photo_file_description
                },
                "meta": {
                    "msg": "上传成功",
                    "status": 200
                }
            })


# 上传意见反馈
def upload_feedback_file(request):
    if request.method == "POST":
        # 获取文件的二进制内容
        feedback_file = request.FILES["my_upload_file"]
        # 获取formData中的feedback_text键的值
        feedback_text = request.POST.get("feedback_text")
        # 获取formData中的feedback_type键的值
        feedback_type = request.POST.get("feedback_type")
        # 判断是否有文件
        if not feedback_file:
            return JsonResponse({
                "message": None,
                "meta": {
                    "msg": "您没有选择文件进行上传",
                    "status": 201
                }
            })
        current_day = time.strftime("%Y%m%d", time.localtime(time.time()))
        upload_path = os.path.join(settings.BASE_DIR + "/static/media/upload/xusong_feedback", current_day)
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        short_file_name = feedback_file.name.split(".")[-2] + "." + feedback_file.name.split(".")[-1]
        # photo_file_abs_path = os.path.join(upload_path, feedback_file.name)
        photo_file_abs_path = os.path.join(upload_path, short_file_name)
        try:
            photo_file_path = default_storage.save(photo_file_abs_path, feedback_file)
            photo_file_url = "https://ferry1119.com:8000/media/upload/xusong_feedback/" + current_day + "/" + \
                             photo_file_path.split("/")[-1]
            db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                                 charset="utf8")
            cursor = db.cursor()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            sql = "INSERT INTO testmodel_feedbackinfo(name,feedback_type,feedback_photo_src,feedback_text,add_time) VALUES('%s','%s','%s','%s','%s')" % (
                photo_file_path.split("/")[-1], feedback_type, photo_file_url, feedback_text, current_time)
            print(sql)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            return JsonResponse({
                "message": None,
                "meta": {
                    "msg": "上传失败，错误原因：" + str(e),
                    "status": 202
                }
            })
        else:
            return JsonResponse({
                "message": {
                    "file_url": photo_file_url,
                    "file_name": photo_file_path.split("/")[-1],
                    "feedback_type": feedback_type,
                    "feedback_text": feedback_text
                },
                "meta": {
                    "msg": "上传成功",
                    "status": 200
                }
            })


# 获取相册
def get_photo_gallery(request):
    if request.method == "GET":
        query = request.GET.get("query", "")
        if query == "":
            result_photo_detail = []
            try:
                db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                                     charset="utf8")
                cursor = db.cursor()
                sql = "select id,name,photo_src from testmodel_photogalleryinfo"
                cursor.execute(sql)
                result_tuple = cursor.fetchall()
            except Exception as e:
                return JsonResponse({
                    "message": None,
                    "meta": {
                        "msg": "获取失败，错误原因：" + str(e),
                        "status": 201
                    }
                })
            else:
                for k in range(len(result_tuple)):
                    result_photo_detail.append({
                        "photo_id": result_tuple[k][0],
                        "photo_name": result_tuple[k][1],
                        "photo_url": result_tuple[k][2]
                    })
                return JsonResponse({
                    "message": {
                        "total": len(result_tuple),
                        "photo_gallery": result_photo_detail,
                    },
                    "meta": {
                        "msg": "获取成功",
                        "status": 200
                    }
                })
        elif query != "":
            result_photo_detail = []
            try:
                db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                                     charset="utf8")
                cursor = db.cursor()
                sql = "select id,name,photo_src from testmodel_photogalleryinfo where name like '%%%s%%'" % query
                cursor.execute(sql)
                result_tuple = cursor.fetchall()
            except Exception as e:
                return JsonResponse({
                    "message": None,
                    "meta": {
                        "msg": "获取失败，错误原因：" + str(e),
                        "status": 201
                    }
                })
            else:
                for k in range(len(result_tuple)):
                    result_photo_detail.append({
                        "photo_id": result_tuple[k][0],
                        "photo_name": result_tuple[k][1],
                        "photo_url": result_tuple[k][2]
                    })
                return JsonResponse({
                    "message": {
                        "total": len(result_tuple),
                        "photo_gallery": result_photo_detail,
                    },
                    "meta": {
                        "msg": "获取成功",
                        "status": 200
                    }
                })


# 获取图片详情
def get_photo_detail(request):
    if request.method == "GET":
        photo_id = request.GET.get("photo_id")
        try:
            db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="ferry_test",
                                 charset="utf8")
            cursor = db.cursor()
            sql = "select id,name,photo_src,description_of_photo,add_time from testmodel_photogalleryinfo where id = " + photo_id
            cursor.execute(sql)
            result_tuple = cursor.fetchone()
        except Exception as e:
            return JsonResponse({
                "message": None,
                "meta": {
                    "msg": "获取失败，错误原因：" + str(e),
                    "status": 201
                }
            })
        else:
            return JsonResponse({
                "message": {
                    "photo_id": result_tuple[0],
                    "photo_name": result_tuple[1],
                    "photo_url": result_tuple[2],
                    "photo_description": result_tuple[3],
                    "photo_time": result_tuple[4]
                },
                "meta": {
                    "msg": "获取成功",
                    "status": 200
                }
            })
