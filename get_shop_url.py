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
import re
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import lxml

url = 'https://i.meituan.com/anshan/all/?p=1'
r = requests.get(url, verify=False)

# print(r.text)
html = BeautifulSoup(r.text, 'lxml')
items = html.findAll("dd")
urls = []
for item in items:
    for url in item.findAll("a"):
        if 'href' in url.attrs:
            urls.append({"url": url.attrs['href']})
print(urls)
# city_groups = html.findAll("span", {"class": "cities"})
# for city_group in city_groups:
#     print(city_group.get_text() + '\n')