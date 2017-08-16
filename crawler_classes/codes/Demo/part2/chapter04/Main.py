# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import cookielib

class Spider:
    def __init__(self,url,method,data,headers):
        self.url=url
        self.method=method
        self.data=data
        self.headers=headers
        self.page = None

    def getPage(self):
        try:
            if self.method=='GET':
                url = self.url +'?'+ urllib.urlencode(self.data)
                req = urllib2.Request(url, None)
            else:
                url = self.url
                req = urllib2.Request(url, self.data)

            cookie  = cookielib.MozillaCookieJar('cookie.txt')
            handler = urllib2.HTTPCookieProcessor(cookie)
            opener = urllib2.build_opener(handler)
            rsp = opener.open(req)

            self.page=rsp.read()
        except urllib2.HTTPError,ex:
            print ex.reason
        except urllib2.URLError,ex:
            print ex.reason


def builSpider(pageIndex):
    '''
    get builder
    :param pageIndex:
    :return:
    '''
    url = 'https://mm.taobao.com/json/request_top_list.htm';
    data = {'page':pageIndex}

    headers = {}
    headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    # headers[':authority'] = 'mm.taobao.com'
    # headers[':method'] = 'GET'
    # headers[':path'] = '/json/request_top_list.htm?page=1'
    # headers[':scheme'] = 'https'
    # headers['accept-encoding'] = 'gzip, deflate, br'
    headers['accept-language'] = 'zh-CN,zh;q=0.8'
    headers['cache-control'] =  'max-age=0'
    headers['Content-Type'] = 'text/html;charset=utf-8'

    headers['cookie'] = 'v=0; cookie2=10ed32d35ac0397a203045bc542dce86; t=19ebdcb9f9a945fb94a205366d9b09c9; _tb_token_=e63e5e1e3ead1; UM_distinctid=15dea15f21fdf6-01ae42717152ee-9383666-1fa400-15dea15f220e78; CNZZDATA30064598=cnzz_eid%3D2023066893-1502867083-https%253A%252F%252Fmm.taobao.com%252F%26ntime%3D1502867083; CNZZDATA30063600=cnzz_eid%3D1472911551-1502867083-https%253A%252F%252Fmm.taobao.com%252F%26ntime%3D1502867083; cna=T9zPEbw/XUsCAT0ya34BT6Iy; JSESSIONID=E01C9153104A4FF499932A17AC708686; uc1=cookie14=UoTcDUUzupSVnQ%3D%3D; mt=ci%3D-1_0; isg=Ak5OFYHEmy1UDS8OVWnsA0bGnyS83iAmbDK8eHiWodEg2-414F9i2fSTZTFM'
    headers['upgrade-insecure-requests'] = 1

    spider = Spider(url,'GET',data,headers)
    spider.getPage()
    return spider

'''
<div class="list-item">
			<div class="personal-info">
				<div class="pic-word">
					<div class="pic s60">
						<a href="//mm.taobao.com/687471686.htm" target="_blank" class="lady-avatar">		<img src="//gtd.alicdn.com/sns_logo/i2/TB1XZ1PQVXXXXaJXpXXSutbFXXX.jpg_60x60.jpg" alt="" width="60" height="60">
</a>
					</div>
					<p class="top">
					<a class="lady-name" href="//mm.taobao.com/self/model_card.htm?user_id=687471686" target="_blank">田媛媛</a>
					<em><strong>27</strong>岁</em>
					<span>广州市</span>
										<span class="friend-follow J_FriendFollow" data-custom="type=14&amp;app_id=12052609" data-group="" data-userid="687471686">加关注</span>
					</p>
					<p>
					<em>平面模特 设计师 T台、展模特</em>
					<em><strong>164433</strong>粉丝</em>
					</p>
				</div>
									<div class="pic w610">
    					<a href="//mm.taobao.com/photo-687471686-10000854046.htm?pic_id=10003369435" target="_blank">
    						<img data-ks-lazyload="//img.alicdn.com/imgextra/i4/687471686/TB1TORaKFXXXXc0aXXXXXXXXXXX_!!2-tstar.png" src="//assets.alicdn.com/kissy/1.0.0/build/imglazyload/spaceball.gif">
    					</a>
    				</div>
							</div>
			<div class="list-info">
				<div class="popularity">
					<dl>
						<dt>
														1
						</dt>
																				<dd>
								<span>总积分:</span>
																	60742
															</dd>
											</dl>
				</div>
									<ul class="info-detail">
                    	                    		                    			<li>新增积分:<strong>529</strong></li>
                    		                    	                    	                    		                    			<li>好评率:<strong>90.0</strong> %</li>
                    		                    		                    			<li>导购照片:<strong>888</strong> 张</li>
                    		                    		                    			<li>签约数量:<strong>406</strong> 次</li>
                    		                    	                    </ul>
    				<p class="description">
    					你还在为上下衣物搭配而苦恼么..你还在为出门不知道穿什么而烦躁么 ..vvip女神教你一键(_)美美哒 ！ 不需要过多的搭配.不需要为不协调而苦恼 ..我们为你选好让你出门美美哒！！
                    </p>
                        				<div class="J_LikeIt" photo-id="687471686_10003369435" photo-favor-count="0">
					   <div class="mm-photolike"><a href="javascript:void(0)" class="mm-photolike-btn" data-targetid="687471686_10003369435" data-count="0">喜欢</a>
					      <var class="mm-photolike-count radius-3">
						    							   0
													  </var>
					   </div>
					</div>
                                        
							</div>
		</div>
'''

def analyze(page,f):
    '''
    analyze page
    :param page:
    :param f:
    :return:
    '''
    pattern = r'<a href="(?P<intro_url>.*?)".*?<img src="(?P<pic_url>.*?)".*?<a class="lady-name" href="(?P<user_page>.*?)" target="_blank">(?P<name>.*?)</a>.*?<strong>(?P<age>\d{1,2})</strong>.*?<span>(?P<address>.*?)</span>.*?<em>(?P<work>.*?)</em>'
    regx = re.compile(pattern,re.S)
    groups = regx.findall(page)

    if groups:
        for group in groups:
            intro_url =group[0]
            pic_url = group[1]
            user_page = group[2]
            name = group[3]
            age = group[4]
            address = group[5]
            work = group[6]
            line = '%s,%s,%s,%s,%s,%s,%s'%(intro_url,pic_url,user_page,name,age,address,work)
            f.write(line+'\r')

def start():
    '''
    start run
    :return:
    '''
    max_page = 1000
    f = file('demo.txt', 'a')
    for pageIndex in xrange(0,max_page):
        spider = builSpider(pageIndex)
        analyze(spider.page,f)

    f.close()

start()