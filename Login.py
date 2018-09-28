# -*- coding:UTF-8 -*-

'''
LogRead OS2000-40 Lander
DesignBy:XB
2017.03
'''

import paramiko
import os
from Tkinter import *

ip=raw_input("Device IP:")
username=raw_input("Username:")
pwd=raw_input("Password:")

def ReadCmdlist():
    print "The Device IP=%s"%ip
    if os.path.exists("cmdlist.txt"):
        print "Find cmdlist.txt.\n"
    else:
        print "Didn't Find cmdlist.txt Create It.\n"
        create=open("cmdlist.txt",'w')
        create.close()

ReadCmdlist()

def scanbody(ip,username,pwd,cmd):
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,pwd)
        stdin,stdout,stderr=ssh.exec_command(cmd)
        cmdoutput=stdout.readlines()
        ssh.close()

        cmdout=[]
        for output in cmdoutput:
            cmdout.append(output)
            print output

    except paramiko.AuthenticationException,e:
        print 'Error'
        print 'Error Detail',e

def Start():
    cmds=[]
    read=file("cmdlist.txt","r")
    for line in read.readlines():
        cmds.append(line)
    for i in cmds:
        i=i.strip("\n")    #去掉行末换行符
        cmd=i
        print "\nCurrent CMD:\n%s"%i
        print "Command Execution Results:"
        scanbody(ip,username,pwd,cmd)
    print "AllDone@LogRead2017"

#GUI
root=Tk()
root.title("LogRead OS2000 Lander")
root.geometry('380x380')    #设置窗口大小
root.resizable(width=False,height=False)    #设置窗口是否可以变化长宽，此处宽高不可变；

notice1=Label(root,text="Please Input CMD One Per Line. ",fg='red')
notice1.pack(side=TOP)
#滚动条
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.set(1,5)

#获取文件内容
content=file("cmdlist.txt","r")
readtext=content.read()
content.close()

#写入到文件
cmd_list=Text(root,width=35,height=22,yscrollcommand=scrollbar.set)
cmd_list.place(x=5,y=80)
cmd_list.insert(END,readtext)
scrollbar.config(command=cmd_list.yview)

#保存函数
def Save():
    save=cmd_list.get('0.0',END).strip()
    print "The following command to be saved."
    print save
    file_object=open("cmdlist.txt.","w")
    file_object.writelines(save)
    file_object.close()
#保存和扫描按钮
save_button=Button(root,text="SAVE",width=9,height=2,command=Save).place(x=260,y=80)
scan_button=Button(root,text="START",width=9,height=2,command=Start).place(x=260,y=150)

root.mainloop()
