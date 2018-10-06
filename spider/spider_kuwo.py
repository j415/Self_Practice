# author:aspiring


import requests
from lxml import etree
import json


class KuwoSpider:
    def __init__(self):
        self.start_url = "http://www.kuwo.cn/bang/index"
        # self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    def parse_url(self):
        response = requests.get(self.start_url, headers=self.headers)
        print(type(response))
        return response.content.decode()

    def get_content_list(self, html_str):
        # print(type(html_str))
        html = etree.HTML(html_str)
        div_list = html.xpath("//ul[@class='listMusic']/li")
        # print(div_list)
        content_list = []
        for div in div_list:
            item = {}
            item["order"] = div.xpath(".//p[@class='num']/text()")[0]
            item["song_name"] = div.xpath("./div[@class='name']/a/text()")[0]
            item["song_url"] = div.xpath("./div[@class='name']/a/@href")[0]
            item["songer"] = div.xpath("./div[@class='artist']/a/text()")[0]
            item["heatValue"] = div.xpath(".//div[@class='heatValue']/@style")
            item["heatValue"] = item["heatValue"][0].replace("width:", "")
            # print(item)
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):
        with open("files/kuwo.txt", "w", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")
        print("保存成功")

    def run(self):  # 实现主要逻辑
        # 1.start_url
        # 2.发送请求，获取响应
        html_str = self.parse_url()
        # 3.提取信息
        content_list = self.get_content_list(html_str)
        # 4.保存
        self.save_content_list(content_list)


if __name__ == '__main__':
    kuwo = KuwoSpider()
    kuwo.run()
