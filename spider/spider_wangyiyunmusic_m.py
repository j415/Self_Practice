# author:aspiring


import requests
from lxml import etree
import json


class M163Spider:
    def __init__(self):
        self.start_url = "https://music.163.com/m/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    def parse_url(self):
        response = requests.get(self.start_url, headers=self.headers)
        # print(response)
        return response.content.decode()

    def get_content_list(self, html_str):
        # print(html_str)
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@class='m-sglst']/a")
        print("***", div_list)
        content_list = []
        for div in div_list:
            item = {}
            item["order"] = div.xpath("./div[@class='sgfl sgfl-cred']/text()")
            item["song_name"] = div.xpath(".//div[@class='f-thide sgtl']/text()")
            item["detail"] = div.xpath(".//div[@class='f-thide sgtl']//text()")
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):
        with open("files/music_163.txt", "w", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")
        print("保存成功")

    def run(self):  # 实现主要逻辑
        # 1.strat_url
        # 2.发送请求，获取响应
        html_str = self.parse_url()
        # 3.提取数据
        content_list = self.get_content_list(html_str)
        # 4.保存
        self.save_content_list(content_list)


if __name__ == '__main__':
    music_163 = M163Spider()
    music_163.run()
