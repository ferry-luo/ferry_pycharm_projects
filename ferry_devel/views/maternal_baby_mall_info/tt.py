import re


'''
正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。
re.I    使匹配对大小写不敏感
re.M    多行匹配，影响 ^ 和 $
re.U    根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
'''
#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回None。
#备注：当字符串里没有反斜杠， r 可有可无；当字符串里有反斜杠，想要让编译器忽略反斜杠，则要用到r，表示字符串为非转义的原始字符串
if(re.match(u"[\u4e00-\u9fa5]","啊哦",re.I)):
    print("匹配到了")
if(re.match("上衣","好看上衣") == None):
    print("'好看上衣'匹配不到")
if(re.match("上衣","上面的衣服") == None):
    print("'上面的衣服'匹配不到")

#re.search 扫描整个字符串并返回第一个成功的匹配。
if(re.search("上衣","好看上衣，夏天上衣",re.M)):
    print("'好看上衣'可匹配到")
if(re.search("上衣","上面的衣服",re.M) == None):
    print("'上面的衣服'匹配不到")

#re.sub用于替换字符串中的匹配项。
phone = "178-1669-8585"
phone_1 = re.sub(r'\D',"",phone)    #把"-"符号替换成空
print(phone_1)

#re.compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
p = re.compile(r'[a-z]',re.I)
if(p.match("Hello,ferry") != None):
    print("匹配成功，返回一个 Match 对象")

# findall在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次， findall 匹配所有。
result = re.findall("上衣","好看上",re.M)
if(result):
    print(result)
p = re.compile(r'\d+')  #用于匹配至少一个数字
result_1 = p.findall("hello 123 hi 456")
result_2 = p.findall("I have 12 apples and 5 pencils")
print(result_1)
print(result_2)

#finditer和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
p = re.compile(r'\d+')
result_3 = p.finditer("I have 12 apples and 5 pencils")
print(result_3)
for i in result_3:
    print(i.group())

#split 方法按照将字符串分割后返回列表
#\w 匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
#\W用于匹配特殊字符，即非字母、非数字、非汉字、非下划线
p = re.compile(r'\W+')
result_5 = p.split("apple,,,orange,,banana")
print(result_5)

result_6 = re.split(r'\W+',"好看的、合身的、时尚的衣服啊。。。")
result_6 = "".join(result_6)
print(result_6)