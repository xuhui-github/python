#!/usr/bin/python

from urllib import urlopen
import re

def extract_links(page):
    link_regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return link_regex.findall(page)
def download_page(url):
    return urlopen(url).read().decode('utf-8')
if __name__=='__main__':
    target_url='http://www.apress.com/'  
    apress=download_page(target_url)
    links=extract_links(apress)

    for link in links:
        print link


