import requests
import re
import json
from requests.exceptions import RequestException
import time
from bs4 import BeautifulSoup

url = 'https://as.meituan.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
html = requests.get(url, headers=headers).text
page = BeautifulSoup(html, 'lxml')
categorys = []
for li in page.findAll("li", {"class": "nav-li"}):
    for category in li.findAll('a'):
        if 'href' in category.attrs:
            categorys.append(category.attrs['href'])
            print(category.attrs['href'])
print(categorys)
# def get_city():
#     try:
#         url = 'https://i.meituan.com/anshan/all/?p=1'
#         r = requests.get(url)
#         if r.status_code == 200:
#             return r.text
#         return None
#     except RequestException:
#         return None
#
#
# def get_city_parse(html):
#     pattern = re.compile('<dd.*?<a.*?href="(.*?)".*?list-item.*?>', re.S)
#     results = re.findall(pattern, html)
#     for result in results:
#         # print(result)
#         yield{
#             'url': result
#         }
#
# def get_next_page(url):
#     page = get_city(url)
#     pattern = re.compile('<span.*?pager-current.*?<a.*?href="(.*?)".*?</a>', re.S)
#     page = re.findall(pattern, page)
#
# def write_to_file(content):
#     with open('category_url.txt', 'a', encoding='utf-8') as f:
#         f.write(json.dumps(content, ensure_ascii=False) + '\n')
#
# def main():
#     for i in range(1,2):
#
#         url = 'https://i.meituan.com/anshan/all/?p=' + str(i) + '&stid_b=3'
#         print(i)
#         html = get_city(url)
#         #print(html)
#         for item in get_city_parse(html):
#             print(item)
#             write_to_file(item)
#
# if __name__ == '__main__':
#     main()
#     time.sleep(1)