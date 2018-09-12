# base64+gzip+AES-ECB-demo

author = "Guanjinglin"
email = "1372851437@qq.com"
# Created on 2018-09-12
# 本代码基于python3.6.1测试通过

import base64
from Crypto.Cipher import AES
from io import StringIO
import gzip

'''
采用AES对称加密算法
'''


# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


# 加密方法
def encrypt_oracle():
    # 秘钥
    key = 'jiayanmiyao'
    # 待加密文本
    text = 'testing'
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(text))
    # 用base64转成字符串形式
    encrypted_text = base64.encodebytes(encrypt_aes)  # 执行加密并转码返回bytes  # str(encoding=utf-8)
    en_gzip = gzip.compress(encrypted_text)
    en_base64 = base64.b64encode(en_gzip)
    return en_base64


# 解密方法
def decrypt_oralce(text):
    # 秘钥
    key = 'jiayanmiyao'
    # 密文

    de_base64 = base64.b64decode(text)

    de_gzip = gzip.decompress(de_base64)

    text = str(de_gzip, encoding="utf-8")
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    # 执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
    return decrypted_text


if __name__ == '__main__':
    en_result = encrypt_oracle()
    print(en_result)
    de_result = decrypt_oralce(en_result)
    print(de_result)
