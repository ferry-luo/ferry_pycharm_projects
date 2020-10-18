# encoding:utf-8
import xlrd


# 函数的第一个参数为文件的绝对路径，第二个参数为需要第几个数据（如：第二个参数是1时，返回的是表格中第1列的第2个值。是0时，返回第一列的表头）
def read_excel(filename, seq):
    work_excel = xlrd.open_workbook(filename)
    sheet_data = work_excel.sheet_by_name("Sheet1")
    '''获取除表头以外的所有值：2行1列，2行2列，……，3行1列，3行2列，……
    for i in range(1,sheet_data.nrows):
        for j in range(0,sheet_data.ncols):
            data = sheet_data.cell_value(i,j)
            #print(type(data))
            d = [data]  #把data放入一个列表
            #print(type(d))
            print(d)
    '''
    col1 = sheet_data.col_values(0)  # 参数化文件中第1列为所需，则获取第1列的值
    a = []
    # extend方法，在已存在的列表中添加新的列表内容
    a.extend(col1)
    # print(a[1:len(a)])
    # print(a[seq])
    nrows_num = sheet_data.nrows
    if seq == 0 or seq >= nrows_num:
        print("输入的第2个参数不在合理范围：获取到表头或是超出行数")
    elif seq >= 1 and seq < nrows_num:
        return a[seq]

# read_excel(r"E:\AAA-w1081\接口自动化测试所用数据表格\查询优惠商户更新数据-日期参数.xlsx",4)
