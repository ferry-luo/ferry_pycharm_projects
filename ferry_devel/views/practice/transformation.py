#encoding:utf-8

#Python字典、列表、字符串之间的转换
#1.列表与字符串转换
#列表转字符串：
x = ['a','b','c']
s = ''.join(x)
print(s)
#字符串转列表：
s = "['a','b','c']"
x = eval(s)
print(x)
#2.列表与字典转换
#两个列表转成字典
x1 = ['a','b','c']
x2 = [1,2,3]
zip(x1,x2)
d = dict(zip(x1,x2))
print(d)
#字典中键、值转为列表
d = {'a':1,'b':2}
l1 = list(d.keys())
l2 = list(d.values())
print(l1)
print(l2)
#3.字典与字符串转换
#字符串转字典：用eval
s = "{'dateUpdated':20181111}"
d = eval(s)
print(d)
#字典转字符串：用str
datas = {"dateUpdated":20181111}
s = str(datas)
print(s)
