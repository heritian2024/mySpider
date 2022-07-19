#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from logging.handlers import SMTPHandler

from sender import Mail, Message
from dayUtils import getToday
import config

logger = logging.getLogger(__name__)

sender = config.mail['sender']
host = config.mail['host']
password = config.mail['password']
receivers = config.mail['receivers']
subject_prefix = config.mail['subject_prefix']


def add_error_log_mail_handler(logger, system):
    mail_handler = SMTPHandler(
        mailhost=host,
        fromaddr=sender,
        toaddrs=receivers,
        subject='[{system}] 发生错误'.format(system=system),
        credentials=(sender, password),
        timeout=30
    )
    mail_handler.setLevel(logging.ERROR)
    logger.addHandler(mail_handler)


def send_mail(subject, to, content, cc=None, type='plain', system='自动'):
    if cc is None:
        cc = []

    html, body = None, None
    if type == 'html':
        html = content
    else:
        body = content

    subject = subject.replace('\n', ' ')
    subject = '[{}]{}'.format(system, subject)
    mail = Mail(host=host, port=25, username=sender, password=password)
    msg = Message(subject=subject, to=to, cc=cc, html=html, body=body,
                  fromaddr=sender)
    mail.send(msg)

def mailGoods(tmpList):
    tmpDiv = ''
    for l in tmpList:
        strs = l.replace('\n', '').split('\t')
        tmpDiv += ('<div>' + '<a href="' + strs[1] + '">' + strs[0] + " : " + strs[2] + "(" + strs[
            3] + ")" + '</a>' + '</div>\n')

    content = '''
     <html>
         <head>
             <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
         </head>
         <body>
             <div>
                 每日上新-{day}
             </div>
             {div}
         </body>
     </html>
     '''.format(day=getToday(), div=tmpDiv)
    print(content)
    send_mail(
        to=receivers,
        subject=getToday(),
        content=content,
        type='html',
        system='真福利每日上新'
    )

if __name__ == '__main__':
    tmpList = {'伊利 苦咖啡冰淇淋童年怀旧冷饮脆皮雪糕70克*6支*2盒\thttps://jifen.zhenfuli.com/mobile/#/goods/1219319\t¥49.90\t43.41\n',
               '茶茶一季冬瓜荷叶茶袋*20泡   2盒 2盒\thttps://jifen.zhenfuli.com/mobile/#/goods/1229790\t¥46.00\t40.02\n',
               '和路雪 可爱多甜筒萨摩椰椰子口味冰淇淋65g*6支\thttps://jifen.zhenfuli.com/mobile/#/goods/1219313\t¥43.90\t38.19\n',
               '老杨咸蛋黄方块酥饼干混合口味礼袋装休闲零食年货送礼礼盒100g*6盒\thttps://jifen.zhenfuli.com/mobile/#/goods/1198083\t¥88.00\t76.56\n'}

    mailGoods(tmpList)
