#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import difflib
import logging
import json
import os
import sys
import random
import time
import datetime
import traceback

from lxml import etree
import requests

import config
from init_logger import init_logger
from mail import send_mail, add_error_log_mail_handler


logger = logging.getLogger(__name__)

system = config.mail['subject_prefix']
groups = config.groups
locations = config.locations
receive_mail_addresses = config.mail['receivers']
exclude_words = config.exclude_words
pre_time = config.pre_time

rooms_filepath = './douban_rooms.json'

class DoubanSpider(object):
    random_headers = [
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)'},
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'},
        {'User-Agent': 'Opera/9.25 (Windows NT 5.1; U; en)'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'},
        {'User-Agent': 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)'},
        {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12'},
        {'User-Agent': 'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'},
        {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7'},
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 '},
    ]
    # default_headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
    #                   'AppleWebKit/537.36 (KHTML, like Gecko) '
    #                   'Chrome/61.0.3163.100 Safari/537.36',
    # }

    search_url = 'http://www.douban.com/group/search'
    search_required_params = dict(cat=1013, sort='time')

    def get_room_url_title_list(self, group_id, query):
        params = dict(group=group_id, q=query, **self.search_required_params)
        response = requests.get(
            url=self.search_url, params=params,
            headers=random.choice(self.random_headers)
        )
        if response.status_code == 200:
            root = etree.HTML(response.text)
            xpath = '//table[@class="olt"]//a[@title]'
            linkNodes = root.xpath(xpath)
            xpathTime = '//table[@class="olt"]//td[@class="td-time"]'
            linkNodesTime = root.xpath(xpathTime)
            for i in range(len(linkNodes)):
                yield linkNodes[i].get('href'), linkNodes[i].get('title'), linkNodesTime[i].get('title')
        else:
            logger.error(
                '查询房子接口失败 url: {} rsp: {}'.format(self.search_url, response)
            )

    def get_room_desc_div(self, url):
        response = requests.get(url=url, headers=random.choice(self.random_headers))
        if response.status_code == 200:
            root = etree.HTML(response.content)
            xpath = '//div[@class="topic-content clearfix"]'
            try:
                div_element = root.xpath(xpath)[0]
                return etree.tostring(div_element).decode()
            except:
                logger.error('获取房子详细信息失败, url: {} rsp: {} {}'.format(url, response, traceback.format_exc()))
        else:
            logger.error('获取房子详细信息失败, url: {} rsp: {}'.format(url, response))

class Diff(object):

    def __init__(self, new_dicts):
        self.filepath = rooms_filepath
        self.old_dicts = self._load_old_items_from_disk()
        self.new_dicts = new_dicts
        self._save_items_to_disk({**self.old_dicts, **self.new_dicts})

    def get_added_items(self):
        # 第一次创建旧文件不提醒
        if not self.old_dicts:
            return
        old_titles = list(set(self.old_dicts.values()))
        added_titles = []
        for url, title in self.new_dicts.items():
            # 根据字符串相似度来选出新帖子
            if not difflib.get_close_matches(title, old_titles + added_titles, cutoff=0.6):
                added_titles.append(title)
                yield url, title

    def _load_old_items_from_disk(self):
        if not os.path.isfile(self.filepath):
            return {}
        return json.load(open(self.filepath))

    def _save_items_to_disk(self, new_dicts):
        f = open(self.filepath, 'w', encoding="utf-8")
        f.write(json.dumps(new_dicts, indent=4, ensure_ascii=False))
        f.flush()
        f.close()


def get_all_group_rooms():
    for group_id, group_name in groups:
        for location in locations:
            logger.info('获取豆瓣小组:{} 地点:{}'.format(group_name, location))
            room_list = DoubanSpider().get_room_url_title_list(group_id, location)
            for url, title, tmpTime in room_list:
                time_stamp_pre = time.mktime(time.strptime(pre_time, '%Y-%m-%d %H:%M:%S'))
                time_stamp_target = time.mktime(time.strptime(tmpTime, '%Y-%m-%d %H:%M:%S'))
                logger.info('######{}:{}'.format(title, tmpTime))
                if int(time_stamp_target) > int(time_stamp_pre):
                    if not any([x in title for x in exclude_words]):
                        logger.info('[筛选后] url:{}  title:{} time:{}'.format(url, title, tmpTime))
                        yield url, title
            time.sleep(random.randint(5, 10))


def get_new_rooms():
    rooms_dict = dict(get_all_group_rooms())
    added_rooms = Diff(rooms_dict).get_added_items()
    return added_rooms


def send_room_mail(room_url, room_title):
    room_desc_div = DoubanSpider().get_room_desc_div(room_url)
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
'''.format(url=room_url, div=room_desc_div)
    
    send_mail(
        to=receive_mail_addresses,
        subject=room_title,
        content=content,
        type='html',
        system=system
    )


def monitor_rooms():
    while True:
        # 当前时间
        n_time = datetime.datetime.now()
        logger.info('*****************************************')
        logger.info('爬虫轮次开始：{}'.format(n_time))
        logger.info('*****************************************')
        # 判断当前时间是否在范围时间内
        range_time_s = datetime.datetime.strptime(str(datetime.datetime.now().date()) + config.range_time_start,
                                                  '%Y-%m-%d%H:%M')
        range_time_e = datetime.datetime.strptime(str(datetime.datetime.now().date()) + config.range_time_end,
                                                  '%Y-%m-%d%H:%M')
        if n_time > range_time_s and n_time < range_time_e:
            new_rooms = get_new_rooms()
            for url, title in new_rooms:
                logger.info('[发送邮件] 链接：{}，标题：{}'.format(url, title))
                send_room_mail(url, title)
                time.sleep(random.randint(2, 10))
            # 休眠60*(45~75)秒
            time.sleep(60 * random.randint(45, 75))
        else:
            #休眠60*60秒
            time.sleep(60 * 60)



if __name__ == '__main__':

    add_error_log_mail_handler(logger, system)

    try:
        monitor_rooms()
    except:
        logger.error('程序异常终止', traceback.format_exc())
