# -*- coding: utf-8 -*-


mail = {
    'sender': 'watch_ch@163.com',
    'host': 'smtp.163.com',
    'password': 'ch20103314',
    'subject_prefix': '豆瓣爬虫租房',
    'receivers': ['chenhe2018@qq.com'],
}

groups = [
    (634832, '天之骄子'),
    (496399, '【广兰路附近租房】'),
#    ('zjhouse', '浦东张江租房'),
    (609867, '个人张江租房'),
]

locations = ('广兰路', '天之骄子')

#不包括
exclude_words = ('求租','香楠','玉兰香苑','金科路','张江高科','求','短租','已出','出')
