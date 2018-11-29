import redis

db = redis.StrictRedis()
KEY = "account:weibo:"

# 在python的file对象的readline以及readlines程序中，针对一些UTF-8编码的文件，开头会加入BOM来表明编码方式
# 使用'utf-8-sig'则不用担心开头出现'\xEF\xBB\xBF'了
with open('account.txt', encoding='utf-8-sig') as f:
    for line in f:
        k, v = line.split('----')
        db.set(KEY+k, v)
