import difflib
import sys

from getZhenfuliGoods import getDay


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


# savepath_today = 'zhenfuliGoods_%s.txt' % getDay(-1)
# savepath_yesterday = 'zhenfuliGoods_%s.txt' % getDay(-2)
savepath_today = 'zhenfuliGoods_20220718.txt'
savepath_yesterday = 'zhenfuliGoods_20220717.txt'


list1 = open(savepath_today, 'r', encoding='utf-8').readlines()
print(savepath_today + "->" + str(len(list1)))
for line in list1:
    strs = line.split("\t")


list2 = open(savepath_yesterday, 'r', encoding='utf-8').readlines()
print(savepath_yesterday + "->" + str(len(list2)))

# diff = difflib.ndiff(file1, file2)
# sys.stdout.writelines(diff)

union = set(list1).intersection(set(list2))
newadd = set(list1).difference(set(list2))
# print(union)
# print(len(union))
print(newadd)
