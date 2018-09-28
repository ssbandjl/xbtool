#! -*- coding:UTF-8 -*-
#XB 18/09

import xlrd
workbook1 = xlrd.open_workbook(u'output.xls') #打开表格1
sheet_names1= workbook1.sheet_names() #获取表格1的所有工作表
workbook2 = xlrd.open_workbook(u'input.xlsx') #打开表格2
sheet_names2= workbook2.sheet_names() #获取表格2的所有工作表

with open('Output.txt', 'w') as fileout:
    for sheet_name1 in sheet_names1: #遍历表格1的工作表
        sheet1 = workbook1.sheet_by_name(sheet_name1)
        for i in range(0,20000):
            rows1 = sheet1.row_values(i)
            for sheet_name2 in sheet_names2:
                sheet2 = workbook2.sheet_by_name(sheet_name2)
                for j in range(0,20000):
                    #print j
                    rows2 = sheet2.row_values(j)
                    if rows1[2] in rows2:
                        print (i,rows1[1],rows1[2],rows2[5])
                        myline=str(i)+','+str(rows1[1])+','+str(rows1[2])+','+str(rows2[5])
                        fileout.writelines(myline)
