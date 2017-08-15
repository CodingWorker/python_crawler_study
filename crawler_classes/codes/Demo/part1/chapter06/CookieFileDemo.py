# -*- coding:utf-8 -*-
import urllib2
import cookielib

file_name = 'cookie.txt'

#构建cookie容器
cookie = cookielib.MozillaCookieJar(file_name)

#构建handler
handler = urllib2.HTTPCookieProcessor(cookie)

#构建opener
opener = urllib2.build_opener(handler)

url = 'http://www.baidu.com'
req = urllib2.Request(url,None)
rsp = opener.open(req)
for item in cookie:
    print 'Name: '+item.name
    print 'Value: '+item.value
cookie.save(ignore_discard=True,ignore_expires=True)



