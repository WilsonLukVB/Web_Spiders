# -*- coding: utf-8 -*-
import urllib


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_date(self, new_date):
        if new_date is None:
            return
        self.datas.append(new_date)


    def output_html(self):
       fout = open('output.html', 'w')

       fout.write('<!DOCTYPE html>')
       fout.write('<html lang="en">')
       fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>'")
       fout.write('<link rel="stylesheet" href="./layout.css">')
       fout.write('<body>')
       fout.write('<div id="wrap">')

       count = 1

       for data in self.datas:
           fout.write('<div class="block">')
           fout.write('<h2>%d. %s</h2>' % (count, data['title'].encode('utf-8')))
           fout.write('<a href=%s>%s</a>' % (urllib.unquote(data['url'].encode('utf-8')), urllib.unquote(data['url'].encode('utf-8'))))

           # fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
           fout.write("<p>%s</p>" % data['summary'].encode('utf-8'))
           fout.write("</div>")

           count +=1

       fout.write("</div>")
       fout.write("</body>")
       fout.write("</html>")
