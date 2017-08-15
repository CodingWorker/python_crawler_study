#coding=utf-8 
import urllib2
import urllib
import re

url = 'https://www.qiushibaike.com/'
headers={}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
headers['Referer'] = 'https://www.baidu.com/link?url=ncoqdmWH0r9tTfujHu0o12vLycPFnKSe0aUQsigPubfuzQjhiOe-U4p3JV5XtWeY&wd=&eqid=cda82bde0003ab520000000359931874'
req = urllib2.Request(url,None,headers)
rsp = urllib2.urlopen(req)

page_content = rsp.read()

r'<div class="article block untagged mb15.*?<div class="author clearfix">.*?<h2>(?P<author>.*?)</h2>.*?<div class="content">.*?<span>(?P<content>.*?)</span>'

'''
<div class="article block untagged mb15 typs_hot" id="qiushi_tag_119426792">


<div class="author clearfix">
<a href="/users/30773484/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3077/30773484/thumb/20170325123807.JPEG?imageView2/1/w/90/h/90" alt="梁生.伊梦">
</a>
<a href="/users/30773484/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
梁生.伊梦
</h2>
</a>
<div class="articleGender manIcon">25</div>
</div>

<a href="/article/119426792" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


买了块花肉，跟花生米煲，懒洗电饭锅就用煤气，心里美滋滋的葛优躺刷糗百。<br>别问我好不好吃，我要告诉你的是，煤气锅没有电饭锅好用，别问为什么，那一锅黑黑的东西我不认识，还有我现在忙着清理犯罪现场，挺忙的。。。<br>那个老板，这个破锅收废旧么...不要你钱你快拿走！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">803</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119426792" data-share="/article/119426792" id="c-119426792" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">14</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119426792" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119426792" class="up">
<a href="javascript:voting(119426792,1)" class="voting" data-article="119426792" id="up-119426792" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">817</span>
</a>
</li>
<li id="vote-dn-119426792" class="down">
<a href="javascript:voting(119426792,-1)" class="voting" data-article="119426792" id="dn-119426792" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-14</span>
</a>
</li>
<li class="comments">
<a href="/article/119426792" id="c-119426792" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>
'''
pattern = r'<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>'
pattern = r'<div class="article block untagged mb15.*?<div class="author clearfix">.*?<h2>(?P<author>.*?)</h2>.*?<div class="content">.*?<span>(?P<content>.*?)</span>'

regx = re.compile(pattern,re.S)

groups = regx.findall(page_content)
if groups !=None:
    for group in groups:
        print 'author: '+group[0]
        print 'content: '+group[1]