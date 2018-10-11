# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TencentItem


class HrSpider(CrawlSpider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tr_list = response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for tr in tr_list:
            item = TencentItem()
            item["href"] = "https://hr.tencent.com/" + tr.xpath("./td[1]/a/@href").extract_first()
            yield scrapy.Request(
                item["href"],
                callback=self.parse_detail,
                meta={"item": item}
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["title"] = response.xpath("//tr[@class='h']/td/text()").extract_first()
        item["aquire"] = response.xpath("//div[text()='工作要求：']/../ul/li/text()").extract()
        # print(item)
        yield item
