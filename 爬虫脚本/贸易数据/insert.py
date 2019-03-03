import xlrd
import xlwt
from xlutils.copy import copy

def read_excel_xls(path):
    title = []
    res = []
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(1, worksheet.nrows): # 从第二行开始读取
        for j in range(0, worksheet.ncols):
            title.append(worksheet.cell_value(i, j))# 逐行逐列读取数据
        res.append(title)
        title = []
    return res

def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    print(rows_old)
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i+rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save('./1.csv')  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")

res_1 = read_excel_xls('./2.csv')
write_excel_xls_append('./1.csv', res_1)


