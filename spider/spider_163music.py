# author:aspiring


from selenium import webdriver
import json


class Music163_Spider:
    def __init__(self):
        self.start_url = "https://music.163.com/#/discover/toplist"
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//tbody/tr")
        content_list = []
        for li in li_list:
            item = {}
            item["num"] = li.find_element_by_xpath(".//span[@class='num']").text
            item["songer"] = li.find_element_by_xpath(".//div[@class='text']").get_attribute("title")
            item["song"] = li.find_element_by_xpath(".//b").get_attribute("title")
            item["song_time"] = li.find_element_by_xpath(".//span[@class='u-dur ']").text
            print(item)
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):
        with open("files/music163.txt", "w", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")
        print("保存成功")

    def run(self):  # 实现主要逻辑
        # 1.start_url
        # 2.发送请求，获取响应
        self.driver.get(self.start_url)
        self.driver.switch_to.frame("g_iframe")  # 切换到iframe
        # 3.提取数据
        content_list = self.get_content_list()
        # 4.保存
        self.save_content_list(content_list)

        # 退出实例浏览器
        self.driver.quit()


if __name__ == '__main__':
    music163 = Music163_Spider()
    music163.run()
