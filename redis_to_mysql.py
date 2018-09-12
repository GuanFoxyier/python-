import pymysql
import redis
import json
# import time
from traceback import print_exc

author = "Guanjinglin"
email = "1372851437@qq.com"
# Created on 2018-09-12
# 本代码基于python3.6.1测试通过

class Redis_To_Mysql:
    def __init__(self):
        self.redis_conn = redis.StrictRedis(host='localhost', port=6379, db=0, password="password")
        self.redis_key = "redis_key"  # redis_key
        self.l = self.redis_conn.llen(self.redis_key)
        self.mysql_conn = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='db',
                       charset='utf8')
        self.mysql_cursor = self.mysql_conn.cursor()
    def run(self):
        for i in range(self.l):
            try:
                n = self.redis_conn.blpop(self.redis_key)
                n = json.loads(n[1].decode("utf-8"))
                x = ','.join(n.keys())
                y = ','.join(['%s'] * len(n.keys()))
                title = "title"   # mysql表名
                sql = 'insert into {}('.format(title) + x + ') VALUES (' + y + ')'
                # for a, b in n.items():
                #     if a == "date_pub" or a == "crawl_time":
                #         n[a] = time.mktime(time.strptime(b, "%Y-%m-%d"))
                z = tuple(n.values())
                print(z)
                self.mysql_cursor.execute(sql, z)
                self.mysql_conn.commit()
                print(i)
            except Exception as e:
                print(e)
                print_exc()
                break
        self.mysql_conn.close()

if __name__ == '__main__':
    rtm = Redis_To_Mysql()
    rtm.run()