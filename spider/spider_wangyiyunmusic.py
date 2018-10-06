# author:aspiring

import requests
import json
from lxml import etree


class WangyiyunSpider:
    def __init__(self):
        # self.start_url = "https://music.163.com/#/discover/playlist"
        self.start_url = "https://music.163.com/#/discover/playlist/?cat=%E5%85%A8%E9%83%A8&order=hot"

    def parse_url(self):
        response = requests.get(self.start_url)
        return response.content.decode()

    def get_content_list(self, html_url):  # 提取数据
        print(self.start_url)
        html = etree.HTML(html_url)
        print(html)
        div_list = html.xpath("//div[@class='bd']/dl[@class='f-cb']")  # 获取分组
        # print(div_list)
        content_list = []
        print("2")
        for li in div_list:
            item = {}
            title = li.xpath("./dt/text()")
            item[title] = li.xpath("./dd/a/text()")
            item[title] = [i for i in item[title]]
            content_list.append(item)
        print("3")
        return content_list

    def save_content_list(self, content_list):
        with open("files/wangyiyunmusic.txt", "w", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
            print("保存成功")


    def run(self):  # 实现主要逻辑
        # 1.start_url
        # 2.发送请求，获取响应
        html_url = self.parse_url()
        # 3.提取数据
        content_list = self.get_content_list(html_url)
        # 4.保存
        self.save_content_list(content_list)


if __name__ == '__main__':
    wangyiyun = WangyiyunSpider()
    wangyiyun.run()
