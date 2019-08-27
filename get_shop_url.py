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

url = 'https://www.meituan.com/changecity/'
r = requests.get(url, verify=False)
html = pq(r.text)
cities = html('.cites a').items()
for city in cities:
    print(city)