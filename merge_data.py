# coding:utf-8

author = "Guanjinglin"
email = "1372851437@qq.com"
# Created on 2018-09-12
# 本代码基于python3.6.1测试通过
# 通过递归合并两条内部多种数据结构的字典

a = {
    "name": '111',
    "url": "123123123",
    "tag": {
        "name": "2222",
        "url": "bbb",
        "ccc": "xxx",
        "tag1": {
            "name": "22222",
            "url": "xxx"
        },
        "tag2": {
            "name": "666666",
            "url": "yyy",
            "666": "66666"
        },
    },
    "test1": [
        "1", "2", "3", "666", {
            "aa": "11",
            "bb": "22"
        },
    ]
}
b = {
    "name": "222",
    "url": "23213123",
    "tag": {
        "name": "1111",
        "url": "bbb",
        "tag1": {
            "name": "11111",
            "url": "xxx"
        },
        "tag2": {
            "name": "dwdqw",
            "url": "yyy"
        }
    },
    "test1": [
        "2", "3", "4", "5", {
            "bb": "22",
            "cc": "333"
        }
    ]
}


def a_b(a, b):  # 两条数据, 以第一条数据为优先,进行数据合并
    if isinstance(a, dict) and isinstance(b, dict):
        for i, j in a.items():
            if i not in b:
                b[i] = j
            else:
                if isinstance(j, list) or isinstance(j, dict):
                    a_b(a[i], b[i])
    if isinstance(a, list) and isinstance(b, list):
        for i in range(len(a)):
            if not a[i] in b and not isinstance(a[i], dict) and not isinstance(a[i], list):
                b.append(a[i])
            else:
                if isinstance(a[i], list) or isinstance(a[i], dict):
                    a_b(a[i], b[i])

    return b


if __name__ == '__main__':
    x = a_b(a, b)
    print(x)
