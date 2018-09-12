from redis import StrictRedis
import json
import pymysql

author = "Guanjinglin"
email = "1372851437@qq.com"
# Created on 2018-09-12
# 本代码基于python3.6.1测试通过

class Create_mysql_for_redis:
    def __init__(self):

        self.conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="password", charset="utf8", db="test")
        self.cursor = self.conn.cursor()
        self.redis_conn = StrictRedis(host="localhost", port=6379, db=0, password="password")
        self.redis_title = "title"  # 要取出的redis数据
    def run(self):


        data = self.redis_conn.lpop(self.redis_title).decode("utf-8")

        print(data)
        title = "title"  # 要创建的表名
        sql = "create table if not exists {}(id int(10) unsigned NOT NULL AUTO_INCREMENT,".format(title)
        print(json.loads(data))
        print(json.loads(data).keys())
        for i, j in json.loads(data).items():
            try:
                j = int(float(j))
                k = " int(2)"
            except:
                j = str(j)
                k = " varchar(255)"
            finally:
                sql += i
                sql += k
                sql += ","
        sql = sql.rstrip(",")
        sql += ",PRIMARY KEY (id))  ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()
        self.redis_conn.lpush(self.redis_title)  # 将该条redis数据回写进redis