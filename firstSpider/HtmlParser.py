# coding:utf-8
# HTML解析器

import re
import urllib.parse
from bs4 import BeautifulSoup

class HtmlParser(object):

    # 用于解析网页内容，抽取url和数据
    # page_url：下载页面的url
    # html_cont:下载的网页内容
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        book_details = self._get_book_details(soup)
        return  book_details

    # 抽取新的URL集合
    def _get_book_details(self,soup):
        self.book_details = []
        self.operatedbooks = []
        # 抽取所有符合要求的a标记
        books = soup.find_all('img',src=re.compile(r'https://images-na.ssl-images-amazon.com'))

        # 去除不符合条件的书籍
        for book in books:
            if('200_.jpg' in book['src']):
                self.operatedbooks.append(book)

        for book in self.operatedbooks:
            book_detail = {}
            book_detail['src'] = book['src']
            book_detail['name'] = book['alt']

            self.book_details.append(book_detail)
        # self.book_details.reverse()
        return self.book_details




