def test_search_by_name(self):
    self.search_field=self.driver.find_element_by_name("q")
    self.search_filed.clear()

    self.search_field.send_keys('salt shaker')
    self.search_field.submit()

    products=self.driver.find_element_by_xpath("//h2[@class='product-name']/a")
    self.assertEqual(1,len(products)


