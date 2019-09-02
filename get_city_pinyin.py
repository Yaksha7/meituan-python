import requests
import json
import time
from bs4 import BeautifulSoup
import lxml
import re
from requests.exceptions import RequestException
url = 'https://www.meituan.com/changecity/'
headers = {
'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}
r = requests.get(url, headers=headers, verify=False).text
BsObj = BeautifulSoup(r, 'lxml')
scripts = []
a = BsObj.findAll('script')
for script in a:
    #print(script)
    scripts.append(script)
b = scripts[9].get_text().strip()
c = b[17:-1]
d = json.loads(c, encoding='utf-8')
e = d['openCityList']
for i in range(0,22):
    lists = e[i][1]
    for list in lists:
        f = {list['pinyin']: list['name']}
print(f)
    #print({e[i][1][0]['pinyin']: e[i][1][0]['name']})
# f = json.loads(e, encoding='utf-8')
# print(f)
# print(scripts)
# BsObj = BeautifulSoup(r, 'lxml')
# pattern = re.compile('<script>window.AppData.*?openCityList.*?name:":"(.*?)".*?pinyin":"(.*?)"', re.S)
# results = re.findall(pattern, r)
# for result in results:
#     yield{
#         'name': result[0],
#         'pinyin': result[1]
#     }

# import json
# from pyquery import PyQuery as pq
# import requests
#
# url = 'https://www.meituan.com/changecity/'
# doc = pq(requests.get(url).text)
# cities = doc('.cities a').items()
# print(cities)
# cities_dict = dict()
# for city in cities:
#     #print(city)
#     a = city.attr('href').replace('.', '/').split('/')[2]
#     print(a)
#     cities_dict.update({city.text(): city.attr('href').replace('.', '/').split('/')[2]})
# print(cities_dict)
# with open(city_code.txt, 'w', encoding='utf-8') as f:
# 	f.write(json.dumps(cities_dict, indent=2, ensure_ascii=False))