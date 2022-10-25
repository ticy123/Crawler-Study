import xlwt
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from retrying import retry
import os
# # 杀死进程
os.system("taskkill /f /im chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",Connection="close"')
chrome_options.add_argument('blink-settings=imagesEnabled=false')#禁用图片
chrome_options.page_load_strategy = 'eager'
class Brower:

    def __init__(self, condition, limit=99999999):
        self._driver = webdriver.Chrome(options=chrome_options)
        self._wait = WebDriverWait(self._driver, 15)
        self._condition = condition
        self._limit=limit
        self._items = []

    @property
    def limit(self):
        return self._limit

    @property
    def driver(self):
        return self._driver

    @property
    def wait(self):
        return self._wait

    @property
    def condition(self):
        return self._condition

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items.append(value)

    @retry(stop_max_attempt_number=2, wait_fixed=3000)
    def search(self):
        print("开始进入b站首页...")
        self.driver.get("https://www.bilibili.com/")
        print("开始获取搜索框...")
        input = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nav-search-input")))
        print("开始输入条件...")
        input.send_keys(self._condition)
        print("开始搜索...")
        self.driver.find_elements()
        all_handles = self.driver.window_handles
        click = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-search-btn")))
        click.click()
        # 等待新窗口打开
        print("等待窗口打开....")
        self.wait.until(EC.new_window_is_opened(all_handles))

    def get_all_pages(self):
        self.search()
        print("获取源码并解析")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        total_page = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="vui_pagenation--btns"]/button[last()-1]')))
        print(f"总页数为:{total_page.text}")
        return total_page.text

    def quit(self):
        self.driver.close()#关闭当前窗口
        self.driver.quit()#关闭所有窗口

    def parse_html(self, pages):
        for page in range(1, pages+1):
            print(f"开始解析第{page}页...")
            html = self.driver.page_source
            movie_list = BeautifulSoup(html, 'lxml').find_all(name="div", attrs={"class": "bili-video-card__info __scale-disable"})
            for item in movie_list:
                name = item.find("h3").get("title")
                src = item.find(class_='bili-video-card__info--right').find("a").get("href")
                self.items.append({
                    "name": name,
                    "src": src
                })
            if page < pages:
                next_page = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="vui_pagenation--btns"]/button[last()]')))
                print(f"解析结束,进入下一页")
                next_page.click()
                handles = self.driver.window_handles
                self.driver.switch_to.window(handles[-1])
            else:
                print("已在最后一页,全部解析结束")
                return

    def save_to_excel(self):
        print("开始保存为Excel...")
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = book.add_sheet(self.condition, cell_overwrite_ok=True)
        sheet.write(0,0,"名称")
        sheet.write(0,1,"资源地址")
        for index,item, in enumerate(self.items):
            sheet.write(index+1,0,item["name"])
            sheet.write(index+1,1,item["src"])
        book.save(f"{self.condition}.xlsx")
        print("已全部保存为Excel,准备退出程序....")




def main():
    try:
        brower = Brower("java相关资源推荐",10)
        pages = min((int(brower.get_all_pages()),brower.limit))
        brower.parse_html(pages)
        brower.save_to_excel()
    except Exception as e:
        print(e)
    finally:
        brower.quit()



if __name__ == '__main__':
    main()
