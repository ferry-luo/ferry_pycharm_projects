import xlwt
import datetime
from io import BytesIO
import requests

def export_excel(request):
    # 获取当前时间
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # 创建一个workbook,设置编码格式为utf8
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个 worksheet
    worksheet = workbook.add_sheet('Worksheet')
    # 将处理好的数据写入excel，其中i为行，j为列
    for i in range(len(msg_list)):
        for j in range(len(msg_list[i])):
            worksheet.write(i, j, msg_list[i][j])
    # 创建操作二进制数据的对象
    output = BytesIO()
    # 将excel数据写入到内存中
    workbook.save(output)
    # 设置文件读取的偏移量，0表示从头读起
    output.seek(0)
    # 设置HTTP的报头为二进制流
    request.set_header("Content-Type", "application/octet-stream")
    # 设置文件名
    request.set_header("Content-Disposition", "attachment; filename=export-%s.xls" % nowtime)
    return request.write(output.getvalue())


