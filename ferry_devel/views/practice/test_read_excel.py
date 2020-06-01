#encoding:utf-8
import xlrd

def read_excel():
    work_excel = xlrd.open_workbook(r"E:\AAA-w1081\班级测试数据.xls")
    sheet_name = work_excel.sheet_names()   #获取文件中所有表格
    print(sheet_name)
    sheet_data = work_excel.sheet_by_name("Sheet1")
    print(sheet_data.name,sheet_data.nrows,sheet_data.ncols)    #获取Sheet1这个表格的名字、行数、列数
    row1 = sheet_data.row_values(0) #获取Sheet1这个表格的第1行内容
    row2 = sheet_data.row_values(1) #获取Sheet1这个表格的第2行内容
    col1 = sheet_data.col_values(0) #获取Sheet1这个表格的第1列内容
    col2 = sheet_data.col_values(1) #获取Sheet1这个表格的第2列内容
    print(row1)
    print(row2)
    print(col1)
    print(col2)
    #获取单元格内容的三种方法   附：encode()用于字符串编码，decode()方法用于字符串解码。如果一个数据是用gbk解码，那么用utf-8编码回去就会报错；用utf-8解码，gbk编码回去就会报错
    data21_1 = sheet_data.cell_value(1,1).encode("gbk")
    data21_2 = sheet_data.cell(1,1).value.encode("utf-8")
    data21_3 = sheet_data.row(1)[1].value
    print(data21_3)
    data22_type = sheet_data.cell(1,1).ctype
    print(data22_type)

if __name__ == "__main__":
    read_excel()