import datetime
import logging
import time

range_time_start = '17:00'
range_time_end = '18:00'


logger = logging.getLogger(__name__)

def main():
    while True:
        # 当前时间
        n_time = datetime.datetime.now()
        logger.info('*****************************************')
        logger.info('爬虫轮次开始：{}'.format(n_time))
        print('爬虫轮次开始：{}'.format(n_time))
        logger.info('*****************************************')
        # 判断当前时间是否在范围时间内
        range_time_s = datetime.datetime.strptime(str(datetime.datetime.now().date()) + range_time_start,
                                                  '%Y-%m-%d%H:%M')
        range_time_e = datetime.datetime.strptime(str(datetime.datetime.now().date()) + range_time_end,
                                                  '%Y-%m-%d%H:%M')
        if n_time > range_time_s and n_time < range_time_e:
            print("123213")

        time.sleep(60 * 60)



if __name__ == "__main__":
    main()