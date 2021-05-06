#!/usr/bin/env python3
#-*-coding:utf-8-*-

import itertools
from time import time
from tqdm import tqdm

start = time()
class Hero():
    '''英雄属性'''
    def __init__(self, cost, name, origin1, origin2, class1, class2):
        # 等级
        self.cost = cost
        # 名称
        self.name = name
        # 种族
        self.origin1 = origin1
        # 第二种族
        self.origin2 = origin2
        # 职业
        self.class1 = class1
        # 第二职业
        self.class2 = class2

弗拉基米尔 = Hero(1, '弗拉基米尔', '黑夜使者', '', '', '复苏者')
沃里克 = Hero(1, '沃里克', '破败军团', '', '', '斗士')
薇恩 = Hero(1, '薇恩', '破败军团', '', '', '游侠')
波比 = Hero(1, '波比', '小恶魔', '', '', '骑士')
乌迪尔 = Hero(1, '乌迪尔', '龙族', '', '', '神盾战士')
古拉加斯 = Hero(1, '古拉加斯', '黎明使者', '', '', '斗士')
蕾欧娜 = Hero(1, '蕾欧娜', '圣光卫士', '', '', '骑士')
吉格斯 = Hero(1, '吉格斯', '小恶魔', '', '', '法师')
卡兹克 = Hero(1, '卡兹克', '黎明使者', '', '', '刺客')
丽桑卓 = Hero(1, '丽桑卓', '魔女', '', '', '复苏者')
克烈 = Hero(1, '克烈', '小恶魔', '', '', '重骑兵')
亚托克斯 = Hero(1, '亚托克斯', '圣光卫士', '', '', '征服者')
卡莉斯塔 = Hero(1, '卡莉斯塔', '丧尸', '', '', '征服者')

乐芙兰 = Hero(2, '乐芙兰', '魔女', '', '', '刺客')
索拉卡 = Hero(2, '索拉卡', '黎明使者', '', '', '复苏者')
特朗德尔 = Hero(2, '特朗德尔', '屠龙勇士', '', '', '神盾战士')
布兰德 = Hero(2, '布兰德', '丧尸', '', '', '法师')
凯南 = Hero(2, '凯南', '小恶魔', '', '', '神盾战士')
韦鲁斯 = Hero(2, '维鲁斯', '圣光卫士', '', '', '游侠')
诺提勒斯 = Hero(2, '诺提勒斯', '铁甲卫士', '', '', '骑士')
维克托 = Hero(2, '维克托', '破败军团', '', '', '法师')
瑟庄妮 = Hero(2, '瑟庄妮', '黑夜使者', '', '', '重骑兵')
赫卡里姆 = Hero(2, '赫卡里姆', '破败军团', '', '', '重骑兵')
辛德拉 = Hero(2, '辛德拉', '圣光卫士', '', '', '神谕者')
锤石 = Hero(2, '锤石', '破败军团', '', '', '骑士')
瑟提 = Hero(2, '瑟提', '龙族', '', '', '斗士')

努努 = Hero(3, '努努', '丧尸', '', '', '斗士')
艾希 = Hero(3, '艾希', '神佑之森', '龙族', '', '游侠')
莫甘娜 = Hero(3, '莫甘娜', '魔女', '黑夜使者', '', '秘术师')
卡特琳娜 = Hero(3, '卡特琳娜', '破败军团', '', '', '刺客')
魔腾 = Hero(3, '魔腾', '复生亡魂', '', '', '刺客')
李青 = Hero(3, '李青', '黑夜使者', '', '', '神盾战士')
奈德丽 = Hero(3, '奈德丽', '黎明使者', '', '', '神盾战士')
潘森 = Hero(3, '潘森', '屠龙勇士', '', '', '神盾战士')
锐雯 = Hero(3, '锐雯', '黎明使者', '', '', '征服者')
拉克丝 = Hero(3, '拉克丝', '圣光卫士', '', '', '秘术师')
璐璐 = Hero(3, '璐璐', '小恶魔', '', '', '秘术师')
婕拉 = Hero(3, '婕拉', '龙族', '', '', '法师')
亚索 = Hero(3, '亚索', '黑夜使者', '', '', '征服者')

瑞兹 = Hero(4, '瑞兹', '破败军团', '丧尸', '', '秘术师')
贾克斯 = Hero(4, '贾克斯', '铁甲卫士', '', '', '神盾战士')
卡尔玛 = Hero(4, '卡尔玛', '黎明使者', '', '', '神谕者')
塔里克 = Hero(4, '塔里克', '神佑之森', '', '', '骑士')
莫德凯撒 = Hero(4, '莫德凯撒', '屠龙勇士', '', '', '征服者')
德莱文 = Hero(4, '德莱文', '破败军团', '', '', '征服者')
黛安娜 = Hero(4, '黛安娜', '黑夜使者', '屠龙勇士', '', '刺客')
维克兹 = Hero(4, '维克兹', '圣光卫士', '', '', '法师')
艾翁 = Hero(4, '艾翁', '复生亡魂', '', '神谕者', '复苏者')
厄斐琉斯 = Hero(4, '厄斐琉斯', '黑夜使者', '', '', '游侠')
芮尔 = Hero(4, '芮尔', '圣光卫士', '铁甲卫士', '', '重骑兵')

凯尔 = Hero(5, '凯尔', '圣光卫士', '神佑之森', '', '征服者')
黑默丁格 = Hero(5, '黑默丁格', '龙族', '', '驯龙大师', '复苏者')
盖伦 = Hero(5, '盖伦', '黎明使者', '', '神王', '骑士')
沃利贝尔 = Hero(5, '沃利贝尔', '复生亡魂', '', '', '斗士')
德莱厄斯 = Hero(5, '德莱厄斯', '黑夜使者', '', '神王', '骑士')
千珏 = Hero(5, '千珏', '永猎双子', '', '游侠', '秘术师')
佛耶戈 = Hero(5, '佛耶戈', '破败军团', '', '刺客', '神盾战士')
提莫 = Hero(5, '提莫', '小恶魔', '', '大魔王', '神谕者')

all_heroes = [
    弗拉基米尔,
    沃里克,
    薇恩,
    波比,
    乌迪尔,
    古拉加斯,
    蕾欧娜,
    吉格斯,
    卡兹克,
    丽桑卓,
    克烈,
    亚托克斯,
    卡莉斯塔,
    乐芙兰,
    索拉卡,
    特朗德尔,
    布兰德,
    凯南,
    韦鲁斯,
    诺提勒斯,
    维克托,
    瑟庄妮,
    赫卡里姆,
    辛德拉,
    锤石,
    瑟提,
    努努,
    艾希,
    莫甘娜,
    卡特琳娜,
    魔腾,
    李青,
    奈德丽,
    潘森,
    锐雯,
    拉克丝,
    璐璐,
    婕拉,
    亚索,
    瑞兹,
    贾克斯,
    卡尔玛,
    塔里克,
    莫德凯撒,
    德莱文,
    黛安娜,
    维克兹,
    艾翁,
    厄斐琉斯,
    芮尔,
    凯尔,
    黑默丁格,
    盖伦,
    沃利贝尔,
    德莱厄斯,
    千珏,
    佛耶戈,
    提莫
]

def main(people, couple):
    '''统计羁绊组合'''
    破败军团 = 0
    黑夜使者 = 0
    魔女 = 0
    小恶魔 = 0
    屠龙勇士 = 0
    丧尸 = 0
    圣光卫士 = 0
    黎明使者 = 0
    神佑之森 = 0
    龙族 = 0
    铁甲卫士 = 0
    复生亡魂 = 0

    刺客 = 0
    游侠 = 0
    斗士 = 0
    征服者 = 0
    复苏者 = 0
    神谕者 = 0
    骑士 = 0
    法师 = 0
    神盾战士 = 0
    秘术师 = 0
    重骑兵 = 0

    text = ''
    couples = 0
    names = []
    for i in couple:
        if people == 4:
            if i.cost >= 4 or i.cost == 5:
                return '', 0, ''
        if people == 5:
            if i.cost == 5:
                return '', 0, ''
        if people == 6:
            if i.cost == 5:
                return '', 0, ''
        names.append(i.name)
        if i.origin1 == '破败军团':
            破败军团 += 1
        if i.origin1 == '黑夜使者':
            黑夜使者 += 1
        if i.origin1 == '魔女':
            魔女 += 1
        if i.origin1 == '小恶魔':
            小恶魔 += 1
        if i.origin1 == '屠龙勇士':
            屠龙勇士 += 1
        if i.origin1 == '丧尸':
            丧尸 += 1
        if i.origin1 == '圣光卫士':
            圣光卫士 += 1
        if i.origin1 == '黎明使者':
            黎明使者 += 1
        if i.origin1 == '神佑之森':
            神佑之森 += 1
        if i.origin1 == '龙族':
            龙族 += 1
        if i.origin1 == '铁甲卫士':
            铁甲卫士 += 1
        if i.origin1 == '复生亡魂':
            复生亡魂 += 1

        if i.origin2 == '破败军团':
            破败军团 += 1
        if i.origin2 == '黑夜使者':
            黑夜使者 += 1
        if i.origin2 == '魔女':
            魔女 += 1
        if i.origin2 == '小恶魔':
            小恶魔 += 1
        if i.origin2 == '屠龙勇士':
            屠龙勇士 += 1
        if i.origin2 == '丧尸':
            丧尸 += 1
        if i.origin2 == '圣光卫士':
            圣光卫士 += 1
        if i.origin2 == '黎明使者':
            黎明使者 += 1
        if i.origin2 == '神佑之森':
            神佑之森 += 1
        if i.origin2 == '龙族':
            龙族 += 1
        if i.origin2 == '铁甲卫士':
            铁甲卫士 += 1
        if i.origin2 == '复生亡魂':
            复生亡魂 += 1


        if i.class1 == '刺客':
            刺客 += 1
        if i.class1 == '游侠':
            游侠 += 1
        if i.class1 == '斗士':
            斗士 += 1
        if i.class1 == '征服者':
            征服者 += 1
        if i.class1 == '复苏者':
            复苏者 += 1
        if i.class1 == '神谕者':
            神谕者 += 1
        if i.class1 == '骑士':
            骑士 += 1
        if i.class1 == '法师':
            法师 += 1
        if i.class1 == '神盾战士':
            神盾战士 += 1
        if i.class1 == '秘术师':
            秘术师 += 1
        if i.class1 == '重骑兵':
            重骑兵 += 1

        if i.class2 == '刺客':
            刺客 += 1
        if i.class2 == '游侠':
            游侠 += 1
        if i.class2 == '斗士':
            斗士 += 1
        if i.class2 == '征服者':
            征服者 += 1
        if i.class2 == '复苏者':
            复苏者 += 1
        if i.class2 == '神谕者':
            神谕者 += 1
        if i.class2 == '骑士':
            骑士 += 1
        if i.class2 == '法师':
            法师 += 1
        if i.class2 == '神盾战士':
            神盾战士 += 1
        if i.class2 == '秘术师':
            秘术师 += 1
        if i.class2 == '重骑兵':
            重骑兵 += 1

    num = 破败军团 // 3
    if num:
        couples += num
        text += f'破败军团{num}'
    num = 黑夜使者 // 2
    if num:
        couples += num
        text += f'黑夜使者{num}'
    num = 魔女 // 3
    if num:
        couples += num
        text += f'魔女{num}'
    num = 小恶魔 // 7
    if num:
        couples += 3
        text += f'小恶魔3'
    else:
        num = 小恶魔 // 5
        if num:
            couples += 2
            text += f'小恶魔2'
        else:
            num = 小恶魔 // 3
            if num:
                couples += 1
                text += f'小恶魔1'
    num = 屠龙勇士 // 2
    if num:
        couples += num
        text += f'屠龙勇士{num}'
    num = 丧尸 // 5
    if num:
        couples += 3
        text += f'丧尸3'
    else:
        num = 丧尸 // 4
        if num:
            couples += 2
            text += f'丧尸2'
        else:
            num = 丧尸 // 3
            if num:
                couples += 1
                text += f'丧尸1'
    num = 圣光卫士 // 3
    if num:
        couples += num
        text += f'圣光卫士{num}'
    num = 黎明使者 // 2
    if num:
        couples += num
        text += f'黎明使者{num}'
    num = 神佑之森 // 2
    if num:
        couples += num
        text += f'神佑之森{num}'
    num = 龙族 // 5
    if num:
        couples += 2
        text += f'龙族2'
    else:
        num = 龙族 // 3
        if num:
            couples += 1
            text += f'龙族1'
    num = 铁甲卫士 // 3
    if num:
        couples += 2
        text += f'铁甲卫士2'
    else:
        num = 铁甲卫士 // 2
        if num:
            couples += 1
            text += f'铁甲卫士1'
    num = 复生亡魂 // 3
    if num:
        couples += 2
        text += f'复生亡魂2'
    else:
        num = 复生亡魂 // 2
        if num:
            couples += 1
            text += f'复生亡魂1'

    num = 刺客 // 2
    if num:
        couples += num
        text += f'刺客{num}'
    num = 游侠 // 2
    if num:
        couples += num
        text += f'游侠{num}'
    num = 斗士 // 2
    if num:
        couples += num
        text += f'斗士{num}'
    num = 征服者 // 2
    if num:
        couples += num
        text += f'征服者{num}'
    num = 复苏者 // 2
    if num:
        couples += num
        text += f'复苏者{num}'
    num = 神谕者 // 2
    if num:
        couples += num
        text += f'神谕者{num}'
    num = 骑士 // 2
    if num:
        couples += num
        text += f'骑士{num}'
    num = 神盾战士 // 3
    if num:
        couples += num
        text += f'神盾战士{num}'
    num = 秘术师 // 4
    if num:
        couples += 3
        text += f'秘术师{num}'
    else:
        num = 秘术师 // 3
        if num:
            couples += 2
            text += f'秘术师2'
        else:
            num = 秘术师 // 2
            if num:
                couples += 1
                text += f'秘术师1'
    num = 重骑兵 // 4
    if num:
        couples += 3
        text += f'重骑兵3'
    else:
        num = 重骑兵 // 3
        if num:
            couples += 2
            text += f'重骑兵2'
        else:
            num = 重骑兵 // 2
            if num:
                couples += 1
                text += f'重骑兵1'

    return names, couples, text

# 人口等级
people = 8
all_couples = itertools.combinations(all_heroes, people)

def eight():
    '''计算组合数量'''
    def digui(n):
        if n == 1:
            return 1
        return n * digui(n - 1)
    Cnm = int(digui(len(all_heroes)) / (digui(len(all_heroes) - people) * digui(people)))
    return Cnm

def save_and_run():
    '''运行并写入文件'''
    n = 0
    with open(f'lol{people}.txt', 'a', encoding='utf-8') as f:
        with tqdm(total=eight(), ncols=85) as pbar:
            for x in all_couples:
                pbar.update(1)
                names, couple, text = main(people, x)
                if couple >= n:
                    n = couple
                    f.write(f'{str(names)}:{couple} {text}\n')
save_and_run()

print(f'用时{int((time()-start) // 60)}分{int((time()-start) % 60)}秒')