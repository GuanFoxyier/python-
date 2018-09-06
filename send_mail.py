# -*- coding:utf-8 _*-
"""
@author:gjl
@file: send_email.py
@time: 2018/07/31
code description:
(1) description: 异常时发送报警邮件

"""

from email.mime.text import MIMEText
import smtplib


def sendmail(text=None, receive_list=None, send_list=None, title=None, from_addr=None, password=None):
    '''

    :param text: 发送内容主体
    :param receive_list: 接收人列表
    :param send_list: 发送人列表
    :param title: 邮件主体
    :return: True
    '''
    if not receive_list:
        return "请设置接收人列表"
    if not send_list:
        return "请设置发送人列表"
    if not text:
        return "请设置text参数"
    # 第一个为文本内容,第二个设置文本格式,第三个编码格式
    msg = MIMEText(text)
    # 显示于发件人
    # msg['From'] = 'guan.jinglin@bohui.com.cn'
    # 显示与收件人
    # 就是标题,最醒目的

    msg['Subject'] = title
    msg["Accept-Language"] = "zh-CN"
    msg["Accept-Charset"] = "ISO-8859-1,utf-8"
    #
    # 发送方
    if not from_addr:
        from_addr = ''  # 需手动添加发件人
    # 必须是自动授权码,需要发送人的授权码
    if not password:
        password = ''   # 需手动添加授权码默认值

    # smtp服务器
    smtp_server = 'smtp.263.net'

    server = smtplib.SMTP(smtp_server, 25)
    # 使用了ssl模式
    # server = smtplib.SMTP_SSL(smtp_server, 465)
    # 设置为调试模式
    # server.set_debuglevel(1)

    # 登陆ssl服务器
    server.login(from_addr, password)

    server.sendmail(from_addr, receive_list, msg.as_string())
    # 退出
    server.quit()
    return "发送邮件成功,收件人为{}".format(receive_list)


if __name__ == '__main__':
    print(sendmail(text="testing", receive_list=["guan.jinglin@bohui.com.cn"]))
