import requests
from bs4 import BeautifulSoup
import lxml
import json
import time
from requests.exceptions import RequestException

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
    print(page)
    url = 'https://i.meituan.com/anshan/all/?p=' + str(page)
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