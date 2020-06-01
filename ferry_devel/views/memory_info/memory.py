#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response


def go_ferry_memory(request):
    #u"我是含有中文字符组成的字符串",作用：后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。
    status_list = [u'-请选择类别-', u'导航栏链接', u'相册标题']
    '''除了在前端JS判断输入框中内容，还可以由后端判断
    if(request.GET):
        select_data = request.GET['category_choice']
        keyboard_data = request.GET['keyboard']
        if(select_data == "-请选择类别-"):
            return u'您还未选择要检索的类别'
        elif(select_data == "导航栏链接"):
            if(keyboard_data == "生日祝福"):
                return render_to_response('birthday_PTY_0301.html',locals())
            elif(keyboard_data == "甜蜜爱情"):
                return render_to_response('the_love_between_lfl_and_pty.html',locals())
            elif(keyboard_data == "联系我"):
                return render_to_response('contact_us.html',locals())
        else:
            if(keyboard_data == "初中"):
                return render_to_response('ferry_memory_chuzhong.html', locals())
            if(keyboard_data == "高中"):
                return render_to_response('ferry_memory_gaozhong.html',locals())
            if(keyboard_data == "大学"):
                return render_to_response('ferry_memory_daxue.html',locals())
    '''
    return render_to_response('ferry_memory.html', locals())






def go_ferry_memory_chuzhong(request):
    return render_to_response('ferry_memory_chuzhong.html',locals())

def go_ferry_memory_gaozhong(request):
    return render_to_response('ferry_memory_gaozhong.html',locals())

def go_ferry_memory_daxue(request):
    return render_to_response('ferry_memory_daxue.html',locals())

def go_ferry_memory_longmenshiku(request):
    return render_to_response('ferry_memory_longmenshiku.html',locals())

def go_ferry_memory_zhujiangxincheng(request):
    return render_to_response('ferry_memory_zhujiangxincheng.html',locals())

def go_ferry_memory_zhongshandaxue(request):
    return render_to_response('ferry_memory_zhongshandaxue.html',locals())

def go_ferry_memory_baiyunshan(request):
    return render_to_response('ferry_memory_baiyunshan.html',locals())

def go_ferry_memory_yuexiushan(request):
    return render_to_response('ferry_memory_yuexiushan.html',locals())

def go_ferry_memory_yuyinshanfang(request):
    return render_to_response('ferry_memory_yuyinshanfang.html',locals())

def go_ferry_memory_hashitate(request):
    return render_to_response('ferry_memory_hashitate.html',locals())

def go_ferry_memory_shamian(request):
    return render_to_response('ferry_memory_shamian.html',locals())

def go_ferry_memory_shangxiajiu(request):
    return render_to_response('ferry_memory_shangxiajiu.html',locals())

def go_ferry_memory_manguyuan(request):
    return render_to_response('ferry_memory_manguyuan.html',locals())

def go_ferry_memory_baishuizhai(request):
    return render_to_response('ferry_memory_baishuizhai.html',locals())

def go_ferry_memory_qimadazhang(request):
    return render_to_response('ferry_memory_qimadazhang.html',locals())

def go_ferry_memory_danzhu(request):
    return render_to_response('ferry_memory_danzhu.html',locals())

def go_ferry_memory_laoyingzhuaxiaoji(request):
    return render_to_response('ferry_memory_laoyingzhuaxiaoji.html',locals())

def go_ferry_memory_fansheng(request):
    return render_to_response('ferry_memory_fansheng.html',locals())

def go_ferry_memory_doujiao(request):
    return render_to_response('ferry_memory_doujiao.html',locals())

def go_ferry_memory_zhuomicang(request):
    return render_to_response('ferry_memory_zhuomicang.html',locals())

def go_ferry_memory_tiaosheng(request):
    return render_to_response('ferry_memory_tiaosheng.html',locals())

def go_ferry_memory_paoshizi(request):
    return render_to_response('ferry_memory_paoshizi.html',locals())

def go_ferry_memory_dashuipiao(request):
    return render_to_response('ferry_memory_dashuipiao.html',locals())

def go_ferry_memory_huaijiuzhangji(request):
    return render_to_response('ferry_memory_huaijiuzhangji.html',locals())

def go_ferry_memory_xiaobawang(request):
    return render_to_response('ferry_memory_xiaobawang.html',locals())

def go_ferry_memory_baolimotuo(request):
    return render_to_response('ferry_memory_baolimotuo.html',locals())

def go_ferry_memory_fankongjingying(request):
    return render_to_response('ferry_memory_fankongjingying.html',locals())

def go_ferry_memory_dixiacheng(request):
    return render_to_response('ferry_memory_dixiacheng.html',locals())

def go_ferry_memory_jipinfeiche(request):
    return render_to_response('ferry_memory_jipinfeiche.html',locals())

def go_ferry_memory_daifanshangxue(request):
    return render_to_response('ferry_memory_daifanshangxue.html',locals())

def go_ferry_memory_fangbianpao(request):
    return render_to_response('ferry_memory_fangbianpao.html',locals())

def go_ferry_memory_qinlao(request):
    return render_to_response('ferry_memory_qinlao.html',locals())