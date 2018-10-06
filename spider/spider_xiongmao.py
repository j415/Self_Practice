# author: aspiring

from selenium import webdriver
import time
import json


class XiongmaoSpider:
    def __init__(self):
        self.start_url = "https://www.panda.tv/all"  # start_url
        self.driver = webdriver.Chrome()  # 实例化一个浏览器

    def get_content_list(self):  # 提取数据
        li_list = self.driver.find_elements_by_xpath("//ul[@id='later-play-list']/li")  # 分组
        content_list = []
        for li in li_list:
            item = {}
            item["name"] = li.find_element_by_xpath(".//span[@class='video-nickname']").get_attribute("title")
            item["title"] = li.find_element_by_xpath(".//span[@class='video-title']").text
            item["room_img"] = li.find_element_by_xpath(".//img[@class='video-img video-img-lazy']").get_attribute("data-original")
            item["watch_num"] = li.find_element_by_xpath(".//span[@class='video-number']").text
            print(item)
            content_list.append(item)  # 将字典放入逐条添加到一个列表内

        # 获取下一页元素
        next_url = self.driver.find_elements_by_xpath("//a[@class='j-page-next']")
        next_url = next_url[0] if len(next_url) > 0 else None

        return content_list, next_url

    def save_content_list(self, content_list):
        with open("files/xiongmao.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))  # 使用json将数据以json格式写入文件
                f.write("\n")

    def run(self):  # 实现主要逻辑
        # 1.start_url
        # 2.发送请求，获取响应
        self.driver.get(self.start_url)
        # 3.提取数据
        content_list, next_url = self.get_content_list()
        # 4.保存
        self.save_content_list(content_list)
        # 点击下一页元素
        while next_url is not None:
            next_url.click() # 点击下一页
            time.sleep(2)  # 睡2是为了下一页元素的载入缓冲时间，防止页面元素还没加载出来就去提取数据
            # 3.提取数据
            content_list, next_url = self.get_content_list()
            # 4.保存
            self.save_content_list(content_list)


if __name__ == '__main__':
    xiongmao = XiongmaoSpider()
    xiongmao.run()
