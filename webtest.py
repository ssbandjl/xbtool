#!usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username='admin'
password='hm.com@2016'

class web_chrome:
    browser=None
    loopFunc=None
    
    def __init__(self,work):
        print 'Init webdriver....'
        chromedriver = "C:\Python27\chromedriver-Windows"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.browser = webdriver.Chrome(chromedriver)
        self.loopFunc = work;
        
    def open(self,url):
        print 'Open web url: '+url
        self.browser.get(url)
        
    def loop(self):
        self.loopFunc(self.browser)
        
    def close(self):
        self.browser.quit();


def web_loop(browser):
    type = sys.getfilesystemencoding()
    
    print('运行测试程序'.decode('utf-8').encode(type))

    try:
        browser.find_element_by_name('username').clear()
        browser.find_element_by_name('username').send_keys(username)

        browser.find_element_by_name('password').clear()
        browser.find_element_by_name("password").send_keys(password)
        browser.find_element_by_name("submit").click()
        print('登陆成功'.decode('utf-8').encode(type))
    except Exception as e:
        print ('登陆失败'.decode('utf-8').encode(type), format(e))
        
    time.sleep(3)
    print('点击手工上线'.decode('utf-8').encode(type))
    browser.find_element_by_partial_link_text("网络").click()
    browser.find_element_by_partial_link_text("手工上线").click()

    print('修改手工上线配置'.decode('utf-8').encode(type))
    browser.find_element_by_name("cbid.system.system.e3g_phone").clear()
    browser.find_element_by_name("cbid.system.system.e3g_phone").send_keys("222222222")
    browser.find_element_by_id("cbid.system.system.srcdev").find_element_by_xpath("//option[@value='wwan1']").click()
    browser.find_element_by_name("submit").click()

    print('点击LAN接口'.decode('utf-8').encode(type))
    browser.find_element_by_partial_link_text("网络").click()
    browser.find_element_by_partial_link_text("LAN接口").click()
    time.sleep(3)

    print('点击DHCP设置'.decode('utf-8').encode(type))
    browser.find_element_by_partial_link_text("服务").click()
    browser.find_element_by_partial_link_text("DHCP设置").click()
    time.sleep(3)
    
    print('点击带宽管理'.decode('utf-8').encode(type))
    browser.find_element_by_partial_link_text("QOS").click()
    browser.find_element_by_partial_link_text("带宽管理").click()
    time.sleep(3)

    print('点击路由信息'.decode('utf-8').encode(type))
    browser.find_element_by_link_text("状态").click()
    browser.find_element_by_link_text("路由信息").click()
    
    time.sleep(3)

    print('即将退出程序!!!'.decode('utf-8').encode(type))
    
    return 0

def main():
    type = sys.getfilesystemencoding()
    web_browser = web_chrome(web_loop)
    web_browser.open('http://192.168.10.1:8080');
    print('打开Chrome成功'.decode('utf-8').encode(type))

    web_browser.loop()

    time.sleep(3)
    web_browser.close()   
    
if __name__ == "__main__":
    main();

