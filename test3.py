import time

import config

groups = config.groups
i = 0
while True:
    i += 1
    print('开始轮次:{}'.format(i))
    print(groups)
    time.sleep(5)
