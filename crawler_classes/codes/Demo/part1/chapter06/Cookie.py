# -*- coding:utf-8 -*-
import urllib2
import cookielib

#创建cookie的对象来保存cookie
cookie = cookielib.CookieJar()

#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)

#通过handler来创建opener
opener = urllib2.build_opener(handler)

url = 'http://www.baidu.com'
req = urllib2.Request(url,None)
rsp = opener.open(req)
for item in cookie:
    print 'Name: '+item.name
    print 'Value: '+item.value
