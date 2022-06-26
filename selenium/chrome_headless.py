#!/usr/bin/python
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

chrome_options=Options()
chrome_options.add_argument('--headless')
chrome=Chrome(options=chrome_options)
chrome.get("http://www.baidu.com")
print chrome.page_source
chrome.quit()
