#encoding:utf-8
import hashlib
import time

m = hashlib.md5()
m.update(b'888888') #update(arg)传入arg对象来更新hash的对象。必须注意的是，该方法只接受byte类型，否则会报错。这就是要在参数前添加b来转换类型的原因。
md5_password = m.hexdigest()
print(md5_password)

passwd = '888888'
md5_passwd = hashlib.md5(passwd.encode(encoding='utf-8')).hexdigest()
print(md5_passwd)

local_time = time.localtime()
current_time = time.strftime("%Y%m%d%H",local_time)
print(current_time)
username = 'ADM0603'
sign = username + md5_passwd + current_time
md5_sign = hashlib.md5(sign.encode(encoding='utf-8')).hexdigest()
print(md5_sign)

l_time = time.localtime()
c_time = time.strftime("%Y%m%d%H",l_time)
my_sign = username + md5_passwd + c_time
md5_my_sign = hashlib.md5(my_sign.encode(encoding='utf-8')).hexdigest()
print(md5_my_sign)