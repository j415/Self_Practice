# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class HuyaoxiaohongniangSpider(CrawlSpider):
    name = 'huyaoxiaohongniang'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://search.bilibili.com/all?keyword=%E7%8B%90%E5%A6%96%E5%B0%8F%E7%BA%A2%E5%A8%98']
    print("2")

    rules = (
        Rule(LinkExtractor(
            allow=r'https://search.bilibili.com/all?keyword=%E7%8B%90%E5%A6%96%E5%B0%8F%E7%BA%A2%E5%A8%98&page=\d+'),
             follow=True),
        Rule(LinkExtractor(allow=r'//www.bilibili.com/video/av\d+\?from=search&seid=4635229979684728515'),
             callback='parse_item'),
    )
    print("3")

    def parse_item(self, response):
        print("*" * 100)
        item = {}
        item["title"] = response.xpath("//span[@class='tit tr-fix']/text()").extract_first()
        item["publish_date"] = response.xpath("//div[@class='video-data']/time/text()").extract_first()
        item["vie_num"] = re.findall(r'"view": (.*?),', response.body.decode())
        item["like"] = re.findall(r'"tag_id": (.*?),', response.body.decode())
        print(item)
