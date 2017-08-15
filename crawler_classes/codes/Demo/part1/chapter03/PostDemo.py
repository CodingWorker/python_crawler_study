import urllib
import urllib2

account = {'username':'Daniel','age':12}
post_data = urllib.urlencode(account)
url = 'http://www.baidu.com'
req = urllib2.Request(url,post_data)
rsp = urllib2.urlopen(req)
print rsp.read()