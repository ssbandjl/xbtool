python 记录日志logging

在项目开发中，往往要记录日志文件。用python记录日志有两种方式：

　　1、利用python 自带的logging库，例如：

复制代码
　# -*- coding: utf-8 -*-

import os
import codecs
import datetime

import logging

#封装logging日志
class LogFile:
    #构造函数 fileName：文件名
    def __init__(self,fileName,level=logging.INFO):
        fh = logging.FileHandler(fileName)
        self.logger = logging.getLogger()
        self.logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s : %(message)s','%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def WriteLog(self,message):
        self.logger.info(message)

    def WriteErrorLog(self,message):
        self.logger.setLevel(logging.ERROR)
        self.logger.error(message)
复制代码


2、自己写日志
　　
复制代码
class LogFile:
    def __init__(self,fileName):
        self.fileName = os.path.join(os.getcwd(), fileName)
    def WriteLog(self,message):
        strMessage = '\r\n%s: %s' % (time.strftime('%Y-%m-%d_%H-%M-%S'), message)
        with open(self.fileName, 'a') as f:
            f.write(strMessage)
log = LogFile(time.strftime('%Y-%m-%d') + '.txt')
log.WriteLog('aaa')
