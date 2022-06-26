#!/usr/bin/python

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

def main():
    options=Options()
    options.add_argument('--headless')
    driver=Firefox(executable_path='/usr/bin/geckodriver',options=options)
    driver.get("http://www.qiushibaike.com/8hr/page/1/")
    print(driver.page_source)
    driver.close()

main()
