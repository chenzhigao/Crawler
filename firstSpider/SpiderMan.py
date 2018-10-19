# coding:utf-8
# 爬虫调度器
from firstSpider.DataOutput import DataOutput
from firstSpider.HtmlDownloader import HtmlDownloader
from firstSpider.UrlManager import UrlManager
from firstSpider.HtmlParser import HtmlParser

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self):
        # 添加URL入口
        self.manager.add_new_url("https://www.amazon.cn/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=1")
        self.manager.add_new_url("https://www.amazon.cn/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg=2")

        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                # 从URL管理器获取新的URL
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                html = self.downloader.download(new_url)
                # HTML解析器抽取网页数据
                book_details = self.parser.parser(new_url,html)
                # 数据存储器存储文件
                print(book_details)
                for book_detail in book_details:
                    self.output.store_book(book_detail)
            except Exception as e:
                print("crawl failed")
        self.output.output_html()

if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl()
