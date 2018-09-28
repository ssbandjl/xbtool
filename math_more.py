##!/usr/bin/env python
# _*_ coding: utf-8 _*_
#XB 18/05

list_excel=[]
list_input=[]
dir_excel={}
match_num=0

with open ('excel.txt','r',) as file1:
  for myline in file1:
    (mykey,myvalue)=myline.split('\t')
    dir_excel[mykey]=myvalue[:-1]

#open()函数有个参数newline，当写入的时候，如果没有newline参数的话，在windows这种使用'\r\n'的系统中，会自动在行尾加上\r，然后写入的时候就会空一行。
with open ('output.txt','wb') as file3:
  with open ('input.txt','r') as file2:
    for myline in file2:
      myline=myline.strip('\n')
      if len(myline) == 0:
        myline='NA'
      if myline in dir_excel.keys(): #input match excel success
        match_num = match_num + 1
        mydata=myline+'\t'+dir_excel[myline]
      else: #Not in
        mydata = myline + '\t' + 'NA'
      file3.writelines(mydata+'\n')
print ('Total Match:%s\n') % match_num



