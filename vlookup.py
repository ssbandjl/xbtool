##!/usr/bin/env python
# _*_ coding: utf-8 _*_
#XB 17/10

import csv

list_myline=[]
list_csv=[]
sn_uptime={}

with open ('input.csv','r',) as f1:
  for csv_line in f1:
    #delete windows '\n'
    list_csv.append(csv_line.strip('\n'))

#create dictionaries(key=sn,value=sysup_time)
with open ('input.txt','r') as f2:
  for sys_line in f2:
    list_myline=sys_line.split("\n")
    #list_myline[1]=list_myline[1].strip('\n')    #删除第二列的换行符
    #print list_myline
    done_flag='OK'
    (key,value)=(list_myline[0],done_flag)
    sn_uptime[key]=value

#open()函数有个参数newline，当写入的时候，如果没有newline参数的话，在windows这种使用'\r\n'的系统中，会自动在行尾加上\r，然后写入的时候就会空一行。
with open ('output.csv','wb') as f3:
  writer = csv.writer(f3)
  for csv_sn in list_csv:
    if csv_sn in sn_uptime:
      DATA=(csv_sn,sn_uptime[csv_sn])
      writer.writerow(DATA)
    else:
      DATA=(csv_sn,'','')
      writer.writerow(DATA)

a=raw_input("Success Any Key To Exit \n")

