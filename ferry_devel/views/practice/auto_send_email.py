#encoding:utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header


server_host = "smtp.qq.com"
server_port = 25
email_user = "xx@qq.com"
email_password = "xx"
email_send = "xx@qq.com"
email_receiver = "xx@qq.com"

msg = MIMEMultipart()
msg["from"] = Header("robot","utf-8")
msg["to"] = Header("ferry","utf-8")
msg["subject"] = Header("自动发送邮件给ferry","utf-8")

body_content = '''
                <h2>Dear Ferry:</h2>
                <p style="text-indent:2em;font-size:24px;">你辛苦了，请注意身体，该休息了哦！</p>
                '''
message = MIMEText(body_content,"html","utf-8")
msg.attach(message)

file1_path = "E:\\AAA-w1081\\python+unittest+requests自动化框架_罗凡林.zip"
file2_path = "E:\\应用日志测试规范.docx"
att_file1 = MIMEApplication(open(file1_path,"rb").read())
att_file2 = MIMEApplication(open(file2_path,"rb").read())
att_file1.add_header("Content-Disposition","attachment",filename = "接口自动化框架_罗凡林.zip")
att_file2.add_header("Ccontent-Disposition","attachment",filename = "应用日志测试规范.docx")
msg.attach(att_file1)
msg.attach(att_file2)

try:
    s =  smtplib.SMTP()
    s.connect(server_host,server_port)
    s.login(email_user,email_password)
    s.sendmail(email_send,email_receiver,msg.as_string())
    s.quit()
    print("邮件发送成功")
except Exception as e:
    print("邮件发送失败\n",e)