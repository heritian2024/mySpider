#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from logging.handlers import SMTPHandler

from sender import Mail, Message

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


if __name__ == '__main__':
    tmpUrl = 'https://www.douban.com/group/topic/234722272/'
    tmpDiv = '天之骄子一室一厅一卫户型'
    content = '''
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        </head>
        <body>
            <a href="{url}">原文链接</a>
            {div}
        </body>
    </html>
    '''.format(url=tmpUrl, div=tmpDiv)

    send_mail(
        to=receivers,
        subject='标题',
        content=content,
        type='html',
        system=subject_prefix
    )
