from redis import StrictRedis
import json
import pymysql

author = "Guanjinglin"
email = "1372851437@qq.com"
# Created on 2018-09-12
# 本代码基于python3.6.1测试通过

conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="password", charset="utf8", db="test")
cursor = conn.cursor()

a = StrictRedis(host="localhost", port=6379, db=0, password="password")
redis_title = "data"  # 要取出的redis数据
data = a.lpop(redis_title).decode("utf-8")

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
cursor.execute(sql)
conn.commit()
