#-*- coding:utf-8 -*-
import urllib2

url = 'http://www.csdn.net/fsfa'
req = urllib2.Request(url)
try:
    rsp = urllib2.urlopen(req)
except urllib2.HTTPError, ex:
    print ex.url
except urllib2.URLError ,e:
    print e.reason
    print e.errno

