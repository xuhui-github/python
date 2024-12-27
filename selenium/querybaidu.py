#!/usr/bin/python
from selenium import webdriver

driver=webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://www.baidu.com")
search_field=driver.find_element_by_name("wd")
search_field.clear()

search_field.send_keys("phones")
search_field.submit()


products=driver.find_elements_by_xpath("//div[@class='result c-container new-pmd']/h3/a")
print "Found "+str(len(products))+" products:"

for product in products:
  print product.text

driver.close()
