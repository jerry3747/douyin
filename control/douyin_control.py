#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import random
import time
from appium import webdriver

STARTUP_CAPS = {
    'platformName': 'Android',
    # 'automationName': 'UIAutomator2',
    'appPackage': 'com.ss.android.ugc.aweme',
    'appActivity': '.main.MainActivity',
    'fullReset': False,
    'noReset': True,
    'newCommandTimeout': 7200,
    'platformVersion': '4.4.4',
    'deviceName': '02c5b5ce091ccc8e',
    'unicodeKeyboard': True,
    'resetKeyboard':True
}
EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

driver = webdriver.Remote(EXECUTOR, STARTUP_CAPS)
time.sleep(10)
driver.find_element_by_id('com.ss.android.ugc.aweme:id/azj').click()
time.sleep(10)
driver.find_element_by_id('com.ss.android.ugc.aweme:id/aar').send_keys('汉服')
time.sleep(1)
driver.find_element_by_id('com.ss.android.ugc.aweme:id/dis').click()
time.sleep(5)
screen = driver.get_window_size()
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
while True:
    driver.swipe(x*0.5, y*0.75, x*0.5, y*0.25)
    time.sleep(random.random())
