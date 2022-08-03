import time
import datetime


def getDay(offset):
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(days=offset)
    uuid_str = yes_time.strftime('%Y%m%d')  # 格式化输出
    return uuid_str

def getYesterday():
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(days=-1)
    uuid_str = yes_time.strftime('%Y%m%d')  # 格式化输出
    return uuid_str

def getTomorrow():
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(days=1)
    uuid_str = yes_time.strftime('%Y%m%d')  # 格式化输出
    return uuid_str


def getToday():
    # uuid_str = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    uuid_str = time.strftime("%Y%m%d", time.localtime())
    return uuid_str