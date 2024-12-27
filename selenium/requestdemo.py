#!/usr/bin/python
import requests

def download_page(url):
  try:
      return requests.get(url).text.encode('utf-8')
  except:
      print 'error in the url',url

if __name__=='__main__':
    content=download_page('http://www.baidu.com')
    if content:
        print content
