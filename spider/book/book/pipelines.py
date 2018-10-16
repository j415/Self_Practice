# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re


class BookPipeline(object):
    def process_item(self, item, spider):
        item["book_publish_date"] = self.content_item(item["book_publish_date"])
        # item["book_publish_date"] = item["book_publish_date"].strip()
        print(item)
        print(type(item["book_publish_date"]))
        return item

    def content_item(self, content):
        # content = re.sub("\xa0", "", content)
        if content == None:
            content = None
        else:
            content = "".join(content.split())
        return content
