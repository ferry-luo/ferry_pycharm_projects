#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def go_get_entertainment(request):
    try:
        result = {}
        if request.POST:
            person_choice = request.POST["choice"]
            if person_choice == "看黄片":
                result['c'] = "请点击'黄色视频'那个超链接，开始快乐起来。"
            if person_choice == "找乔碧萝":
                result['c'] = "请点击'斗鱼直播'那个超链接，开始快乐起来。"
            if person_choice == "玩亚索":
                result['c'] = "请点击'英雄联盟'那个超链接，开始快乐起来。"
            if person_choice == "-请选择-":
                return HttpResponse("请作出选择后再查看！")
        return render(request,"get_entertainment.html",result)
    except Exception as e:
        return HttpResponse(e)
