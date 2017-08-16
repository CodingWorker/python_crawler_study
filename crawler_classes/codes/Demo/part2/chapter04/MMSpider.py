#coding=utf-8
import urllib
import urllib2
import re

class MMSpider:
    def __init__(self,url,method,data):
        self.reqUrl = url
        self.reqMethod = method
        self.reqData = data
    def getPage(self):
        try:
            if self.reqMethod == 'GET':
                req =urllib2.Request(self.reqUrl + '?'+urllib.urlencode(self.reqData),None)
            elif self.reqMethod == 'POST':
                req = urllib2.Request(self.reqUrl,urllib.urlencode(self.reqData))
            else:
                raise Exception('invalid http method')

            rsp = urllib2.urlopen(req)
            self.page = rsp.read()
        except urllib2.HTTPError,ex:
            print ex.reason
        except urllib2.URLError,ex:
            print ex.reason
        except Exception,ex:
            print ex.reason


baseUrl = 'https://mm.taobao.com/json/request_top_list.htm'
reqMethod = 'GET'
reqData = {'page':1}

spider = MMSpider(baseUrl,reqMethod,reqData)
spider.getPage()
print spider.page

