# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from urllib.parse import quote
#
# browser = webdriver.chrome()
# wait = WebDriverWait(browser, 10)
import requests
import json
import time
from bs4 import BeautifulSoup
import lxml
from requests.exceptions import RequestException

def get_city(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }
    try:
        r = requests.get(url, headers=headers, verify=False)
        if r.status_code == 200:
            return r.text
        return None
    except RequestException:
        return None
# url = 'https://www.meituan.com/changecity/'
# r = requests.get(url, verify=False)
def get_city_parse(html):
    BsObj = BeautifulSoup(html, 'lxml')
    #print(BsObj)
    city_groups = []
    for span in BsObj.findAll("span", {"class": "cities"}):
        for city_group in span.findAll("a"):
            if 'href' in city_group.attrs:
                city_groups.append({city_group.get_text(): city_group.attrs['href']})
    return city_groups

def get_city_pinyin(html):
    BsObj = BeautifulSoup(html, 'lxml')
    scripts = []
    a = BsObj.findAll('script')
    for script in a:
        # print(script)
        scripts.append(script)
    b = scripts[9].get_text().strip()
    c = b[17:-1]
    d = json.loads(c, encoding='utf-8')
    e = d['openCityList']
    return e
    # for i in range(0, 22):
    #     lists = e[i][1]
    #     #return lists
    #     for list in lists:
    #         #f = {list['pinyin']: list['name']}
    #         return list

def write_to_file(content):
    with open('cities.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def write_to_file_1(content):
    with open('city_pinyin.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main():
    url = 'https://www.meituan.com/changecity/'
    html = get_city(url)
    for item in get_city_parse(html):
        #print(item)
        write_to_file(item)

    for i in range(0, 22):
        lists = get_city_pinyin(html)[i][1]
        #return lists
        for list in lists:
            f = {list['pinyin']: list['name']}
            write_to_file_1(f)
            #print(get_city_pinyin(html))
    #for city_pinyin in get_city_pinyin(html):
        #print(city_pinyin['pinyin'])
        #write_to_file_1(get_city_pinyin(html))

if __name__ == '__main__':
    main()
    time.sleep(1)