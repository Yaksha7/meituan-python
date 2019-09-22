import requests
from bs4 import BeautifulSoup
import lxml
import json
import time
from requests.exceptions import RequestException
from urllib.parse import urlencode

def get_city(page, city):
    proxy = '18218147779:quan381104156@123.101.141.46:9999'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'iuuid=CFAE3B470A1F80B4D7C7BC658D2B8D38382CE891323DFF9333978C3D338869AC; _lxsdk_cuid=16cc6c1849f6c-0beb5e26d8ad7f-7373e61-144000-16cc6c184a0c8; _lxsdk=CFAE3B470A1F80B4D7C7BC658D2B8D38382CE891323DFF9333978C3D338869AC; webp=1; __utmz=74597006.1566702667.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cityname=%E9%9E%8D%E5%B1%B1; _hc.v=475771b6-9612-da2e-7506-680f1d29407a.1566705266; a2h=4; __utma=74597006.1755981119.1566702667.1567323028.1567323129.7; i_extend=H__a100001__b7; uuid=4b0b141df32342e9b649.1567935195.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; client-id=9fd7f393-ea75-48d7-a712-21483755d239; mtcdn=K; lat=36.169136; lng=120.426643; u=236535115; n=Yaksha%E4%B8%B6; lt=offCndiK44GkoZRrP1_A1M0PODwAAAAADwkAAK9jPT8Pz3edhJHQ2DnnNEbHnfdqrTHpvS25dKUb9TgAgpvMtW4JY-PQEq4lRegyFw; lsu=; token2=offCndiK44GkoZRrP1_A1M0PODwAAAAADwkAAK9jPT8Pz3edhJHQ2DnnNEbHnfdqrTHpvS25dKUb9TgAgpvMtW4JY-PQEq4lRegyFw; unc=Yaksha%E4%B8%B6; ci=60; rvct=60%2C664%2C1283%2C1%2C151%2C675; __mta=51276182.1567935218963.1567935218963.1567951847038.2; _lxsdk_s=16d112746b8-43d-e2d-941%7C%7C13',
        'Host': 'qd.meituan.com',
        'Referer': 'https://qd.meituan.com/meishi/',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }
    params = {
        'cityName': city,
        'cateId': 0,
        'areaId': 0,
        'sort': '',
        'dinnerCountAttrId': '',
        'page': page,
        'userId': '236535115',
        'uuid': '4b0b141df32342e9b649.1567935195.1.0.0',
        'platform': 1,
        'partner': 126,
        'originUrl': 'https://qd.meituan.com/meishi/',
        'riskLevel': 1,
        'optimusCode': 10,
        '_token': 'eJx1j8uSokAQRf+lthBWFW+NmAWjIs8OBcTHRC+wUCkRBApEe2L+faqj7cUsZnVvnsy8kfkbtE4GJhihMUIiuB9bMAF4hEYaEEHHeEfV9LGKDVVGkiIC8i/DmC8d2mQGJr+wKmuirOP3TxJy8EUMTXkXX1bilqd8Cjg4fATkXVezCYRNNiqPtOvTakRuJeSe5RTyG/4zAHhCGfMErsVL05d233XAf+ERjJ4r7o7ucL2scT9czFV+hNOhuNtx752TpTNlab3OCPlpzz7Mxp9nj/7N2zpBp+Q+oauNPFjJVh8vYwEXqnk/1W3o6g9oLp9udreMqaB3p0p57ozHmaI42j7z+tqETWQF+8iIQ40l1Anti92n/q5SaQLfAnn/HGbOY71RY21RV3O4o8E6S7W5R/YS6nN5HlyY4Jpt4rIBbqHpE2FDqIdui5MuSKUyVJmdUstfSbIaFYKGl3LYYZ0McRHAqJQW4ySf3VQr9Zrr5jBkLIrPP8Cfv4I+lZ8='
    }
    url = 'https://qd.meituan.com/meishi/api/poi/getPoiList?' + urlencode(params)
    print(url)
    try:
        response = requests.get(url, headers=headers, proxies=proxies, verify=False)
        if response.status_code == 200:
            print(response)
            return response
    except RequestException:
        return None

# def get_pages(html):
#     shops = html.json()
#     pages = shops['data']['totalCounts']
#     return pages

def get_city_parse(html):
    shops = html.json()
    # pages = shops['data']['totalCounts']
    items = shops['data']['poiInfos']
    return items

def write_to_file(content):
    with open('shop_url.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(pages):
    for page in range(pages+1):
        with open('city_pinyin.txt', 'r', encoding='UTF-8') as f:
            cities = []
            for line in f.readlines():
                a = json.loads(line)
                for keys, values in a.items():
                    cities.append(values)
                    for city in cities:
                        #print(city)
                        html = get_city(page, city)
                        items = get_city_parse(html)
                        if items:
                            for item in items:
                                shop_id = item['poiId']
                                shop_url = 'https://www.meituan.com/meishi/' + str(shop_id)
                                write_to_file(shop_url)

if __name__ == '__main__':
    #print(url)
    response = get_city(1)
    #print(pages)
    result = response.json()
    print(result)
    pages = result['data']['totalCounts']
    counts = pages//15
    # print(type(pages))
    main(counts)