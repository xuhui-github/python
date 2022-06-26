#!/usr/bin/python
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

options=Options()
options.add_argument('--headless')

browser=webdriver.Firefox(options=options)
browser.get('http://www.baidu.com')
print browser.page_source
browser.close()
