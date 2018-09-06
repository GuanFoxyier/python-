# -*- coding: utf-8 -*-
import pymongo
import re

author = "Guanjinglin"
email = "1372851437@qq.com"


conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
citytest2 = conn.spider_wx.cityarea2_fang   # 连接表
i = 0  # 用来统计删除坐标点次数及防止栈溢出
def decoordinates(citytest2):
    '''
    名称: decoordinates
    功能: 添加坐标索引,若发生坐标冲突,则删除靠后的坐标,直至成功(坐标点相同问题尚未添加)
    return: None
    '''
    try:
        global i
        citytest2.create_index([("polygons", "2dsphere")])
        print(i)
    except Exception as e:
        global i
        e = str(e)
        retest = re.compile(r'\[(.*?)\]')
        if "Duplicate vertices" in str(e):  # 坐标重合问题
            retest2 = re.compile(r'and (\d+)')
            test2 = int(retest2.findall(str(e))[0])   # 获取出错在第几条
            # print test2
        elif "locations in degrees" in str(e):  # 坐标冲突问题
            retest2 = re.compile(r'(\d+?)\s+?cross')
            test2 = retest2.findall(str(e))[0]  # 获取出错在第几条
        i += 1
        idtest = re.compile(r'_id:\s+(\d+)')
        idtest = idtest.findall(str(e))[0]   # 获取出错id
        test = ' [' + retest.findall(str(e))[int(test2)].strip() +  '],' # 获取该条出错的坐标
        errortest = citytest2.find_one({"_id": int(idtest)})
        e = eval(str(errortest).replace(test, ''))
        citytest2.update({"_id": int(idtest)}, e)
        if i < 1000:
            decoordinates(citytest2)
if __name__ == '__main__':
    decoordinates(citytest2)