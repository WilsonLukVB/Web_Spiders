# -*- coding: utf-8 -*-
from baike_spider import Url_manager, html_download, html_parse, html_output


class SpiderMain(object):
    def __init__(self):
        self.urls = Url_manager.UrlManger()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parse.HtmlParser()
        self.outputer = html_output.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():  #如果有待爬取的url
            try:
                new_url = self.urls.get_new_url() #取一个新的url
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url) #下载好对应的页面
                new_urls, new_date = self.parser.parse(new_url, html_cont) #对页面进行解析得到行的url和数据
                self.urls.add_new_urls(new_urls) #把新的url补充进url管理器
                self.outputer.collect_date(new_date) #收集新的url数据
                if count == 5:
                    break
                count = count + 1
            except:
                print 'craw fail'

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"   #爬取的入口url
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)









