# -*- coding:utf-8 -*-

import urllib2

enable_proxy = True
base_url = 'http://www.baidu.com'
proxy_handler = urllib2.ProxyHandler({'http':'http://www.baidu.com'})
null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)

urllib2.install_opener(opener)

url = 'http://www.baidu.com'
req = urllib2.Request(url)
rsp = urllib2.urlopen(req)
print rsp.read()




