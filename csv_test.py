##!/usr/bin/env python
# _*_ coding: utf-8 _*_
#XB 17/9

import csv
from distutils.log import warn as printf

#DATA=(
#    (9,'Web Clinets and Servers','base64,urllib'),
#    (10,'Web Programming:CGI & WSGI','cgi,time,wsgiref'),
#    (13,'Web Services','urllib,twython'),
#)
#
##open()函数有个参数newline，当写入的时候，如果没有newline参数的话，在windows这种使用'\r\n'的系统中，会自动在行尾加上\r，然后写入的时候就会空一行。
#f = open('csv.csv','wb')
#writer=csv.writer(f)
#for record in DATA:
#    writer.writerow(record)
#f.close()
#
#printf ('*** REVIEW OF SAVED DATA')
#f=open('bookdata.csv','rb')
#reader=csv.reader(f)
#for chap,title,modpkgs in reader:
#    printf('Chapter %s: %r (featuring %s)' % (chap,title,modpkgs))
#f.close()


with open ('sysupgrade.txt','r') as f:
    for myline in f:
        




