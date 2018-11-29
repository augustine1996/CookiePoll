# -*- coding: utf-8 -*-
import json
from lxml import etree
import requests
from requests.exceptions import ConnectionError
from cookiepool.db import *
import time


class ValidTester(object):
    def __init__(self, name='default'):
        self.name = name
        self.cookies_redis = CookieRedisClient(name=self.name)
        self.account_redis = AccountRedisClient(name=self.name)

    def test(self, username, cookies):
        raise NotImplementedError

    def run(self):
        accounts = self.cookies_redis.all()
        for account in accounts:
            username = account.get('username')
            cookies = self.cookies_redis.get(username)
            self.test(username, cookies)
            time.sleep(0.8)


class WeiboValidTester(ValidTester):
    def __init__(self, name='weibo'):
        super().__init__(name)

    def test(self, username, cookies):
        print('测试{}的Cookie信息：'.format(username))
        try:
            cookies = json.loads(cookies)
        except TypeError:
            # Cookie 格式不正确
            print('{}的Cookie格式不正确'.format(username))
            self.cookies_redis.delete(username)
            print('删除{}的Cookis'.format(username))
            return None
        try:
            response = requests.get('https://weibo.com/', cookies=cookies)
            if response.status_code == 200:
                html = response.text
                text = etree.HTML(html)
                inp = text.xpath('//title')[0]
                if inp.text.startswith('我的首页'):
                    print('{} 的Cookies可用'.format(username))
                else:
                    print('{}的Cookie已失效'.format(username))
                    self.cookies_redis.delete(username)
                    print('删除{}的Cookis'.format(username))
        except ConnectionError as e:
            print('Error', e.args)
            print('{}的Cookie已失效'.format(username))
            self.cookies_redis.delete(username)
            print('删除{}的Cookis'.format(username))
