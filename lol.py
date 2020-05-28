#!/usr/bin/env python3
#-*-coding:utf-8-*-

import itertools
from time import time
from tqdm import tqdm

start = time()
class Hero():
    '''英雄属性'''
    def __init__(self, grade, name, phyle, profession):
        # 等级
        self.grade = grade
        # 名称
        self.name = name
        # 种族
        self.phyle = phyle
        # 职业
        self.profession = profession

崔斯特 = Hero(1, '崔斯特', '未来战士', '法师')
凯特琳 = Hero(1, '凯特琳', '未来战士', '狙神')
墨菲特 = Hero(1, '墨菲特', '奥德赛', '斗士')
嘉文四世 = Hero(1, '嘉文四世', '暗星', '圣盾使')
波比 = Hero(1, '波比', '星之守护者', '重装战士')
蕾欧娜 = Hero(1, '蕾欧娜', '源计划', '重装战士')
格雷福斯 = Hero(1, '格雷福斯', '太空海盗', '强袭枪手')
菲奥娜 = Hero(1, '菲奥娜', '源计划', '剑士')
吉格斯 = Hero(1, '吉格斯', '奥德赛', '爆破专家')
卡兹克 = Hero(1, '卡兹克', '虚空', '刺客')
佐伊 = Hero(1, '佐伊', '星之守护者', '法师')
霞 = Hero(1, '霞', '星神', '剑士')
安妮 = Hero(2, '安妮', '银河魔装机神', '法师')
赵信 = Hero(2, '赵信', '星神', '圣盾使')
娑娜 = Hero(2, '娑娜', '奥德赛', '爆破专家秘术师')
布里茨 = Hero(2, '布里茨', '未来战士', '斗士')
莫德凯撒 = Hero(2, '莫德凯撒', '暗星', '重装战士')
慎 = Hero(2, '慎', '未来战士', '剑士')
阿狸 = Hero(2, '阿狸', '星之守护者', '法师')
德莱厄斯 = Hero(2, '德莱厄斯', '太空海盗', '破法战士')
卡莎 = Hero(2, '卡莎', '女武神', '刺客')
亚索 = Hero(2, '亚索', '奥德赛', '剑士')
卢锡安 = Hero(2, '卢锡安', '源计划', '强袭枪手')
洛 = Hero(2, '洛', '星神', '圣盾使')
易 = Hero(3, '易', '奥德赛', '剑士')
艾希 = Hero(3, '艾希', '星神', '狙神')
萨科 = Hero(3, '萨科', '暗星', '刺客')
卡萨丁 = Hero(3, '卡萨丁', '星神', '破法战士')
卡尔玛 = Hero(3, '卡尔玛', '暗星', '秘术师')
兰博 = Hero(3, '兰博', '银河魔装机神', '爆破专家')
伊泽瑞尔 = Hero(3, '伊泽瑞尔', '未来战士', '强袭枪手')
拉克丝 = Hero(3, '拉克丝', '暗星', '法师')
杰斯 = Hero(3, '杰斯', '太空海盗', '重装战士')
辛德拉 = Hero(3, '辛德拉', '星之守护者', '法师')
蔚 = Hero(3, '蔚', '源计划', '斗士')
妮蔻 = Hero(3, '妮蔻', '星之守护者', '圣盾使')
凯尔 = Hero(4, '凯尔', '女武神', '剑士')
索拉卡 = Hero(4, '索拉卡', '星之守护者', '秘术师')
科加斯 = Hero(4, '科加斯', '虚空', '斗士')
艾瑞莉娅 = Hero(4, '艾瑞莉娅', '源计划', '剑士')
孙悟空 = Hero(4, '孙悟空', '未来战士', '重装战士')
菲兹 = Hero(4, '菲兹', '银河魔装机神', '刺客')
维克兹 = Hero(4, '维克兹', '虚空', '法师')
烬 = Hero(4, '烬', '暗星', '狙神')
金克斯 = Hero(4, '金克斯', '奥德赛', '强袭枪手')
厄运小姐 = Hero(5, '厄运小姐', '女武神', '强袭枪手')
普朗克 = Hero(5, '普朗克', '太空海盗', '爆破专家')
泽拉斯 = Hero(5, '泽拉斯', '暗星', '法师')
璐璐 = Hero(5, '璐璐', '星神', '秘术师')
龙王 = Hero(5, '龙王', '奥德赛', '')
艾克 = Hero(5, '艾克', '源计划', '刺客')
锤石 = Hero(5, '锤石', '未来战士', '破法战士')

all_heroes = [
    崔斯特,
    凯特琳,
    墨菲特,
    嘉文四世,
    波比,
    蕾欧娜,
    格雷福斯,
    菲奥娜,
    吉格斯,
    卡兹克,
    佐伊,
    霞,
    安妮,
    赵信,
    娑娜,
    布里茨,
    莫德凯撒,
    慎,
    阿狸,
    德莱厄斯,
    卡莎,
    亚索,
    卢锡安,
    洛,
    易,
    艾希,
    萨科,
    卡萨丁,
    卡尔玛,
    兰博,
    伊泽瑞尔,
    拉克丝,
    杰斯,
    辛德拉,
    蔚,
    妮蔻,
    凯尔,
    索拉卡,
    科加斯,
    艾瑞莉娅,
    孙悟空,
    菲兹,
    维克兹,
    烬,
    金克斯,
    厄运小姐,
    普朗克,
    泽拉斯,
    璐璐,
    龙王,
    艾克,
    锤石
]

def main(people, couple):
    '''统计羁绊组合'''
    星之守护者 = 0
    银河魔装机神 = 0
    星神 = 0
    奥德赛 = 0
    未来战士 = 0
    虚空 = 0
    太空海盗 = 0
    源计划 = 0
    暗星 = 0
    女武神 = 0

    剑士 = 0
    爆破专家 = 0
    刺客 = 0
    斗士 = 0
    法师 = 0
    圣盾使 = 0
    狙神 = 0
    秘术师 = 0
    破法战士 = 0
    强袭枪手 = 0
    重装战士 = 0
    couples = 0
    names = []
    for i in couple:
        if people == 4:
            if i.grade >= 4 or i.grade == 5:
                return '', 0
        if people == 5:
            if i.grade == 5:
                return '', 0
        if people == 6:
            if i.grade == 5:
                return '', 0
        names.append(i.name)
        if i.phyle == '星之守护者':
            星之守护者 += 1
        if i.phyle == '银河魔装机神':
            银河魔装机神 += 1
        if i.phyle == '星神':
            星神 += 1
        if i.phyle == '奥德赛':
            奥德赛 += 1
        if i.phyle == '未来战士':
            未来战士 += 1
        if i.phyle == '虚空':
            虚空 += 1
        if i.phyle == '太空海盗':
            太空海盗 += 1
        if i.phyle == '源计划':
            源计划 += 1
        if i.phyle == '暗星':
            暗星 += 1
        if i.phyle == '女武神':
            女武神 += 1

        if i.profession == '剑士':
            剑士 += 1
        if i.profession == '爆破专家':
            爆破专家 += 1
        if i.profession == '刺客':
            刺客 += 1
        if i.profession == '斗士':
            斗士 += 1
        if i.profession == '法师':
            法师 += 1
        if i.profession == '圣盾使':
            圣盾使 += 1
        if i.profession == '狙神':
            狙神 += 1
        if i.profession == '秘术师':
            秘术师 += 1
        if i.profession == '破法战士':
            破法战士 += 1
        if i.profession == '强袭枪手':
            强袭枪手 += 1
        if i.profession == '重装战士':
            重装战士 += 1

    #print(names)
    num = 星之守护者 // 3
    if num:
        couples += num
    num = 银河魔装机神 // 3
    if num:
        couples += num
    num = 星神 // 2
    if num:
        couples += num
    num = 奥德赛 // 3
    if num:
        couples += num
    num = 未来战士 // 2
    if num:
        couples += num
    num = 虚空 // 3
    if num:
        couples += num
    num = 太空海盗 // 2
    if num:
        couples += num
    num = 源计划 // 3
    if num:
        couples += num
    num = 暗星 // 3
    if num:
        couples += num
    num = 女武神 // 2
    if num:
        couples += num

    num = 剑士 // 3
    if num:
        couples += num
    num = 爆破专家 // 2
    if num:
        couples += num
    num = 刺客 // 2
    if num:
        couples += num
    num = 斗士 // 2
    if num:
        couples += num
    num = 法师 // 2
    if num:
        couples += num
    num = 圣盾使 // 2
    if num:
        couples += num
    num = 狙神 // 2
    if num:
        couples += num
    num = 秘术师 // 2
    if num:
        couples += num
    num = 破法战士 // 2
    if num:
        couples += num
    num = 强袭枪手 // 2
    if num:
        couples += num
    num = 重装战士 // 2
    if num:
        couples += num

    return names, couples

# 人口等级
people = 9
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
    with open('lol.txt', 'a', encoding='utf-8') as f:
        with tqdm(total=eight()) as pbar:
            for x in all_couples:
                pbar.update(1)
                names, couple = main(people, x)
                if couple >= n:
                    n = couple
                    f.write(f'{str(names)}:{couple}\n')
save_and_run()

print(f'用时{int((time()-start) // 60)}分{int((time()-start) % 60)}秒')