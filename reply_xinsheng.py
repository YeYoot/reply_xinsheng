#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import sys
import time
import random

from config import *


def Login(user, password):
    options = webdriver.ChromeOptions()
    if not SHOW_CHROM:
        options.add_argument('--headless')
    driver_path = os.getcwd() + '\\chromedriver\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_options=options, executable_path=driver_path)
    driver.maximize_window()
    # 登陆
    driver.get(LOGIN_URL)
    try:
        locator = (By.XPATH, PATH["输入账号"])
        WebDriverWait(driver, 15, 0.5).until(EC.presence_of_element_located(locator))
        driver.find_element_by_xpath(PATH["输入账号"]).send_keys(USERNAME)
        driver.find_element_by_xpath(PATH["输入密码"]).send_keys(PASSWORD)
        driver.find_element_by_xpath(PATH["点击登陆"]).click()
    except Exception as e:
        print("登陆失败。原因：{}".format(e))

    print("登陆成功。")
    return driver


def reply_one_message(driver, message):
    driver.get(URL)
    try:
        locator = (By.XPATH, PATH["回复"])
        WebDriverWait(driver, 15, 0.5).until(EC.element_to_be_clickable(locator))
        driver.switch_to.frame("post_content_kinde")
        driver.find_element_by_xpath(PATH["输入框"]).send_keys(message)
        driver.switch_to.default_content()
        driver.find_element_by_xpath(PATH["回复"]).click()
    except Exception as e:
        print("回复一条信息失败。原因：{}".format(e))
        return False

    return True


def generate_sleep_time():
    return random.randint(MIN_SLEEP_TIME, MAX_SLEEP_TIME)


def generate_content():
    return word[random.randint(0, len(word) - 1)] + str(random.randint(1000, 100000))


def reply(driver, MAX_MESSAGE):
    sended_num = 0
    failed_num = 0

    while (sended_num < MAX_MESSAGE):
        message = generate_content()
        if (reply_one_message(driver, message)):
            sended_num += 1
            print("发送信息{}成功.\n当前已发送：{} / {}".format(message, sended_num, MAX_MESSAGE))
            if sended_num >= MAX_MESSAGE:
                driver.quit()
                return True
            sleep_time = generate_sleep_time()
            print("休息{}秒。".format(sleep_time))
            time.sleep(sleep_time)
        else:
            failed_num += 1
            if failed_num >= 3:
                driver.quit()
                return False


if __name__ == '__main__':
    try:
        MAX_MESSAGE = int(sys.argv[1])
    except:
        print("请输入回帖个数！！！")
        sys.exit(-1)
    driver = Login(USERNAME, PASSWORD)
    if (reply(driver, MAX_MESSAGE)):
        print("任务成功，已回复{}条随机信息。".format(MAX_MESSAGE))
    else:
        print("任务失败。")
