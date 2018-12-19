# -*- coding: utf-8 -*-
import string
import urllib

class HtmlDownloader(object):

    def download(self, new_url):
        if new_url is None:
            return None
        decode_url_ = urllib.quote(new_url, safe=string.printable)
        response = urllib.urlopen(decode_url_)

        if response.getcode() != 200:
            return None

        return response.read()
