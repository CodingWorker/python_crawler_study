#encoding=utf-8

import urllib2
import urllib
import re


class MMAnalyze():
    '''
    
    '''
    def analyze(self,page):
        pass

    def getPattern(self):
        pass


url = 'https://mm.taobao.com/self/model_info.htm?user_id=687471686&e'
rsp = urllib2.urlopen(url)
page = rsp.read()
print page

'''
<ul class="mm-p-info-cell clearfix">
    		<li><label>昵  称:</label><span>田媛媛</span></li>
        	<li class="mm-p-cell-left"><label>生　　日:</label><span> 公历 &nbsp;06月22日</span></li>
    		<li class="mm-p-cell-right"><label>所在城市:</label><span>广州市</span></li>
    		<li class="mm-p-cell-left"><label>职　　业:</label><span>平面模特 设计师 T台、展模特</span></li>
    		<li class="mm-p-cell-right"><label>血　　型:</label><span></span></li>
			<li><label>学校/专业:</label><span>广东纺织职业技术学院&nbsp;&nbsp;&nbsp;&nbsp;服装设计与展示</span></li>
			<li><label>风　　格:</label><span>欧美 韩版 街头</span></li>
		　	<li class="mm-p-small-cell mm-p-height"><var></var><p>168.0CM</p></li>
    		<li class="mm-p-small-cell mm-p-weight"><var></var><p>46.0KG</p></li>
    		<li class="mm-p-small-cell mm-p-size"><var></var><p>83-62-89</p></li>
    		<li class="mm-p-small-cell mm-p-bar"><var></var><p>34</p></li>
    		<li class="mm-p-small-cell mm-p-shose"><var></var><p>38码</p></li>
		</ul>
'''
pattern = r'<ul class="mm-p-info-cell clearfix">.*?<li><label>.*?<span>(?P<name>.*?)</span></li>'
regex=re.compile(pattern)
groups = regex.findall(page)
if groups:
    for group in groups:
        print group