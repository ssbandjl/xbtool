#! -*- coding:UTF-8 -*-
#Powered By XB 2017/5

import xlrd
workbook_out = xlrd.open_workbook(u'output.xls')
sheet_names_out= workbook_out.sheet_names()
workbook_in = xlrd.open_workbook(u'input.xlsx')
sheet_names_in= workbook_in.sheet_names()

for sheet_name in sheet_names_out:
    sheet2 = workbook_out.sheet_by_name(sheet_name)
    for i in range(0,20000):
        rows = sheet2.row_values(i)
        for sheet_name2 in sheet_names_in:
            sheet3 = workbook_in.sheet_by_name(sheet_name2)
            for j in range(0,20000):
                datas = sheet3.row_values(j)
                if rows[2] in datas:
                    print rows[1],rows[2],datas[5]
