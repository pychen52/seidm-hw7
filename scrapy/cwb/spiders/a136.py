# -*- coding: utf-8 -*-
import scrapy
from cwb.items import CwbItem

class A136Spider(scrapy.Spider):
    name = 'a136'
    allowed_domains = ['www.cwb.gov.tw']
    start_urls = ['http://www.cwb.gov.tw/V7/observe/rainfall/A136.htm']

    def parse(self, response):
        item = CwbItem()
        t_sl = response.css('center table.description tr td::text').re('[0-9]+')
        timestamp = t_sl[0] + '-' + t_sl[1] + '-' + t_sl[2] + 'T' + t_sl[3] + ':' + t_sl[4] + ':' + t_sl[5] + '+08:00'
        
        for station in response.css('tr.Area3'):
            item['name'] = station.css('td span::text').re("[\u4e00-\u9fa5]{1,}")[0]
            item['sid'] = station.css('td span::text').re("[A-Z0-9]{5,}")[0]
            item['timestamp'] = timestamp
            item['r_10m'] = station.css('td font::text').extract()[0]
            item['r_1h'] = station.css('td font::text').extract()[1]
            item['r_3h'] = station.css('td font::text').extract()[2]
            item['r_6h'] = station.css('td font::text').extract()[3]
            item['r_12h'] = station.css('td font::text').extract()[4]
            item['r_24h'] = station.css('td font::text').extract()[5]
            item['r_td'] = station.css('td font::text').extract()[6]
            item['r_yd'] = station.css('td font::text').extract()[7]
            item['r_2d'] = station.css('td font::text').extract()[8]
            yield item
