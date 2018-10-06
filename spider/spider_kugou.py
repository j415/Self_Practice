# author:aspiring


import requests
import json
from lxml import etree


class KugouSpider:
    def __init__(self):
        self.start_url = "http://www.kugou.com/yy/html/rank.html"

    def parse_url(self):
        response = requests.get(self.start_url)
        return response.content.decode()

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@class='pc_temp_side']")
        print(div_list)
        content_list = []
        for list in div_list:
            print("***",list)
            for li in list:
                # //div[@class="pc_temp_side"]//h3/a/@title
                print("###", li)
                item = {}
                item["title"] = li.xpath("./h3/a/@title")
                print("$$$",item["title"])
                content_list.append(item)

    # def save_content_list(self, content_list):
    #     with open("files/kugou.txt", "w", encoding="utf-8") as f:
    #         for content in content_list:
    #             f.write(json.dumps(content, ensure_ascii=False))
    #             f.write("\n")
    #         print("保存成功")

    def run(self):  # 实现主要逻辑
        # 1.start_url
        # 2.发送请求，获取响应
        html_str = self.parse_url()
        # 3.提取数据
        content_list = self.get_content_list(html_str)
        # 4.保存
        # self.save_content_list(content_list)


if __name__ == '__main__':
    kugou = KugouSpider()
    kugou.run()
