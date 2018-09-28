#! -*- coding:UTF-8 -*-
#XB 18/05
"""
1.截取原始数据中需要的位数，比如设备ID一般是7位，我们从末尾往前推移7位截取就获得想要的设备ID
"""

NEED_BITS=7
input_list=[]

with open ('input.txt','r') as f:
    for myline in f:
        if len(myline) < NEED_BITS:
            myline='NA'
        myline.replace(' ', '')    #去掉字符串中间的空格
        myline.strip()    #去掉行首行末的空格
        #id_line=id_line[-8:]
        #myline=myline[0:19]
        myline=myline[-8:] #末尾往前推移7位截取，获得想要的设备ID
        with open('output.txt','a') as fwrite:
            fwrite.writelines(myline)
            #fwrite.writelines(myline+'\n')
print ('Success\n')
        
        
