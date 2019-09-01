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
    try:
        r = requests.get(url, verify=False)
        if r.status_code == 200:
            return r.text
        return None
    except RequestException:
        return None
# url = 'https://www.meituan.com/changecity/'
# r = requests.get(url, verify=False)
def get_city_parse(html):
    BsObj = BeautifulSoup(html, 'lxml')
    print(BsObj)
    city_groups = []
    for span in BsObj.findAll("span", {"class": "cities"}):
        for city_group in span.findAll("a"):
            if 'href' in city_group.attrs:
                city_groups.append({city_group.get_text(): city_group.attrs['href']})
    return city_groups

def write_to_file(content):
    with open('cities.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main():
    url = 'https://www.meituan.com/changecity/'
    html = get_city(url)
    #BsObj = BeautifulSoup(html, 'lxml')
    #print(html)
    for item in get_city_parse(html):
        #print(item)
        write_to_file(item)

if __name__ == '__main__':
    main()
    time.sleep(1)