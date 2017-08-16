# coding=utf-8
import urllib2
import urllib
import re

class BaiduTieBaSpider:
    def __init__(self,baseUrl):
        self.baseUrl = baseUrl

    def getPage(self):
        try:
            url = self.baseUrl
            req = urllib2.Request(url,None)
            rsp = urllib2.urlopen(req)

            self.pageContent = rsp.read()
        except urllib2.HTTPError,e:
            print e.message
        except urllib2.URLError,e:
            print e.message

query = {}
query['kw'] = '骑行'
query['pn'] = 0  #跳过多少条，每页50条
base_url = 'http://tieba.baidu.com/f'
url = base_url+'?'+urllib.urlencode(query)
spider = BaiduTieBaSpider(url)
spider.getPage()
pageContent=spider.pageContent

'''
<li class=" j_thread_list clearfix" data-field="{&quot;id&quot;:5274223109,&quot;author_name&quot;:&quot;\u5f20\u9f99Open66_&quot;,&quot;first_post_id&quot;:110615374608,&quot;reply_num&quot;:1,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:true,&quot;frs_tpoint&quot;:null}">
            <div class="t_con cleafix">
        
                    <div class="col2_left j_threadlist_li_left">
                <span class="threadlist_rep_num center_text" title="回复">1</span>
            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a href="/p/5274223109?fid=416282" title="十月一 去四川的 旅友有吗 求" target="_blank" class="j_th_tit ">十月一 去四川的 旅友有吗 求</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author " title="主题作者: 行走的行者😲" data-field="{&quot;user_id&quot;:2930786037}"><i class="icon_author"></i><span class="frs-author-name-wrap"><a data-field="{&quot;un&quot;:&quot;\u5f20\u9f99Open66_&quot;}" class="frs-author-name j_user_card " href="/home/main/?un=%E5%BC%A0%E9%BE%99Open66_&amp;ie=utf-8&amp;fr=frs" target="_blank">行走的行...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">06:10</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            十月一 去四川的 旅友有吗 求队友 男女不限 骑行去稻城
        </div>

            <div class="small_wrap j_small_wrap" is_handle="true">
                <a href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5274223109" style="float: left;"><li><a class="thumbnail vpic_wrap"><img src="http://imgsrc.baidu.com/forum/wh%3D90%2C160%3Bcrop%3D0%2C0%2C90%2C90/sign=94962d26adefce1bea7ec0c39f7dc2e8/5598d3628535e5dde368cb0f7cc6a7efcf1b6277.jpg" attr="49165" data-original="http://imgsrc.baidu.com/forum/wh%3D90%2C160%3Bcrop%3D0%2C0%2C90%2C90/sign=94962d26adefce1bea7ec0c39f7dc2e8/5598d3628535e5dde368cb0f7cc6a7efcf1b6277.jpg" bpic="http://imgsrc.baidu.com/forum/pic/item/5598d3628535e5dde368cb0f7cc6a7efcf1b6277.jpg" class="threadlist_pic j_m_pic " style="display: inline; width: 90px; height: 90px;"></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 🐶天涯過客🐶">
            <i class="icon_replyer"></i>
            <a data-field="{&quot;un&quot;:&quot;\u7231\u4e0aEbook&quot;}" class="frs-author-name j_user_card  vip_red " href="/home/main/?un=%E7%88%B1%E4%B8%8AEbook&amp;ie=utf-8&amp;fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/2-2.png" class="nicknameEmoji" style="width:13px;height:13px">天涯過...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            06:20        </span>
</div>
                </div>
                    </div>
    </div>
</li>
'''
pattern = r'<a.*?class="j_th_tit.*?>(?P<title>.*?)</a>.*?class="frs-author-name j_user_card ".*?>(?P<author>.*?)(<img.*?/>)*</a>'
regx = re.compile(pattern,re.S)
groupIter = regx.finditer(pageContent)
index = 0
if groupIter!=None:
    for iter in groupIter:
        index = index+1
        print str(index)+') Author: '+iter.group('author')+'@Title: '+iter.group('title')
