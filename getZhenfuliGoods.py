import re  # 正则
import urllib.error
import urllib.request
import json
import requests
import random
import time
import datetime


def main():
    savepath_today = 'zhenfuliGoods_%s.txt' % getToday()
    savepath_yesterday = 'zhenfuliGoods_%s.txt' % getYesterday()
    print("today    >>" + savepath_today)
    print("yesterday >>" + savepath_yesterday)

    ## step.获取所有商品
    # cat_id: 55180
    default_max_page = 5000
    default_start_page = 22
    for page in range(default_max_page):
        tmp_page = default_start_page + page
        print("执行轮次：" + str(tmp_page))
        count = saveGoods(tmp_page, savepath_today)
        if count <= 0:
            break
        time.sleep(5 + random.randint(5, 10))

    ## step.比对商品列表

    ## step.获取上新物品


def getYesterday():
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(days=-1)
    uuid_str = yes_time.strftime('%Y%m%d')  # 格式化输出
    return uuid_str


def getToday():
    # uuid_str = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    uuid_str = time.strftime("%Y%m%d", time.localtime())
    return uuid_str


def saveGoods(page, savepath):
    post_url = "https://jifen.zhenfuli.com/api/v4/catalog/goodslist"
    request_param = {
        # "cat_id":"55180",
        "warehouse_id": "0",
        "area_id": "0",
        "min": "",
        "max": "",
        "filter_attr": "",
        "ext": "",
        "goods_num": "0",
        "size": "100",
        "page": page,
        "sort": "goods_id",
        "order": "desc",
        "self": "0",
        "intro": "",
        "ru_id": "86517"}
    response_data = request_post(post_url, request_param)
    for good in response_data["data"]:
        print(good["goods_name"] + "\t" + good["url"] + "\t" + good["market_price"] + "\t" + good["shop_price"])
        f = open(savepath, 'a', encoding='utf-8')
        f.write(
            good["goods_name"] + "\t" + good["url"] + "\t" + good["market_price"] + "\t" + good["shop_price"] + "\n")
        f.flush()
        f.close()
    return len(response_data["data"])


def request_post(url, param):
    fails = 0
    while True:
        try:
            if fails >= 10:
                break

            headers = {'content-type': 'application/json',
                       'cookie': 'PHPSESSID=kd507cl67smve838cli4k0qgel; session_id_ip=eyJpdiI6InlRNmdwM1VZMlpETWRZTm80TWZDcmc9PSIsInZhbHVlIjoiWExRejBrSFF0UWdUWUppYm15NVRYTzg1V1JwM1hFN3VQMDE2UXhwN1RCQ3MxaWdyR2xWSCttTytENWkrM3hxcnFBNnNLdkpMUGZmbE9GWXNVZWIyb1E9PSIsIm1hYyI6ImMwOTExM2NiODgzMDRjOTgyZmMwZjRlMDI2ZTVlNDcwZDE3MmZmZTYyMzU0Njc2NGY0ZmJmZTVmN2I3N2NiMGQifQ%3D%3D; XSRF-TOKEN=eyJpdiI6ImFDN0ZEbW1oMng4aG9uK0xzZ2lsNGc9PSIsInZhbHVlIjoiYWQ5NE8yMmxOb3ZEaURnVEwwM2pGZjNLdzQyY0VcL0IwSWkzTUQrbTUwMVRWcjgzUm5rclMzTHFEVWhWOVF1eHIiLCJtYWMiOiIxMmUxMzUyNmZjMzNkZmVkZWY5NzJiNTk4MTFlOTk4NGYxNjZiNTMzYWE2MjE0NjUyY2NhZTk2ZDgwNjNkMzM1In0%3D; dscmall_session=eyJpdiI6Imh4TGV1dmk4RnVraFVxaStQRXNTSHc9PSIsInZhbHVlIjoicXpQSzJcL3VMTXVNYlNCZFwvbWFiTDRrSklOdVFiOXRPRG9POHBmaFVBdXBLWVFCYndmT0tVc1JNUGdQNjlpYzVmIiwibWFjIjoiYjQwMDNiZWNlNjE5MDU3OGRhZGVlMjgwYzMzYmY3ZDZlMDFkNWVhNTA4NWNmMGYyZDQ3OTg0NzA0M2E1ODk3MCJ9',
                       'origin': 'https://jifen.zhenfuli.com',
                       'referer': 'https://jifen.zhenfuli.com/mobile',
                       'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJhdWQiOiJodHRwczpcL1wvd3d3LmRzY21hbGwuY24iLCJzdWIiOiJqcm9ja2V0QGV4YW1wbGUuY29tIiwiZXhwIjoxNjU5MTkzNDM1LCJ1c2VyX2lkIjo4ODc4Nn0.tLMDTKO5r6iJopv7-SL0b_Hf1oLvGO4emWGr72Pwq-4',
                       'userregion': 'bnVsbA==',
                       'origin': 'https://jifen.zhenfuli.com',
                       }
            ret = requests.post(url, json=param, headers=headers, timeout=10)

            if ret.status_code == 200:
                text = json.loads(ret.text)
            else:
                continue
        except:
            fails += 1
            print('网络连接出现问题, 正在尝试再次请求: ', fails)
            time.sleep(5)
        else:
            break
    return text


# 得到指定网站url内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


if __name__ == "__main__":
    main()
