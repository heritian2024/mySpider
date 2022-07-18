


locations1 = ('广兰路', '天之骄子')
locations2 = ['广兰路', '天之骄子']
locations3 = ( '天之骄子')
locations4 = [ '天之骄子']


for l in locations1:
    print(l)
for l in locations2:
    print(l)
for l in locations3:
    print(l)
for l in locations4:
    print(l)



# 搜索关键字
locations = ['天之骄子']

# 不包括
exclude_words = ('求租', '香楠')

title = '2号线广兰路地铁口 天之骄子人才公寓最小户型整租3200 有钥匙 一年一签'

if not any([x in title for x in exclude_words]):
    print('[筛选后] url:{}  title:{} time:{}'+title)

if any([x in title for x in locations[0]]):
    print('[筛选后] qqqqqqqqqqq' + title)


if not any([x in title for x in exclude_words]) and any([x in title for x in locations[0]]):
    print('[筛选后] wwwwww'+title)