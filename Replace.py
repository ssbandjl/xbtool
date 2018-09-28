#! -*- coding:UTF-8 -*-
#Powered By XB 2017/5

import os
f= open('Input.txt', 'r')

#读取文件
rf=f.read()
#rf=f.read().decode('UTF-8')


f= open('Output.txt', 'w')

#逗号转换为回车
#f.write(rf.replace('，','\n'))

#回车换成逗号
f.write(rf.replace('\n',','))

#去掉空格
#f.write(rf.replace(' ',''))

#逗号换回车
#f.write(rf.replace(',','\n'))

#分号换行
#f.write(rf.replace(';','\n'))
#f.write(rf.replace('\n',';'))
f.close()
