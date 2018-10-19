# coding:utf-8
# 数据存储

import codecs
class DataOutput(object):

    def __init__(self):
        self.books = []

    # 将解析出来的数据存储到内存中
    def store_book(self,book):
        if book is None:
            return
        self.books.append(book)


    # 定义输出页面
    def output_html(self):
        fout=codecs.open('book.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8'/></head>")
        fout.write("<body>")
        fout.write("<h1 align='center'>亚马逊图书销售排行榜</h1>")
        fout.write("<table border='1' align='center'>")
        fout.write("<tr>")
        fout.write("<th width='10%'>排名</th>")
        fout.write("<th width='60%'>书名</th>")
        fout.write("<th width='30%'>图片</th>")
        fout.write("</tr>")
        for book in self.books:
            fout.write("<tr>")
            fout.write("<td>%d</td>"%(self.books.index(book)+1))
            fout.write("<td>%s</td>"%book['name'])
            fout.write("<td><img style='width=400px;height=200px'src='%s'/></td>"%book['src'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
