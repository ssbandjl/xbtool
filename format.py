##!/usr/bin/env python
# _*_ coding: utf-8 _*_
#XB 18/05



with open ('input.txt','r') as file1:
  for myline in file1:
    #print dev_sn=dict['sn'],
    myline=myline.strip('\n')
    myprint=myline+'=dict['+"'"+myline+"'"+']'+','
    print myprint,


#\"dev_day2_video_num\":\"${dev_day2_video_num}\",\
with open ('input.txt','r') as file1:
  for myline in file1:
    myline=myline.strip('\n')
    myprint='\\"'+myline+'\\":\\"${'+myline+'}\\",\\'
    print myprint



