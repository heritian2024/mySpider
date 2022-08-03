import difflib
import sys

from dayUtils import getDay
from mailUtils import mailGoods

class Good:
    def __init__(self, name, link, label, price):
        self.name = name
        self.link = link
        self.label = label
        self.price = price


def find_samenumber(list1, list2):
    A = set(list1).intersection(set(list2))  # 交集
    B = set(list1).union(set(list2))  # 并集
    C = set(list1).difference(set(list2))  # 差集，在list1中但不在list2中的元素
    D = set(list2).difference(set(list1))  # 差集，在list2中但不在list1中的元素
    return A, B, C, D


def compareGoods(originfile, targetfile):
    dict_origin = {}
    list_origin = open(originfile, 'r', encoding='utf-8').readlines()
    print(originfile + "->" + str(len(list_origin)))
    for line in list_origin:
        gooditem = line.replace('\n', '').split('\t')
        name_target = gooditem[0]
        link_target = gooditem[1]
        label_target = gooditem[2]
        price_target = gooditem[3]
        dict_origin[link_target] = {
            'name': name_target,
            'link': link_target,
            'label': label_target,
            'price': price_target,
            'classify': ''
        }

    dict_new = {}  # 新增
    dict_rise = {}  # 涨价
    dict_drop = {}  # 降价

    list2 = open(targetfile, 'r', encoding='utf-8').readlines()
    print(targetfile + "->" + str(len(list2)))
    for line in list2:
        gooditem = line.replace('\n', '').split('\t')
        name_target = gooditem[0]
        link_target = gooditem[1]
        label_target = gooditem[2]
        price_target = gooditem[3]
        classify_target = gooditem[4]
        # print(name_target)
        # print(link_target)
        # print(label_target)
        # print(price_target)
        if link_target not in dict_origin:
            dict_new[link_target] = {
                'name': name_target,
                'link': link_target,
                'label': label_target,
                'price': price_target,
                'classify': classify_target
            }
        else:
            change_good = dict_origin[link_target]
            # print(change_good)
            if float(price_target) > float(change_good['price']):
                dict_rise[link_target] = {
                    'name': name_target,
                    'link': link_target,
                    'label': change_good['label'] + '->' + label_target,
                    'price': change_good['price'] + '->' + price_target,
                    'classify': classify_target
                }
            elif float(price_target) < float(change_good['price']):
                dict_drop[link_target] = {
                    'name': name_target,
                    'link': link_target,
                    'label': change_good['label'] + '->' + label_target,
                    'price': change_good['price'] + '->' + price_target,
                    'classify': classify_target
                }
    return dict_new, dict_rise, dict_drop


if __name__ == '__main__':
    # savepath_today = 'zhenfuliGoods_%s.txt' % getDay(-1)
    # savepath_yesterday = 'zhenfuliGoods_%s.txt' % getDay(-2)
    savepath_today = 'zhenfuliGoods_20220804.txt'
    savepath_yesterday = 'zhenfuliGoods_20220803.txt'

    dict_new, dict_rise, dict_drop = compareGoods(savepath_yesterday, savepath_today)

    print('每日上新：')
    print(dict_new)
    print('每日涨价：')
    print(dict_rise)
    print('每日降价：')
    print(dict_drop)

    ## step.发送email邮件通知
    print('step.发送email邮件通知')
    # if bool(dict_new):
    #     mailGoods(dict_new, '每日上新')
    # if bool(dict_rise):
    #     mailGoods(dict_rise, '每日涨价')
    if bool(dict_drop):
        mailGoods(dict_drop, '每日降价')