# coding:utf-8
# HTML下载器,保证下载的网页没有乱码

import requests

class HtmlDownloader(object):
    # 用于下载页面的内容
    def download(self,url):
        if url is None:
            return None
        user_agent = "Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)"
        headers = {'User-Agent':user_agent}
        r = requests.get(url,headers=headers)

        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text


        return None
