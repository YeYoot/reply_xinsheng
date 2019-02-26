#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# W3账号及密码
USERNAME = "xxxx"
PASSWORD = "xxxx"

# 可自定义发送的消息
word = ["厉害厉害~", "支持一波~", "加油！！", "666啊!!", "顶顶顶..."]

# 间隔时间 单位：秒 当前休息时间为 1分钟--5分钟 60 300
MIN_SLEEP_TIME = 60
MAX_SLEEP_TIME = 300

# 是否前台显示浏览器
SHOW_CHROM = False

# 新帖子的URL请在这里修改
URL = "http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=4187335&p=last#p37449143"

# 以下内容无需修改
# LOGIN_URL = "https://uniportal.huawei.com/uniportal/"
LOGIN_URL = "https://login.huawei.com/login"

PATH = {
    "输入账号": '//*[@id="uid"]',
    "输入密码": '//*[@id="password"]',
    "点击登陆_uniportal": '//*[@id="content"]/div[2]/div[2]/div[1]/div[5]/center/input',
    "点击登陆": '//*[@id="page-input-holder-pwd"]/form/div/input[2]',

    "输入框": '/html/body',
    "回复": '//*[@id="post_btn"]'
}


