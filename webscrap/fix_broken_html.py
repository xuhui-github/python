#!/usr/bin/python3
import bs4
import html5lib
from pprint import pprint
from bs4 import BeautifulSoup

broken_html = "<ul class=country><li>Area<li>Population</ul>"
soup = BeautifulSoup(broken_html, "html5lib")
fixed_html = soup.prettify()
pprint(fixed_html)

ul = soup.find("ul", attrs={"class": "country"})
ulElem = ul.find("li")
print(ulElem)
ulElems = ul.find_all("li")
print(ulElems)
