# -*- coding: utf-8 -*-
from urllib import request
import json
def fetch_data(url):
    req = request.Request(url)

    with request.urlopen(req) as f:
        #print('Status:', f.status, f.reason)
        #for k, v in f.getheaders():
        #   print('%s: %s' % (k, v))
        data=json.loads(f.read().decode('utf-8'))
        print(type(data))
        return data
# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
