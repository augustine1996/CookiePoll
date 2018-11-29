# -*- coding: utf-8 -*-
import redis
from cookiepool.setting import *
import random


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host, port=port, password=password)
        self.domain = REDIS_DOMAIN
        self.name = REDIS_NAME

    def get_key(self, key):
        """
        获得格式化后的键名
        """
        return "{domain}:{name}:{key}".format(domain=self.domain, name=self.name, key=key)

    def set(self, key, value):
        """
        把键值对保存进数据库
        :param key:键名
        :param value:键值
        """
        raise NotImplementedError

    def get(self, key):
        """
        根据键名取得键值
        :param key: 键名
        """
        raise NotImplementedError

    def delete(self, key):
        """
        根据键名删除数据库中的数据
        :param key:键名
        """
        raise NotImplementedError

    def get_keys(self):
        """
        获得所有的键名
        """
        return self.db.keys('{domain}:{name}:*'.format(domain=self.domain, name=self.name))

    def flushall(self):
        """
        清空数据库
        """
        self.db.flushall()


class AccountRedisClient(RedisClient):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, domain='account', name='default'):
        super().__init__(host, port, password)
        self.domain = domain
        self.name = name

    def set(self, key, value):
        return self.db.set(self.get_key(key), value)

    def get(self, key):
        return self.db.get(self.get_key(key)).decode('utf-8')

    def delete(self, key):
        return self.db.delete(self.get_key(key))

    def all(self):
        for key in self.get_keys():
            group = key.decode('utf-8').split(":")
            if len(group) == 3:
                username = group[2]
                yield {
                    'username': username,
                    'password': self.get(username)
                }


class CookieRedisClient(RedisClient):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, domain='cookie', name='default'):
        super().__init__(host, port, password)
        self.domain = domain
        self.name = name

    def set(self, key, value):
        return self.db.set(self.get_key(key), value)

    def get(self, key):
        return self.db.get(self.get_key(key)).decode('utf-8')

    def delete(self, key):
        return self.db.delete(self.get_key(key))

    def all(self):
        for key in self.get_keys():
            group = key.decode('utf-8').split(":")
            if len(group) == 3:
                username = group[2]
                yield {
                    'username': username,
                    'cookie': self.get(username)
                }

    def random(self):
        keys = self.get_keys()
        res = self.db.get(random.choice(keys)).decode('utf-8')
        return res

    def count(self):
        return len(self.get_keys())
