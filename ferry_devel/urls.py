# encoding:utf-8
from django.conf.urls import url
from django.urls import path

from ferry_devel.views.api_info import vue_ajax_get
from ferry_devel.views.api_info import vue_ajax_post
from ferry_devel.views.api_info import event

from ferry_devel.views.maternal_baby_mall_info import shopping_cart
from ferry_devel.views.maternal_baby_mall_info import login_and_register
from ferry_devel.views.maternal_baby_mall_info import about_us
from ferry_devel.views.maternal_baby_mall_info import all_commodity
from ferry_devel.views.maternal_baby_mall_info import buy_today
from ferry_devel.views.maternal_baby_mall_info import commodity_details
from ferry_devel.views.maternal_baby_mall_info import information
from ferry_devel.views.maternal_baby_mall_info import mall_search
from ferry_devel.views.confession_info import confession
from ferry_devel.views.practice import search_sth
from ferry_devel.views.practice import test_db
from ferry_devel.views.practice import view
from ferry_devel.views.birthday_info import birthday
from ferry_devel.views.yellow_info import yellow
from ferry_devel.views.programmer_info import programmer
from ferry_devel.views.shop_info import shop
from ferry_devel.views.rich_info import rich
from ferry_devel.views.eternal_love_info import eternal_love
from ferry_devel.views.memory_info import memory
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^$', view.index),

    url(r'^go_vue_ajax_handle_get$', vue_ajax_get.get_event_handle),
    url(r'^go_vue_ajax_handle_post$', vue_ajax_post.get_event_handle),

    url(r'^add_event$', event.add_event),
    url(r'^get_event$', event.get_event),
    url(r'^add_event_handle$', event.add_event_handle),
    url(r'^get_event_handle$', event.get_event_handle),
    url(r'^delete_event$', event.delete_event),
    url(r'^export_event$', event.export_event),
    url(r'^import_event$', event.import_event),

    url(r'^register$', login_and_register.register),
    url(r'^login$', login_and_register.login),
    url(r'^register_handle', login_and_register.register_handle),
    url(r'^index$', login_and_register.login_handle),
    url(r'^logout$', login_and_register.logout),
    url(r'^shopping_cart$', shopping_cart.shopping_cart),
    url(r'^about_us$', about_us.about_us),
    url(r'^all_commodity$', all_commodity.all_commodity),
    url(r'^commodity_details$', commodity_details.commodity_details),
    url(r'^buy_today$', buy_today.buy_today),
    url(r'^information$', information.information),
    url(r'^mall_search$', mall_search.mall_search),
    path('hello/', view.hello),
    path('introduce/', view.introduce),
    url(r'^see_loading$', view.see_loading),
    url(r'^testdb$', test_db.test_db),
    url(r'^search_form$', search_sth.search_form),
    url(r'^search$', search_sth.search),
    url(r'^search_post$', search_sth.search_post),
    url(r'^image$', view.see_image),
    url(r'^love_PTY$', confession.confession_to_PTY),
    url(r'^TingyunPeng_0301$', birthday.go_birthday_PTY_0301),
    url(r'^happy$', yellow.go_yellow_happy),
    url(r'^amusement$', yellow.go_yellow_amusement),
    url(r'^contact_us$', yellow.go_contact_us),
    url(r'^ProgrammerFestival$', programmer.go_programmer_festival),
    url(r'^discount_shopping$', shop.go_shopping),
    url(r'^go_get_rich$', rich.go_get_rich),
    url(r'^the_love_between_jie_and_xin$', eternal_love.the_love_between_jie_and_xin),
    url(r'^the_love_between_lfl_and_pty$', eternal_love.the_love_between_lfl_and_pty),
    url(r'^see_img_float$', view.see_img_float),
    url(r'^see_img_tupianpinhe$', view.see_img_splicing),
    url(r'^go_yellow_website$', yellow.go_yellow_website),
    url(r'^go_ferry_memory$', memory.go_ferry_memory),
    url(r'^go_ferry_memory_chuzhong$', memory.go_ferry_memory_chuzhong),
    url(r'^go_ferry_memory_gaozhong$', memory.go_ferry_memory_gaozhong),
    url(r'^go_ferry_memory_daxue$', memory.go_ferry_memory_daxue),
    url(r'^go_ferry_memory_longmenshiku$', memory.go_ferry_memory_longmenshiku),
    url(r'^go_ferry_memory_zhujiangxincheng$', memory.go_ferry_memory_zhujiangxincheng),
    url(r'^go_ferry_memory_zhongshandaxue$', memory.go_ferry_memory_zhongshandaxue),
    url(r'^go_ferry_memory_baiyunshan$', memory.go_ferry_memory_baiyunshan),
    url(r'^go_ferry_memory_yuexiushan$', memory.go_ferry_memory_yuexiushan),
    url(r'^go_ferry_memory_yuyinshanfang$', memory.go_ferry_memory_yuyinshanfang),
    url(r'^go_ferry_memory_hashitate$', memory.go_ferry_memory_hashitate),
    url(r'^go_ferry_memory_shamian$', memory.go_ferry_memory_shamian),
    url(r'^go_ferry_memory_shangxiajiu$', memory.go_ferry_memory_shangxiajiu),
    url(r'^go_ferry_memory_manguyuan$', memory.go_ferry_memory_manguyuan),
    url(r'^go_ferry_memory_baishuizhai$', memory.go_ferry_memory_baishuizhai),
    url(r'^go_ferry_memory_qimadazhang$', memory.go_ferry_memory_qimadazhang),
    url(r'^go_ferry_memory_danzhu$', memory.go_ferry_memory_danzhu),
    url(r'^go_ferry_memory_laoyingzhuaxiaoji$', memory.go_ferry_memory_laoyingzhuaxiaoji),
    url(r'^go_ferry_memory_fansheng$', memory.go_ferry_memory_fansheng),
    url(r'^go_ferry_memory_doujiao$', memory.go_ferry_memory_doujiao),
    url(r'^go_ferry_memory_zhuomicang$', memory.go_ferry_memory_zhuomicang),
    url(r'^go_ferry_memory_tiaosheng$', memory.go_ferry_memory_tiaosheng),
    url(r'^go_ferry_memory_paoshizi$', memory.go_ferry_memory_paoshizi),
    url(r'^go_ferry_memory_dashuipiao$', memory.go_ferry_memory_dashuipiao),
    url(r'^go_ferry_memory_xiaobawang$', memory.go_ferry_memory_xiaobawang),
    url(r'^go_ferry_memory_huaijiuzhangji$', memory.go_ferry_memory_huaijiuzhangji),
    url(r'^go_ferry_memory_baolimotuo$', memory.go_ferry_memory_baolimotuo),
    url(r'^go_ferry_memory_fankongjingying$', memory.go_ferry_memory_fankongjingying),
    url(r'^go_ferry_memory_dixiacheng$', memory.go_ferry_memory_dixiacheng),
    url(r'^go_ferry_memory_jipinfeiche$', memory.go_ferry_memory_jipinfeiche),
    url(r'^go_ferry_memory_daifanshangxue$', memory.go_ferry_memory_daifanshangxue),
    url(r'^go_ferry_memory_fangbianpao$', memory.go_ferry_memory_fangbianpao),
    url(r'^go_ferry_memory_qinlao$', memory.go_ferry_memory_qinlao),
]
# 设置静态文件路径
urlpatterns += staticfiles_urlpatterns()

'''
Django path() 可以接收四个参数，分别是两个必选参数：route、view 和两个可选参数：kwargs、name。

语法格式：
path(route, view, kwargs=None, name=None)
route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。

view: 用于执行与正则表达式匹配的 URL 请求。

kwargs: 视图使用的字典类型的参数。

name: 用来反向获取 URL。
'''
