import requests
from bs4 import BeautifulSoup
import lxml
import json
import time
from requests.exceptions import RequestException
from urllib.parse import urlencode

params = {
        'cityName': '青岛',
        'cateId': 0,
        'areaId': 0,
        'sort': '',
        'dinnerCountAttrId': '',
        'page': 1,
        'userId': '236535115',
        'uuid': '4cbc619a4c2340bb84bc.1567570779.1.0.0',
        'platform': 1,
        'partner': 126,
        'originUrl': 'https://qd.meituan.com/meishi/',
        'riskLevel': 1,
        'optimusCode': 10,
        '_token': 'eJxVkNFumzAARf/FD3sJCgYMhEjTFArbSJMSCklKpmkCY4hTIMTYIUm1f5+ntlL7dK+vz8OxXwALCjDVIHQgVMCZMDAF2hiOLaAA3ssb07JNW9dNB1qaAvDnTTMcBeRs44HpL82wLEWDOvr9f3qUy8fpY9eR8koFEgJ7zrt+qqqnYtwQykXWjvGxUWXv91TtWl2VKu9Ql/V9d2T8E5phfBQtV3uCj20h30DL6zdGJNj25A8+FuQr1IhpwUluwglCBSR5WZYos4zMyLNSJ+UXRk6C9PyVJpMSEumqIQMhHRo5hsjIECFOoRcOIkDKN4mUl/n8ltlb8vfzUv6kNO9p1cpG5kN9S3joen7kPtzZeehF50u76v0qhP4uoMHgkfDScPvp4BlpTrciCqjtthFF7nrnO+k81vD3DV6VbizSYkhGkbE3C3d1vo1K23Gwf9dViVb/FDS0Aiukw9PAD/l9RIaYzfEkvXUnYutRnWTscXau1sXMoualtZZpvsfr+bZ16UF4Wrw8HTYNc5aLe1tUpqZXm5NDhafO7keGt6jjG/NKNHLyOL3G+3obTlI7HIyzRQ+NrZMdq/mDumpEslhkdWayZyJEmFwnM/4D+70P/v4DwUfCdA=='
    }
    #print(page)

headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_lxsdk_cuid=16c4b9f13d7c8-0c17e1cb45fd8f-c343162-144000-16c4b9f13d7c8; rvct=60%2C197%2C1; iuuid=8113DB0E3DA03E5994CDB6BBFC762FDCA4EB25E21481B4ECE3253168F1DCEB81; _lxsdk=8113DB0E3DA03E5994CDB6BBFC762FDCA4EB25E21481B4ECE3253168F1DCEB81; _hc.v=9cb58b8d-67a3-eb79-f4ec-86afda73b704.1564653381; __utmz=74597006.1565832626.7.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; a2h=4; cityname=%E9%9E%8D%E5%B1%B1; mtcdn=K; lsu=; webp=1; __utma=74597006.739706182.1564653304.1567397719.1567484632.20; i_extend=H__a100001__b20; latlng=36.078829,120.388789,1567484886315; ci=60; client-id=df464bca-ace0-4a7e-ac9f-2e9548fe949e; uuid=4cbc619a4c2340bb84bc.1567570779.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=55425556.1564653277490.1567484921701.1567570782360.3; userTicket=lWRzlGJBHCRnVRVpJskTVCwqmYzwddKThTclKlMM; u=236535115; n=Yaksha%E4%B8%B6; token2=vTG3DyIuyvg4ydKbttBVk02w-14AAAAA-ggAAGEiXg2eiLx1KkhIFR6CjwPEkVkey7xMdN7adQRdJgXAznkSnRc4jcNPy8IM3dPe6w; lt=vTG3DyIuyvg4ydKbttBVk02w-14AAAAA-ggAAGEiXg2eiLx1KkhIFR6CjwPEkVkey7xMdN7adQRdJgXAznkSnRc4jcNPy8IM3dPe6w; unc=Yaksha%E4%B8%B6; _lxsdk_s=16cfac33a8a-92c-490-bfc%7C%7C3',
    'Host': 'qd.meituan.com',
    'Referer': 'https://qd.meituan.com/meishi/pn2/',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}
url = 'https://qd.meituan.com/meishi/api/poi/getPoiList?' + urlencode(params)

response = requests.get(url, headers=headers, verify=False)
print(response.status_code)
# shops = r.json()
# print(shops('data'))