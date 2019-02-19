# -*- coding: utf-8 -*-

"配置代理"

import requests
import config
import pymysql
import json
import random
import time

db = pymysql.connect(host='192.168.1.100', port=3306, user='root', passwd='123123', db='proxies',
                     charset='utf8')
cursor = db.cursor()

#proxy = {'https':'https://172.106.164.151:8082'}
# 抓取免费代理
def fetch():
    cursor.execute('SELECT COUNT(*) AS count FROM `proxy` WHERE `is_valid` = 1')
    count=cursor.fetchone()[0]  #可用的代理ip数量
    if count > 5000:
        print('代理IP超出5000 暂时不需要再抓取')
    else:
        req = requests.get('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list')
        response = req.text
        #js = json.loads(response)
        responseJsonList = response.splitlines()
        proxyList = []
        for val in responseJsonList:
            array = json.loads(val)
            if array['type'] == 'https':
                proxy_ip = 'https://' + str(array['host']) + ':' + str(array['port'])
                proxyList.append(proxy_ip)
        #返回所有的代理ip
        return proxyList[:]

proxyList = fetch()
proxy_len = len(proxyList)
proxy_random = random.randint(0,proxy_len-1)
proxy = {'https': proxyList[proxy_random]}
#proxy = {}
#print proxy

def change_proxy():
    proxy_random = random.randint(0, proxy_len - 1)
    proxy = {'https': proxyList[proxy_random]}
    return proxy

'''
while True:
    proxy = {'https': proxyList[proxy_random]}
    print proxy
    headers = config.headers
    token = '0a4d4efa568303b11774a8b8df601921'
    try:
        js = requests.get('https://xcx.qichacha.com/wxa/v1/base/getMoreEntInfo?unique=7f3e39410189a22878048e9d09b6570d&token=%s' %(token),headers = headers,proxies=proxy,timeout=2)
    except:
        proxy_random = random.randint(0, proxy_len - 1)
        proxy = {'https': proxyList[proxy_random]}
        continue
    js = js.text
    print js
    time.sleep(2)
'''






