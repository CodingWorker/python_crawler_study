import urllib
import urllib2

base_url = 'http://www.baidu.com/s'
#ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=csdn
query = {}
query['ie'] = 'utf-8'
query['f'] = '8'
query['rsv_bp'] = 1
query['rsv_idx'] =  1
query['tn'] = 'baidu'
query['wd'] = 'csdn'

url = base_url+'?'+urllib.urlencode(query)
req = urllib2.Request(url,None,{'Content-Type':'text/html;charset=utf-8'})
rsp = urllib2.urlopen(req)
print rsp.read()

#http://www.baidu.com?tn=baidu&wd=csdn
print rsp.geturl()