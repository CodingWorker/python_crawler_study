# -*- coding:utf-8 -*-

import urllib2

url = 'http://www.baidu.com'
http_handler = urllib2.HTTPHandler(debuglevel=1)
https_handler = urllib2.HTTPHandler(debuglevel=1)

opener = urllib2.build_opener(http_handler,https_handler)
urllib2.install_opener(opener)
req = urllib2.Request(url,None)
rsp = urllib2.urlopen(req)
print rsp.read()

