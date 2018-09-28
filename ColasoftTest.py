# -*- coding:UTF-8 -*-
from selenium import webdriver
import time

profile = webdriver.FirefoxProfile(r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\8j02fw1d.firefox_webdriver')
browser = webdriver.Firefox(profile)
browser.get('https://192.168.5.197')
while True: 

    #登陆
    browser.find_element_by_xpath(".//*[@id='loginForm']/div[2]/div/table/tbody/tr[1]/td[2]/input").clear()
    browser.find_element_by_xpath(".//*[@id='loginForm']/div[2]/div/table/tbody/tr[1]/td[2]/input").send_keys('admin')
    browser.find_element_by_xpath(".//*[@id='loginForm']/div[2]/div/table/tbody/tr[2]/td[2]/input").send_keys('D&^4Vs')
    browser.find_element_by_xpath(".//*[@id='loginForm']/div[2]/div/table/tbody/tr[4]/td[2]/button").click()
    time.sleep(3)

    #获得title
    title=browser.title
    print title

    #比较
    if title==u'科来网络回溯分析系统 - 服务器':
        print 'title is ok'
    else:
        print 'title is on!'

    #Get URL
    now_url=browser.current_url
    print now_url

    #Compare URL
    if now_url=='https://192.168.5.197/main?mod=sysmgr':
        print 'URL is OK!'
    else:
        print 'URL Error!'

    #Get User
    now_user=browser.find_element_by_xpath("html/body/div[1]/div[1]/div[2]/font[2]").text
    print 'Now User is:%s' %now_user

    #Logout
    browser.find_element_by_xpath("html/body/div[1]/div[1]/div[2]/a[2]").click()
    time.sleep(1)

