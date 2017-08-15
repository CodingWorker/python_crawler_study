#-*- coding:utf-8 -*-
#中文

import urllib
import  urllib2

base_url = 'http://www.baidu.com'
post_data = urllib.urlencode({})
headers = {}
headers['Content-Type'] = 'text/html;charset=utf-8'
headers['Accept-Encoding'] = 'gzip, deflate, sdch, br'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
url = base_url+urllib.urlencode(post_data)
req = urllib2.Request(url,None,headers)
rsp = urllib2.urlopen(req)
print rsp.read()
print rsp.geturl()