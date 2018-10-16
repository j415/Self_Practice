# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import time

class DangdangSpider(RedisCrawlSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://book.dangdang.com/']
    redis_key = "dangdang"

    rules = (
        # 大小分类
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='con flq_body']/div")), follow=True),
        # 详情页
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='bigimg']/li")), callback="parse_book_detail"),
        # 翻页
        Rule(LinkExtractor(restrict_xpaths=("//ul[@name='Fy']/li")), follow=True),
    )

    def parse_book_detail(self, response):
        item = {}
        item["book_title"] = response.xpath("//div[@class='name_info']/h1/@title").extract_first()
        item["book_author"] = response.xpath("//span[@id='author']/a/text()").extract_first()
        item["book_press"] = response.xpath("//div[@class='messbox_info']/span[2]/a/text()").extract_first()
        item["book_publish_date"] = response.xpath("//div[@class='messbox_info']/span[3]/text()").extract_first()
        item["book_img"] = response.xpath("//div[@class='pic']/a/img/@src").extract_first()

        # print(type(item["title"]))
        # print(item)
        yield item

    # def parse_book_href(self, response):
    #
    #     item = {}
    #     item["book_href"] = response.xpath("./")