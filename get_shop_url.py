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

url = 'https://www.meituan.com/changecity/'
r = requests.get(url, verify=False)
html = BeautifulSoup(r.text, 'lxml')
city_groups = html.findAll("span", {"class": "cities"})
for city_group in city_groups:
    print(city_group.get_text() + '\n')