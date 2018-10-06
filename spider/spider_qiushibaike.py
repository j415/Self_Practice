# author:aspiring


import requests
import json
from lxml import etree


class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    def url_list(self):
        return [self.url_temp.format(i) for i in range(1,14)]

    def parse_url(self,url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_url):
        html = etree.HTML(html_url)
        div_list = html.xpath("//div[@id='content-left']/div")
        # print(div_list)
        content_list = []
        for list in div_list:
            item = {}
            item["author"] = list.xpath(".//h2/text()")[0].replace("\n", "")
            # item["author"] = [i.replace("\n", "") for i in item["author"]]
            print(item["author"])
            # item["author_gender"] = list.xpath(".//div[contains(@class,'articleGender')]/@class")
            # item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon","")
            item["author_gender"] = list.xpath(".//div[contains(@class,'articleGender')]/@class")
            item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon", "") if len(
                item["author_gender"]) > 0 else None
            # print(item["author_gender"])
            # item["content"] = list.xpath(".//div[@class='content']/span/text()")
            # item["content"] = [i.replace("\n", "") for i in item["content"]]

            item["content"] = list.xpath(".//div[@class='content']/span/text()")[0].replace("\n", "")
            # item["content"] = [i.replace("\n", "") for i in item["content"]]
            # print(item["content"])
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):  # 保存
        with open("files/qiushibaike.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=4))
                f.write("\n")
        print("保存成功")

    def run(self):  # 实现主要逻辑
        # 1.start_url
        # 2.发送请求，获取响应
        url_list = self.url_list()
        for url in url_list:
            html_url = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_content_list(html_url)
            # 4.保存
            self.save_content_list(content_list)


if __name__ == '__main__':
    qiubai = QiubaiSpider()
    qiubai.run()
