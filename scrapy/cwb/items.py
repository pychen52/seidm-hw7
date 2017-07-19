# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CwbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    sid = scrapy.Field()
    timestamp = scrapy.Field()
    r_10m = scrapy.Field()
    r_1h = scrapy.Field()
    r_3h = scrapy.Field()
    r_6h = scrapy.Field()
    r_12h = scrapy.Field()
    r_24h = scrapy.Field()
    r_td = scrapy.Field()
    r_yd = scrapy.Field()
    r_2d = scrapy.Field()
