# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')

myusername = "3170503079"  # 登录账号
mypassword = "610303npj"  # 登录密码

driver = webdriver.Chrome(chrome_options=chrome_options)  # 模拟浏览器打开网站

driver.get("https://pass.ujs.edu.cn/cas/login?service=http%3A%2F%2Fyun.ujs.edu.cn%2Fxxhgl%2Fyqsb%2Findex")
# driver.maximize_window() #将窗口最大化

try:
    # driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div[3]/div[1]').click()#定位语句去源码中找
    time.sleep(2)  # 延时加载

    print("找到登录框，输入账号密码")
    driver.find_element_by_xpath("//*[@id='username']").send_keys(myusername)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(mypassword)

    # 模拟点击登录
    print("模拟点击登录")
    driver.find_element_by_xpath("//*[@id='casLoginForm']/p[5]/button").click()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    # 模拟登陆后点击签到界面
    print("模拟登陆后点击签到界面")
    driver.find_element_by_css_selector("body > div.weui_btn_area > a").click()
    time.sleep(2)

    # 模拟点击签到
    print("模拟点击签到")
    driver.find_element_by_xpath("//*[@id='button1']").click()
    time.sleep(2)

    print("签到成功")
    driver.quit
except:
    print("签到失败")
driver.quit  # 退出去动
