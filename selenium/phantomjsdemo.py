#!/usr/bin/python

from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get("http://www.baidu.com")
print(browser.current_url)
