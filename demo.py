#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import time
from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0.0'
desired_caps['deviceName'] = 'HUAWEI EML-AL00'
desired_caps['appPackage'] = 'com.sina.news'
desired_caps['appActivity'] = 'com.duolabao.customer.activity.BootActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

