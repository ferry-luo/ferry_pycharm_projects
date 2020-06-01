#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from time import sleep
from django.shortcuts import render_to_response


def the_love_between_jie_and_xin(request):
    try:
        love_result = {}
        if request.POST:
            xin_choice = request.POST["choose"]
            if xin_choice == "只想恋爱，不想结婚":
                love_result["say1"] = "好吧，我会继续努力，总有一天，让你愿意与我结婚。"
            if xin_choice == "愿意结婚，相伴一生":
                love_result["say2"] = "哦耶！咱们选个黄道吉日去领证吧~"
            if xin_choice == "我已失望，铁心分手":
                love_result["say3"] = "好吧，我会好好反思。"
            if xin_choice == "不再爱你，心系他人":
                sleep(999)    #后端不做判断，由前端展示被绿的表情图，且让表情图停留999秒
            if xin_choice == "-请选择-":
                return HttpResponse("请作出选择后，再提交")
        return render(request,"the_love_between_jie_and_xin.html",love_result)
    except Exception as e:
        return HttpResponse(e)

def the_love_between_lfl_and_pty(request):
    try:
        result = {}
        if request.POST:
            person_choice = request.POST["choose"]
            if person_choice == "x1":
                sleep(999)
            if person_choice == "x2":
                sleep(999)
        return render(request,"the_love_between_lfl_and_pty.html",result)
    except Exception as e:
        return HttpResponse(e)
