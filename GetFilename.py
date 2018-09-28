#! -*- coding:UTF-8 -*-
# Author="XB"

import os
 
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):    #判断路径是否为文件
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):    #判断路径是否为目录
        for s in os.listdir(dir):    #使用os.listdir()函数来获得目录中内容
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)    #os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径
            GetFileList(newDir, fileList)  
    return fileList
 
if __name__=='__main__':
    '''path=raw_input('Enter The Path(Like:D:\\Test):')'''
    list = GetFileList(os.getcwd(), [])
    f=open(os.getcwd()+".txt",'w')
    for i in list:
        f.write(i)
        f.write('\n')
        print i
    f.close()
    raw_input('Press Anykey To Exit:')
