#conding:utf-8

import urllib2
import urllib
import cookielib

url = 'https://mm.taobao.com/json/request_top_list.htm'
cookie =cookielib.MozillaCookieJar('cookie.txt');
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

req = urllib2.Request(url)
rsp = opener.open(req)

print rsp.read()

cookie.save(ignore_discard=False,ignore_expires=False)