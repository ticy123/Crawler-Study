from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Brower:
    def __init__(self,condition):
        self.__driver = webdriver.Chrome()
        self.__condition = condition

    def search(self):
        print("开始进入b站首页...")
        self.__driver.get("https://www.bilibili.com/")
        sleep(5)
        print("开始获取搜索框...")
        input = self.__driver.find_element(By.CLASS_NAME, "nav-search-input")
        sleep(5)
        print("开始输入条件...")
        input.send_keys(self.__condition)
        sleep(2)
        print("开始搜索...")
        click = self.__driver.find_element(By.CLASS_NAME, "nav-search-btn")
        click.click()
        sleep(2)

    def get_search_info(self):
        self.search()
        print("获取源码并解析")
        handles = self.__driver.window_handles
        self.__driver.switch_to.window(handles[-1])
        html = self.__driver.page_source
        sleep(5)
        total_page = self.__driver.find_elements(By.CLASS_NAME,"vui_button vui_button--no-transition vui_pagenation--btn vui_pagenation--btn-num")[-1]
        a = 0

    def parse_html(self,pages):
        for p in range(1,pages + 1):
            pass



def main():
    brower = Brower("蔡徐坤篮球")
    brower.get_serach_html()

if __name__ == '__main__':
    pass
