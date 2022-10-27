import requests
import re

from common.utils import timing

pre_url = f"http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


def get_page_html(url):
    with requests.get(url) as rep:
        try:
            if rep.status_code == 200:
                return rep.text
        except requests.RequestException:
            return None


def parse_html(html):
    # pattern = re.compile('<li>.*?list_num.*?(d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><spansclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
    pattern = re.compile("""<div class="list_num.*?">(?P<id>.*?).</div>.*?<img src="(?P<pic>.*?)".*?</a></div>""",re.S)

    return re.finditer(pattern, html)

@timing
def main(pages = 10):
    for page in range(1, pages):
        url = f"{pre_url}{page}"
        html = get_page_html(url)
        items = parse_html(html)
        for item in items:
            print(f'{item.group("id")}  {item.group("pic")}')

if __name__ == '__main__':
    main()
