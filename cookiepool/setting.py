# -*- coding: utf-8 -*-

# API运行的地址和端口
API_HOST = '127.0.0.1'
API_PORT = '8888'

# api、测试器、cookies生成器开关
API_ENABLED = True
CREATOR_ENABLED = True
TESTER_ENABLED = True

# 云打码的参数设置
YUNDAMA_USERNAME = 'vash1996'
YUNDAMA_PASSWORD = 'zhouxin'
YUNDAMA_APP_ID = '6272'
YUNDAMA_APP_KEY = '66e73c9d840f7121200c4a856167ce91'
YUNDAMA_API_URL = 'http://api.yundama.com/api.php'
YUNDAMA_MAX_RETRY = 20

# redis 数据库的设置
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None

REDIS_DOMAIN = '*'
REDIS_NAME = '*'

# 浏览器类型
DEFAULT_TYPE = 'Chrome'

# 产生器类，如扩展其他站点，请在此配置
GREATOR_MAP = {
    'weibo': 'WeiboCookieCreator'
}

# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}

# 产生器和验证器循环周期
CYCLE = 1800

# 用于生成cookie的线程数
THREAD_COUNT = 2
