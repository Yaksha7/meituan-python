import requests
from bs4 import BeautifulSoup
import lxml
import json
import time
from requests.exceptions import RequestException
from urllib.parse import urlencode

def get_city(url):

    try:
        r = requests.get(url, verify=False)
        if r.status_code == 200:
            return r.text
        return None
    except RequestException:
        return None

# url = 'https://i.meituan.com/anshan/all/?p=1'
# r = requests.get(url, verify=False)

# print(r.text)
def get_city_parse(html):
    page = BeautifulSoup(html, 'lxml')
    items = page.findAll("dd")
    urls = []
    for item in items:
        for url in item.findAll("a"):
            if 'href' in url.attrs:
                urls.append(url.attrs['href'])
    return urls

def write_to_file(content):
    with open('shops.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(page):
    params = {
        'cityName': '青岛',
        'cateId': 0,
        'areaId': 0,
        'sort': '',
        'dinnerCountAttrId': '',
        'page': 1,
        'userId': '',
        'uuid': 'c616858a316245f1b52b.1567061944.1.0.0',
        'platform': 1,
        'partner': 126,
        'originUrl': 'https://qd.meituan.com/meishi/',
        'riskLevel': 1,
        'optimusCode': 10,
        '_token': 'eJx1kM1uozAUhd/FW1DA4BASqYv8QCgTAjjBbWfUBSQBTAllwIZA1Xevq+lIncWszrnfPTq69hto7s9gAVV1rqoy6C4NWAA4UScGkAFrxWZqzJCJ5joy9KkMTv8yE+oySBqyAYtfUDcMGaoaev5EWJDv6LvXkPwndS9CIGesbheK8vs8uV4o43E1Ob1eFeHbnCrijP8EgGi4HkWD0Jcvjb+U/Z098RxR0dKsEu7i9mVxZLwflyH2JZpRYg/5rlhtl5gvX8M68FaxY7PdwZU6u9+am8fTtimtWR1S1uc5Ubz+ainVej8kTG28glurwT0FtrmRUjJXUm22fkK3JYdh0Y3ucUA02kYe49JxFdPogMKqqMp45vnpoHbnatd7GbmlZWXtUr4en6h085vz2uIWjANMMTFTB/9wfub+4+gk0ywh/aHFD7APtI50WNuLj6kNPYk3vqdCK625lc0fDpdy7wRooJDYLlRQZOIxugPvH9IIlbI='
    }
    #print(page)
    url = 'https://qd.meituan.com/meishi/api/poi/getPoiList?' + urlencode(params)
    html = get_city(url)
    #BsObj = BeautifulSoup(html, 'lxml')
    #print(html)
    for item in get_city_parse(html):
        if 'p=' not in item:
        #print(item)
            write_to_file(item)

if __name__ == '__main__':
    for i in range(301):
        main(i)
        time.sleep(1)
# city_groups = html.findAll("span", {"class": "cities"})
# for city_group in city_groups:
#     print(city_group.get_text() + '\n')