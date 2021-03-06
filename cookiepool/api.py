# -*- coding: utf-8 -*-
from flask import Flask, g
from .setting import *
from .db import CookieRedisClient, AccountRedisClient

app = Flask(__name__)
__all__ = [app]


@app.route('/')
def index_views():
    return "<h1 style='text-align: center;'>Welcome to CookiePool</h1>"


def get_conn():
    """
    获取
    :return:
    """
    for name in GREATOR_MAP:
        print(name)
        if not hasattr(g, name):
            setattr(g, name + '_cookie', eval('CookieRedisClient' + '(name="' + name + '")'))
            setattr(g, name + '_account', eval('AccountRedisClient' + '(name="' + name + '")'))
    return g


@app.route('/<name>/random')
def random(name):
    """
    获取随机的Cookie, 访问地址如 /weibo/random
    :return: 随机Cookie
    """
    g = get_conn()
    cookies = getattr(g, name + '_cookie').random()
    return cookies


@app.route('/<name>/add/<username>/<password>')
def add(name, username, password):
    """
    添加用户, 访问地址如 /weibo/add/user/password
    """
    g = get_conn()
    result = getattr(g, name + '_account').set(username, password)
    if result:
        return '添加用户信息成功'
    return '添加信息失败'


@app.route('/<name>/count')
def count(name):
    """
    获取Cookies总数
    """
    g = get_conn()
    count = getattr(g, name + '_cookie').count()
    return str(count) if isinstance(count, int) else count
