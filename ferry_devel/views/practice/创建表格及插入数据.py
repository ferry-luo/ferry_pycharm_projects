import datetime
import xlsxwriter
from excel_response3 import ExcelResponse

# 获取当前时间
now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
# 建立文件
workbook = xlsxwriter.Workbook("event" + now + ".xlsx")
# 建立sheet
worksheet = workbook.add_worksheet("event_sheet")
# 写入
worksheet.write(0, 0, "发布会名称")
worksheet.write(0, 1, "发布会限制人数")
worksheet.write(0, 2, "发布会地址")
worksheet.write(0, 3, "发布会开始时间")
worksheet.write(1, 0, "小米")
worksheet.write(1, 1, 2000)
worksheet.write(1, 2, "西街74")
worksheet.write(1, 3, "2020-05-25 14:00")
workbook.close()
