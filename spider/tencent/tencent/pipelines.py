# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from pymongo import MongoClient

logger = logging.getLogger(__name__)

class TencentPipeline(object):
    def open_spider(self, spider):
        # spider.hello = "world"
        client = MongoClient()
        self.collection = client["tencent"]["hr"]

    def process_item(self, item, spider):
        logger.warning(item)
        self.collection.insert(dict(item))
        return item
