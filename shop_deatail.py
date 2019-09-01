import requests
from bs4 import BeautifulSoup
import lxml
import json
import time
from requests.exceptions import RequestException

url = 'http://meishi.meituan.com/i/deal/114585'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
r = requests.get(url, headers=headers)
html = BeautifulSoup(r.text, 'lxml')
print(html)