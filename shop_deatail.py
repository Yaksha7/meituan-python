import requests
from bs4 import BeautifulSoup
import lxml
import json
import time
from requests.exceptions import RequestException

proxy = '18218147779:quan381104156@123.101.141.46:9999'
proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
url = 'http://meituan.com/meishi/6690007/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
r = requests.get(url, headers=headers, proxies=proxies)
html = BeautifulSoup(r.text, 'lxml')
print(html)