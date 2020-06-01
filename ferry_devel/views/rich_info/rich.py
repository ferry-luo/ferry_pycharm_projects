#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def go_get_rich(request):
    try:
        rich_result = {}
        if request.POST:
            jie_choice = request.POST['choice']
            if jie_choice == "找富婆":
                rich_result['c'] = "马上即可致富"
            if jie_choice == "编程":
                rich_result['c'] = "35岁方能致富"
            if jie_choice == "其他":
                rich_result['c'] = "55岁方能致富"
            if jie_choice == "-请选择-":
                return HttpResponse("请作出选择后，再点查看")
        return render(request,"get_rich.html",rich_result)
    except Exception as e:
        return HttpResponse(e)