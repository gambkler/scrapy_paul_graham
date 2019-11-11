import urllib

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader

from paulgraham.items import indexItem, aritcleItem
from paulgraham.utils import Cleaner


class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['paulgraham.com']
    start_urls = ['http://paulgraham.com/articles.html']
    base_url = 'http://paulgraham.com'

    def parse(self, response):
        l = ItemLoader(item=indexItem(), response=response)
        articles = response.xpath('//font/a')
        for i in articles:
            article_url = urllib.parse.urljoin(self.base_url, i.attrib['href'])
            article_name = i.xpath('text()').get()
            l.add_value('article_urls', article_url)
            l.add_value('article_names', article_name)
        return l.load_item()
