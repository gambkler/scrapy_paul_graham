# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class indexItem(scrapy.Item):
    article_urls = scrapy.Field()
    article_names = scrapy.Field()


class aritcleItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    raw = scrapy.Field()
    content = scrapy.Field()
