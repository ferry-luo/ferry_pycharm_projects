#encoding:utf-8

from django.http import HttpResponse
from TestModel.models import C21Students,GroupInformation,PrivateInformation

def test_db(request):
    C21Students(ch_name='杨泽杰',salary=15000,sex='男',graduation_school='华南农业大学',age=23,company='某某有限公司').save()
    C21Students(ch_name='舒中华',salary=8700,sex='男',graduation_school='湖南理工大学',age=23,company='蓝月亮（中国）有限公司').save()
    C21Students(ch_name='蔡君',salary=8000,sex='男',graduation_school='湖南理工大学',company='广州滴普科技有限公司').save()
    C21Students(ch_name='刘杰高',salary=9000,sex='男',graduation_school='湖南理工大学',company='广州滴普科技有限公司').save()

    GroupInformation(name='胡明',age=30,email='9778766@qq.com').save()
    GroupInformation(name='杨新明',email='25787766@qq.com').save()
    GroupInformation(name='陈超',age=29,email='766465523@qq.com').save()

    return HttpResponse("<p>数据添加成功</p>")