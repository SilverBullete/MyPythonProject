import os
from selenium import webdriver
from time import sleep


def initWork():
    # 初始化配置根据自己chromedriver位置做相应的修改
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    return driver


def login(un, pw):
    username = un
    password = pw
    url = 'https://mail.qq.com/'
    # 转至登陆界面
    driver.get(url)
    # 进入frame标签
    driver.switch_to.frame("login_frame")
    # 选择账号密码登陆
    driver.find_element_by_xpath("//*[@id='switcher_plogin']").click()
    # 输入账号密码并登陆
    driver.find_element_by_xpath("//*[@id='u']").send_keys(username)
    driver.find_element_by_xpath('//*[@id="p"]').send_keys(password)
    driver.find_element_by_xpath("//*[@id='login_button']").click()
    # 获取登陆后的cookie并返回
    cookie2 = driver.get_cookies()
    return cookie2


def fresh(cookies):
    # 将获取到的cookie加入webdriver
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()


def sendEmail(email, title, concent):
    # 选择发送邮件
    driver.find_element_by_xpath("//*[@id='composebtn']").click()
    # 进入frame标签
    driver.switch_to.frame("mainFrame")
    # 静止1s等待相应
    sleep(1)
    # 输入收件人，主题
    driver.find_element_by_xpath("//*[@id='toAreaCtrl']/div[2]/input").send_keys(email)
    sleep(1)
    driver.find_element_by_xpath("//*[@id='subject']").send_keys(title)
    sleep(1)
    # 进入下一级frame标签
    driver.switch_to.frame(0)
    # 输入邮件内容
    driver.find_element_by_xpath('/html/body').send_keys(content)
    # 返回上一级frame标签
    driver.switch_to.parent_frame()
    # 点击发送邮件
    driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()


driver = initWork()
username = ""
password = ""
email = ""
title = ""
content = ""
cookies = login(username, password)
fresh(cookies)
sleep(2)
sendEmail(email, title, content)
driver.close()
driver.quit()
