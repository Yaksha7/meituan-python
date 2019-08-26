html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

import requests
import re
import json
from requests.exceptions import RequestException
import time

def get_city(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        return None
    except RequestException:
        return None


def get_city_parse(html):
    pattern = re.compile('<dd.*?<a.*?href="(.*?)".*?list-item>.*?>', re.S)
    #pattern = re.compile('<h4.*?A.*?href="(.*?)".*?>(.*?)</a>', re.S)
    results = re.findall(pattern, html)
    for result in results:
        yield{
            'url':result
        }

def write_to_file(content):
    with open('category_url.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main():
    for i in range(1,500):
        url = 'https://i.meituan.com/anshan/all/?p=' + str(i) + '&stid_b=3'
        html = get_city(url)
        #print(html)
        for item in get_city_parse(html):
            #print(item)
            write_to_file(item)

if __name__ == '__main__':
    main()
    time.sleep(1)

# print(type(r.text))
# print(r.text)
# print(type(r))
# print(r.status_code)