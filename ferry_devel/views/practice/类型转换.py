#encoding:utf-8

#Python字典、列表、字符串之间的转换
#1.列表与字符串转换
#列表转字符串：
x = ['a','b','c']
s = ''.join(x)
print(str(x))
print(s)
#字符串转列表：
s = "['a','b','c']"
x = eval(s) #eval()函数用来执行一个字符串表达式，并返回表达式的值。
print(x)
#2.列表与字典转换
#两个列表转成字典
x1 = ['a','b','c']
x2 = [1,2,3]
x3 = zip(x1,x2) #zip返回 打包为元组的列表，如[('a',1),('b',2),('c',3)]
print(x3)
d = dict(zip(x1,x2))
print(d)
#字典中键、值转为列表
d = {'a':1,'b':2}
l1 = list(d.keys())
l2 = list(d.values())
print(d.keys())
print(d.values())
print(l1)
print(l2)
#3.字典与字符串转换
#字符串转字典：用eval
s = "{'dateUpdated':20181111}"
d = eval(s) #eval()函数用来执行一个字符串表达式，并返回表达式的值。
print(d)
#字典转字符串：用str
datas = {"dateUpdated":20181111}
s = str(datas)  #str()函数返回一个对象的string格式。
print(s)

#eval() 函数用来执行一个字符串表达式，并返回表达式的值。
a = 7
print(eval('3 * a'))
#join函数 语法：'sep'.join(seq)  以sep作为分隔符，将seq所有的元素合并成一个新的字符串
#sep：分隔符，可以为空
#seq:要连接的元素序列、字符串、元组、列表
