import urllib

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader

from paulgraham.items import indexItem, aritcleItem
from paulgraham.utils import Cleaner


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['paulgraham.com']
    start_urls = ['http://paulgraham.com/articles.html']
    base_url = 'http://paulgraham.com'
    cleaner = Cleaner()

    def parse(self, response):
        l = ItemLoader(item=indexItem(), response=response)
        articles = response.xpath('//font/a')
        for i in articles:
            article_url = urllib.parse.urljoin(self.base_url, i.attrib['href'])
            article_name = i.xpath('text()').get()
            l.add_value('article_urls', article_url)
            l.add_value('article_names', article_name)
            yield scrapy.Request(article_url, callback=self.parse_article)
        return l.load_item()
    
    def parse_article(self, response):
        l = ItemLoader(item=aritcleItem(), response=response)
        l.add_value('url', response.url)
        l.add_xpath('name', '//img/@alt')
        l.add_value('raw', response.body.decode())
        l.add_value('content', self.cleaner.clean(response.xpath('//font[@size="2" and @face="verdana"]')[0].getall()[0]))
        return l.load_item()
