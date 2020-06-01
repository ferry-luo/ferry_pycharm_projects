#encoding:utf-8
from django.http import response

print("亲，请问可以获取您的身份信息吗？可以的话，请输入Y或y")
a = input("可不可以？")
i = 3
confirm = 0
while(i == 3):
    if(a == 'Y' or a == 'y'):
        print("好的，谢谢亲。")
        confirm = 1
        break
    else:
        while(i == 3):
            print("别这么快拒绝嘛，有奖励的哦！")
            a = input("可不可以？")
            i -= 1
        if(a == 'Y' or a == 'y'):
                print("好的，谢谢亲。")
                confirm = 1
                break
        while(i == 2):
            print("再考虑一下，以后定期给您发奖励哦！")
            a = input("可不可以？")
            i -= 1
        if(a == 'Y' or a == 'y'):
            print("好的，谢谢亲。")
            confirm = 1
            break
        while(i == 1):
            print("我们定期发奖励，绝不食言，您放心好了。请再考虑一下！")
            a = input("可不可以？")
            i -= 1
        if(a == 'Y' or a == 'y'):
            print("好的，谢谢亲。")
            confirm = 1
            break
    if(confirm == 0 and i == 0):
        print("好吧，我不会再打扰亲了。")