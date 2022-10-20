import requests
from bs4 import BeautifulSoup
import xlwt

def get_page_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    with requests.get(url,headers=headers) as rep:
        try:
            if rep.status_code == 200:
                return rep.text
        except requests.RequestException:
            return None


def parse_html(html):
    move_list = BeautifulSoup(html,'lxml').find(class_= 'grid_view').find_all('li')
    for item in move_list:
        rank = item.find(class_="pic").find(class_="").string
        name = item.find(class_="title").string
        pic =item.find("a").find("img").get("src")
        dire= item.find("p").text.split("导演: ")[1].split("\xa0\xa0\xa0")[0]
        star = item.find(class_='rating_num').string
        yield   {
            "rank":rank,
            "name":name,
            "pic":pic,
            "dire":dire,
            "star":star
        }


def save_to_excel(items):
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet("豆瓣电影250",cell_overwrite_ok=True)
    sheet.write(0,0,'排名')
    sheet.write(0,1,'名称')
    sheet.write(0,2,'图片')
    sheet.write(0,3,'导演')
    sheet.write(0,4,'评分')
    for item in items:
        row = int(item["rank"])
        sheet.write(row,0,item["rank"])
        sheet.write(row,1,item["name"])
        sheet.write(row,2,item["pic"])
        sheet.write(row,3,item["dire"])
        sheet.write(row,4,item["star"])
    book.save(u"豆瓣受欢迎的250部电影.xlsx")



def main(page):
    url = f"https://movie.douban.com/top250?start={page * 25}&filter="
    html = get_page_html(url)
    items = parse_html(html)
    return items
    # save_to_excel(items)



if __name__ == '__main__':
    movies = []
    for page in range(10):
        movies += main(page)
    save_to_excel(movies)