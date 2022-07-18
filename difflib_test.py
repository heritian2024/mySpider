import difflib
import sys

from getZhenfuliGoods import getDay

savepath_today = 'zhenfuliGoods_%s.txt' % getDay(-1)
savepath_yesterday = 'zhenfuliGoods_%s.txt' % getDay(-2)

file1 = open(savepath_today, 'r', encoding='utf-8').readlines()
file2 = open(savepath_yesterday, 'r', encoding='utf-8').readlines()
diff = difflib.ndiff(file1, file2)


sys.stdout.writelines(diff)