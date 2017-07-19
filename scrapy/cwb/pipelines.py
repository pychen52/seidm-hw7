# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors
import re

class CwbPipeline(object):
    def open_spider(self, spider):
        self.conn = MySQLdb.connect(host='127.0.0.1',
                                    user='demouser',
                                    passwd='demo1234',
                                    db='demo',
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close() 

    def check_item(self, item):
        for key, val in item.items():
            if re.match('^r_', key):
                if val and not re.match('^\d+?\.\d+?$', val):
                    item[key] = None
        return item

    def process_item(self, item, spider):
        item = self.check_item(item)
        self.cursor.execute("""INSERT INTO rainfall (sid, name, timestamp, r_10m, r_1h, r_3h, r_6h, r_12h, r_24h, r_td, r_yd, r_2d) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",(
            item['sid'],
            item['name'],
            item['timestamp'],
            item['r_10m'],
            item['r_1h'],
            item['r_3h'],
            item['r_6h'],
            item['r_12h'],
            item['r_24h'],
            item['r_td'],
            item['r_yd'],
            item['r_2d']
        ))  
        self.conn.commit()

        return item

