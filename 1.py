import requests
import json
import time
from bs4 import BeautifulSoup
import lxml
import re
from requests.exceptions import RequestException
url = 'https://www.meituan.com/changecity/'
r = requests.get(url, verify=False).text
# BsObj = BeautifulSoup(r, 'lxml')
pattern = re.compile('<script>window.AppData.*?openCityList.*?name:":"(.*?)".*?pinyin":"(.*?)"', re.S)
results = re.findall(pattern, r)
for result in results:
    yield{
        'name': result[0],
        'pinyin': result[1]
    }