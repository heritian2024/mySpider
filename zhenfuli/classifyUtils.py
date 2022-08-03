import re


def classification(contents):
    # contents = []
    # # originfile = 'zhenfuliGoods_20220720.txt'
    # list_origin = open(originfile, 'r', encoding='utf-8').readlines()
    # print(originfile + "->" + str(len(list_origin)))
    # for line in list_origin:
    #     gooditem = line.replace('\n', '').split('\t')
    #     name_target = gooditem[0]
    #     # cleaned_name = re.sub(r'\d+[g|kg|KG|盒|泡|节|卷|ml|L|只|mm|cm|m|袋|罐|瓶|块装|支|箱|件装|桶|包|克]', '', name_target) \
    #     #     .replace("*", "") \
    #     #     .replace(" ", "")
    #     # contents.append(cleaned_name)
    #     contents.append(name_target)
    # # print(contents)

    # classifyArray = ['锅', '电', '火锅', '餐具', '碗盘', '甜品杯', '削皮刀','瓷器','瓷杯'
    #     # , '苹果', '橙子', '火龙果', '鲜果', '', '', '芒果', '蔓越莓','山楂','秋梨膏','桃胶'
    #     # , '零食', '休闲食品', '海苔','糕'
    #     # , '咖啡', '茶', '饮料', '炖品'
    #     # , '雪糕', '蛋糕'
    #     # , '酸奶', '牛奶', '冰淇淋', '巧克力奶'
    #     # , '披萨', '蛋白', '奶酪','蛋黄酥','芝士'
    #     # , '银耳', '百合', '枣', '烘焙', '枸杞', '坚果', '莲子', '松子', '开心果', '甘草','陈皮', '八宝粥', '巴旦木', '榛子', '枸杞', '粮粗', '坚果', '木耳', '花生仁','甘栗仁','核桃','桂圆'
    #     , '香水', '整理', '收纳', '礼品', '牙', '衣架', '药盒', '眼罩', '镜','毛巾'
    #     # , '馄饨', '水饺', '烧麦', '包子', '面包', '饼', '方便面', '早点', '早餐', '膳食', '吐司', '手抓饼', '代餐粉', '代餐棒','蟹味棒','酥蛋皮','麻花'
    #     # , '纸巾', '湿巾', '卫生巾', '姨妈巾', '面巾纸', '抹布', '软抽', '卷纸', '手帕纸', '抽纸', '浴巾', '纸手帕', '洗脸巾', '护垫','纸品','斑布','护舒宝'
    #     # , '沐浴液','清洗液','烫染修护', '洗发','发膜', '洗手液', '柔顺剂', '洗衣', '洁', '护手霜', '止汗露','除毛', '护发素', '精华', '沐浴露', '衣领净', '染发', '润发', '皂', '身体乳', '口腔喷雾','喷剂','乳液','润体乳','发胶','发蜡','乳液','育发膏','足膜'
    #     # , '虾', '海鲜', '菜肴', '牛', '羊'
    #     # , '鸭', '鸡', '肉', '粮粗', '香肠', '火腿', '腊味', '腊肠','烤肠'
    #     # , '面', '菜', '米', '油', '肉', '豆', '水', '五谷', '鱼', '粉', '菌', '食品'
    #     # , '调味', '醋', '盐', '酱油', '耗油', '底料', '蜜', '糖', '咖喱', '酱', '酒', '汁', '煲汤', '味精', '香叶'
    #     , '垃圾袋', '塑料袋', '竹炭包', '驱虫','甲醛'
    #     , '西洋参', '花旗参'
    #                  ]
    # classifyArray = [i for i in classifyArray if (len(str(i)) != 0)]
    # print(classifyArray)

    classifyMap = {}
    classifyMap['洗护'] = ['沐浴液', '清洗液', '烫染修护', '洗发', '发膜', '洗手液', '柔顺剂', '洗衣', '洁', '护手霜', '止汗露', '除毛', '护发素', '精华',
                         '沐浴露',
                         '衣领净', '染发', '润发', '皂', '身体乳', '口腔喷雾', '喷剂', '乳液', '润体乳', '发胶', '发蜡', '乳液', '育发膏', '足膜'
                         ]
    classifyMap['纸巾'] = ['纸巾', '湿巾', '卫生巾', '姨妈巾', '面巾纸', '抹布', '软抽', '卷纸', '手帕纸', '抽纸', '浴巾', '纸手帕', '洗脸巾', '护垫', '纸品',
                         '斑布', '护舒宝'
                         ]
    classifyMap['水果'] = ['苹果', '橙子', '火龙果', '鲜果', '芒果', '蔓越莓', '山楂', '秋梨膏', '桃胶'
                         ]
    classifyMap['零食'] = ['零食', '休闲食品', '海苔', '糕', '咖啡', '茶', '饮料', '炖品', '雪糕', '蛋糕', '酸奶', '牛奶', '冰淇淋', '巧克力奶', '披萨',
                         '蛋白', '奶酪', '蛋黄酥', '芝士',
                         '银耳', '百合', '枣', '烘焙', '枸杞', '坚果', '莲子', '松子', '开心果', '甘草', '陈皮', '八宝粥', '巴旦木', '榛子', '枸杞',
                         '粮粗', '坚果', '木耳', '花生仁', '甘栗仁', '核桃', '桂圆'
                         ]
    classifyMap['主食'] = ['馄饨', '水饺', '烧麦', '包子', '面包', '饼', '方便面', '早点', '早餐', '膳食', '吐司', '手抓饼', '代餐粉', '代餐棒', '蟹味棒',
                         '酥蛋皮', '麻花',
                         '虾', '海鲜', '菜肴', '牛', '羊',
                         '鸭', '鸡', '肉', '粮粗', '香肠', '火腿', '腊味', '腊肠', '烤肠',
                         '面', '菜', '米', '油', '肉', '豆', '水', '五谷', '鱼', '粉', '菌', '食品'
                         ]
    classifyMap['厨房'] = ['调味', '醋', '盐', '酱油', '耗油', '底料', '蜜', '糖', '咖喱', '酱', '酒', '汁', '煲汤', '味精', '香叶'
                         ]
    classifyMap['置物'] = ['锅', '电', '火锅', '餐具', '碗盘', '甜品杯', '削皮刀', '瓷器', '瓷杯',
                         '香水', '整理', '收纳', '礼品', '牙', '衣架', '药盒', '眼罩', '镜', '毛巾',
                         '垃圾袋', '塑料袋', '竹炭包', '驱虫', '甲醛',
                         '西洋参', '花旗参'
                         ]
    cachedContent = {}

    for key in classifyMap:
        cachedContent[key] = []

    for content in contents:
        isExit = False
        for key in classifyMap:
            for subject in classifyMap[key]:
                if subject in content:
                    isExit = True
                    break
            if isExit:
                cachedContent[key].append(content)
                break
        if not isExit:
            cachedContent['未分类'].append(content)
    return cachedContent



if __name__ == "__main__":
    originfile = 'zhenfuliGoods_20220717.txt'
    # originfile = 'zhenfuliGoods_20220720.txt'
    contents = []
    # step.1
    list_origin = open(originfile, 'r', encoding='utf-8').readlines()
    print(originfile + "->" + str(len(list_origin)))
    for line in list_origin:
        gooditem = line.replace('\n', '').split('\t')
        name_target = gooditem[0]
        # cleaned_name = re.sub(r'\d+[g|kg|KG|盒|泡|节|卷|ml|L|只|mm|cm|m|袋|罐|瓶|块装|支|箱|件装|桶|包|克]', '', name_target) \
        #     .replace("*", "") \
        #     .replace(" ", "")
        # contents.append(cleaned_name)
        contents.append(name_target)
    print(contents)
    # step.2
    cachedContent = classification(contents)
    for key in cachedContent:
        print('%s:%s' % (key, cachedContent[key]))