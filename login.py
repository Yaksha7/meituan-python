import json

with open('city_pinyin.txt', 'r', encoding='UTF-8') as f:
    cities = []
    for line in f.readlines():
        a = json.loads(line)
        for keys, values in a.items():
            cities.append(values)
            for city in cities:
                print(city)