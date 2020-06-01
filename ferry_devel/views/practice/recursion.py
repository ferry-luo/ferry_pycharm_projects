#encoding:utf-8
from time import sleep
#递归
def recursion(x):
    if x/2 > 1:
        print(x/2)
        repeat = recursion(x/2)
        sleep(1)
        print("返回值：",repeat)
    return x
recursion(10)

#判断数据在列表的左边还是右边
def twosplit(source_data,find_data):
    half_length = int(len(source_data)/2)
    if find_data in source_data[:half_length]:
        print("数据在左边的：%s"%source_data[:half_length])
    elif find_data in source_data[half_length:]:
        print("数据在右边的：%s"%source_data[half_length:])
    else:
        print("找不到数据")

d_list = ["小明","小红","小燕","小华","小刚"]
twosplit(d_list,"小华")

#斐波那契数列
def fb_series(arg1,arg2,stop):
    arg3 = arg1 + arg2
    print(arg1,arg2,arg3)
    if arg3 < stop:
        fb_series(arg2,arg3,stop)
fb_series(0,1,60)

#用普通for循环列出数据及下标
l = ["a","b","c","d"]
i = 0
for e in l:
    print(i,l[i])
    i += 1
#for循环使用enumerate()方法，enumerate将一个可遍历的数据对象（列表、元祖、字符串等）组合成一个索引序列，同时列出数据的下表及数据
d = ["a","b","c","d"]
for i,element in enumerate(d):
    print(i,element)

d1 = [["001","002","003"],["学号1","学号2","学号3"],["小明","小红","小燕"],[5000,6000,5500]]
print(d1)
for i,element in enumerate(d1):
    #print(i,element)
    for j in range(i,len(element)):
        print(len(element))
        print(d1[i][j])