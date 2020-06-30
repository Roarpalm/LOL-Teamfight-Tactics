from lxml import etree
from bs4 import BeautifulSoup
from datetime import datetime
import requests

class Hero():
    '''英雄属性'''
    def __init__(self, cost, name, origin, class_):
        # 等级
        self.cost = cost
        # 名称
        self.name = name
        # 种族
        self.origin = origin
        # 职业
        self.class_ = class_

class Spider():
    def __init__(self):
        self.url = 'https://lolchess.gg/statistics/meta/deck/MA'
        self.header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        with open('lol.txt', 'a', encoding='utf-8') as f:
            f.write(datetime.now().strftime('%Y.%m.%d %H:%M:%S') + '\n\n') # 记录时间
        self.源计划 = 0
        self.重装秘 = 0
        self.斗枪 = 0
        self.奥德赛 = 0
        self.宇航员 = 0
        self.机甲 = 0
        self.战地 = 0
        self.法师 = 0
        self.剑士 = 0
        self.狙神 = 0

    def count(self, couple):
        '''统计羁绊组合'''
        星之守护者 = 0
        银河魔装机神 = 0
        星神 = 0
        奥德赛 = 0
        未来战士 = 0
        太空海盗 = 0
        源计划 = 0
        暗星 = 0
        战地机甲 = 0
        宇航员 = 0

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
        couples = []
        names = []

        for i in couple:
            names.append(i.name)
            if i.origin == '星之守护者':
                星之守护者 += 1
            if i.origin == '银河魔装机神':
                银河魔装机神 += 1
            if i.origin == '星神':
                星神 += 1
            if i.origin == '奥德赛':
                奥德赛 += 1
            if i.origin == '未来战士':
                未来战士 += 1
            if i.origin == '太空海盗':
                太空海盗 += 1
            if i.origin == '源计划':
                源计划 += 1
            if i.origin == '暗星':
                暗星 += 1
            if i.origin == '战地机甲':
                战地机甲 += 1
            if i.origin == '宇航员':
                宇航员 += 1

            if i.class_ == '剑士':
                剑士 += 1
            if i.class_ == '爆破专家':
                爆破专家 += 1
            if i.class_ == '刺客':
                刺客 += 1
            if i.class_ == '斗士':
                斗士 += 1
            if i.class_ == '法师':
                法师 += 1
            if i.class_ == '圣盾使':
                圣盾使 += 1
            if i.class_ == '狙神':
                狙神 += 1
            if i.class_ == '秘术师':
                秘术师 += 1
            if i.class_ == '破法战士':
                破法战士 += 1
            if i.class_ == '强袭枪手':
                强袭枪手 += 1
            if i.class_ == '重装战士':
                重装战士 += 1

        num = 星之守护者 // 3
        if num:
            couples.append(f'{星之守护者}星之守护者')
        num = 银河魔装机神 // 3
        if num:
            couples.append(f'{银河魔装机神}银河魔装机神')
        num = 星神 // 2
        if num:
            couples.append(f'{星神}星神')
        num = 奥德赛 // 3
        if num:
            couples.append(f'{奥德赛}奥德赛')
        num = 未来战士 // 2
        if num:
            couples.append(f'{未来战士}未来战士')
        num = 太空海盗 // 2
        if num:
            couples.append(f'{太空海盗}太空海盗')
        num = 源计划 // 3
        if num:
            couples.append(f'{源计划}源计划')
        num = 暗星 // 2
        if num:
            couples.append(f'{暗星}暗星')
        num = 战地机甲 // 2
        if num:
            couples.append(f'{战地机甲}战地机甲')
        num = 宇航员 // 3
        if num:
            couples.append(f'{宇航员}宇航员')

        num = 剑士 // 3
        if num:
            couples.append(f'{剑士}剑士')
        num = 爆破专家 // 2
        if num:
            couples.append(f'{爆破专家}爆破专家')
        num = 刺客 // 2
        if num:
            couples.append(f'{刺客}刺客')
        num = 斗士 // 2
        if num:
            couples.append(f'{斗士}斗士')
        num = 法师 // 2
        if num:
            couples.append(f'{法师}法师')
        num = 圣盾使 // 2
        if num:
            couples.append(f'{圣盾使}圣盾使')
        num = 狙神 // 2
        if num:
            couples.append(f'{狙神}狙神')
        num = 秘术师 // 2
        if num:
            couples.append(f'{秘术师}秘术师')
        num = 破法战士 // 2
        if num:
            couples.append(f'{破法战士}破法战士')
        num = 强袭枪手 // 2
        if num:
            couples.append(f'{强袭枪手}强袭枪手')
        num = 重装战士 // 2
        if num:
            couples.append(f'{重装战士}重装战士')

        return names, couples

    def get_name(self):
        '''爬取最新吃鸡阵容'''
        response = requests.get(self.url, headers=self.header)
        if response.status_code != 200:
            print(response.status_code)
            return None
        html = response.content.decode('utf-8')
        tree = etree.HTML(html)
        for n in range(1,26):
            galaxy = tree.xpath(f'//*[@id="wrapper"]/div/div[7]/div[{n}]/div[1]/div[1]/div[2]/text()')[0]
            galaxy = str(galaxy).replace(' ', '').replace('\n', '')
            if galaxy == 'NormalGalaxy':
                galaxy = '普通星系'
            if galaxy == 'BinaryStar':
                galaxy = '装备限持星系'
            if galaxy == 'TradeSector':
                galaxy = 'DD星系'
            if galaxy == 'TheNeekoverse':
                galaxy = '妮蔻星系'
            if galaxy == 'TreasureTrove':
                galaxy = '战利品星系'
            if galaxy == 'LittlerLegends':
                galaxy = '小小星系'
            if galaxy == 'GalacticArmory':
                galaxy = '军械库星系'
            if galaxy == 'SuperdenseGalaxy':
                galaxy = '自然之力星系'
            if galaxy == 'StarCluster':
                galaxy = '2星选秀星系'

            names = tree.xpath(f'//*[@id="wrapper"]/div/div[7]/div[{n}]/div[1]/div[4]/div/div/img/@alt')
            couple = []
            for i in names:
                if i == 'TwistedFate':
                    i = Hero(1, '崔斯特', '未来战士', '法师')
                    couple.append(i)
                if i == 'Caitlyn':
                    i = Hero(1, '凯特琳', '未来战士', '狙神')
                    couple.append(i)
                if i == 'Malphite':
                    i = Hero(1, '墨菲特', '奥德赛', '斗士')
                    couple.append(i)
                if i == 'Nocturne':
                    i = Hero(1, '魔腾', '战地机甲', '刺客')
                    couple.append(i)
                if i == 'Jarvan IV':
                    i = Hero(1, '嘉文四世', '暗星', '圣盾使')
                    couple.append(i)
                if i == 'Poppy':
                    i = Hero(1, '波比', '星之守护者', '重装战士')
                    couple.append(i)
                if i == 'Leona':
                    i = Hero(1, '蕾欧娜', '源计划', '重装战士')
                    couple.append(i)
                if i == 'Graves':
                    i = Hero(1, '格雷福斯', '太空海盗', '强袭枪手')
                    couple.append(i)
                if i == 'Fiora':
                    i = Hero(1, '菲奥娜', '源计划', '剑士')
                    couple.append(i)
                if i == 'Ziggs':
                    i = Hero(1, '吉格斯', '奥德赛', '爆破专家')
                    couple.append(i)
                if i == 'Zoe':
                    i = Hero(1, '佐伊', '星之守护者', '法师')
                    couple.append(i)
                if i == 'Illaoi':
                    i = Hero(1, '俄洛伊', '战地机甲', '斗士')
                    couple.append(i)
                if i == 'Xayah':
                    i = Hero(1, '霞', '星神', '剑士')
                    couple.append(i)
                if i == 'Annie':
                    i = Hero(2, '安妮', '银河魔装机神', '法师')
                    couple.append(i)
                if i == 'Xin Zhao':
                    i = Hero(2, '赵信', '星神', '圣盾使')
                    couple.append(i)
                if i == 'Blitzcrank':
                    i = Hero(2, '布里茨', '未来战士', '斗士')
                    couple.append(i)
                if i == 'Mordekaiser':
                    i = Hero(2, '莫德凯撒', '暗星', '重装战士')
                    couple.append(i)
                if i == 'KogMaw':
                    i = Hero(2, '克格莫', '战地机甲', '强袭枪手')
                    couple.append(i)
                if i == 'Shen':
                    i = Hero(2, '慎', '未来战士', '剑士')
                    couple.append(i)
                if i == 'Ahri':
                    i = Hero(2, '阿狸', '星之守护者', '法师')
                    couple.append(i)
                if i == 'Nautilus':
                    i = Hero(2, '诺提勒斯', '宇航员', '重装战士')
                    couple.append(i)
                if i == 'Darius':
                    i = Hero(2, '德莱厄斯', '太空海盗', '破法战士')
                    couple.append(i)
                if i == 'Yasuo':
                    i = Hero(2, '亚索', '奥德赛', '剑士')
                    couple.append(i)
                if i == 'Lucian':
                    i = Hero(2, '卢锡安', '源计划', '强袭枪手')
                    couple.append(i)
                if i == 'Zed':
                    i = Hero(2, '劫', '奥德赛', '刺客')
                    couple.append(i)
                if i == 'Rakan':
                    i = Hero(2, '洛', '星神', '圣盾使')
                    couple.append(i)
                if i == 'Master Yi':
                    i = Hero(3, '易', '奥德赛', '剑士')
                    couple.append(i)
                if i == 'Ashe':
                    i = Hero(3, '艾希', '星神', '狙神')
                    couple.append(i)
                if i == 'Shaco':
                    i = Hero(3, '萨科', '暗星', '刺客')
                    couple.append(i)
                if i == 'Karna':
                    i = Hero(3, '卡尔玛', '暗星', '秘术师')
                    couple.append(i)
                if i == 'Vayne':
                    i = Hero(3, '薇恩', '源计划', '狙神')
                    couple.append(i)
                if i == 'Rumble':
                    i = Hero(3, '兰博', '银河魔装机神', '爆破专家')
                    couple.append(i)
                if i == 'Cassiopeia':
                    i = Hero(3, '卡西奥佩娅', '战地机甲', '秘术师')
                    couple.append(i)
                if i == 'Ezreal':
                    i = Hero(3, '伊泽瑞尔', '未来战士', '强袭枪手')
                    couple.append(i)
                if i == 'Jayce':
                    i = Hero(3, '杰斯', '太空海盗', '重装战士')
                    couple.append(i)
                if i == 'Syndra':
                    i = Hero(3, '辛德拉', '星之守护者', '法师')
                    couple.append(i)
                if i == 'Vi':
                    i = Hero(3, '蔚', '源计划', '斗士')
                    couple.append(i)
                if i == 'Bard':
                    i = Hero(3, '巴德', '宇航员', '秘术师')
                    couple.append(i)
                if i == 'Neeko':
                    i = Hero(3, '妮蔻', '星之守护者', '圣盾使')
                    couple.append(i)
                if i == 'Soraka':
                    i = Hero(4, '索拉卡', '星之守护者', '秘术师')
                    couple.append(i)
                if i == 'Teemo':
                    i = Hero(4, '提莫', '宇航员', '狙神')
                    couple.append(i)
                if i == 'Irelia':
                    i = Hero(4, '艾瑞莉娅', '源计划', '剑士')
                    couple.append(i)
                if i == 'Wukong':
                    i = Hero(4, '孙悟空', '未来战士', '重装战士')
                    couple.append(i)
                if i == 'Riven':
                    i = Hero(4, '锐雯', '未来战士', '剑士')
                    couple.append(i)
                if i == 'Fizz':
                    i = Hero(4, '菲兹', '银河魔装机神', '刺客')
                    couple.append(i)
                if i == 'Viktor':
                    i = Hero(4, '维克托', '战地机甲', '法师')
                    couple.append(i)
                if i == 'Gnar':
                    i = Hero(4, '纳尔', '宇航员', '斗士')
                    couple.append(i)
                if i == 'Jhin':
                    i = Hero(4, '烬', '暗星', '狙神')
                    couple.append(i)
                if i == 'Jinx':
                    i = Hero(4, '金克斯', '奥德赛', '强袭枪手')
                    couple.append(i)
                if i == 'Urgot':
                    i = Hero(5, '厄加特', '战地机甲', '圣盾使')
                    couple.append(i)
                if i == 'Janna':
                    i = Hero(5, '迦娜', '星之守护者', '大魔法使')
                    couple.append(i)
                if i == 'Gangplank':
                    i = Hero(5, '普朗克', '太空海盗', '爆破专家')
                    couple.append(i)
                if i == 'Xerath':
                    i = Hero(5, '泽拉斯', '暗星', '法师')
                    couple.append(i)
                if i == 'Lulu':
                    i = Hero(5, '璐璐', '星神', '秘术师')
                    couple.append(i)
                if i == 'Aurelion Sol':
                    i = Hero(5, '龙王', '奥德赛', '星舰龙神')
                    couple.append(i)
                if i == 'Ekko':
                    i = Hero(5, '艾克', '源计划', '刺客')
                    couple.append(i)
                if i == 'Thresh':
                    i = Hero(5, '锤石', '未来战士', '破法战士')
                    couple.append(i)
            team, couples = self.count(couple)
            if '斗士' in couples and '强袭枪手' in couples:
                self.斗枪 += 1
            if '4重装战士' in couples and '秘术师' in couples:
                self.重装秘 += 1
            if '6源计划' in couples:
                self.源计划 += 1
            if '6奥德赛' in couples:
                self.奥德赛 += 1
            if '3银河魔装机神' in couples:
                self.机甲 += 1
            if '3宇航员' in couples:
                self.宇航员 += 1
            if '4战地机甲' in couples or '6战地机甲' in couples:
                self.战地 += 1
            if '4法师' in couples or '5法师' in couples or '6法师' in couples:
                self.法师 += 1
            if '6剑士' in couples:
                self.剑士 += 1
            if '4狙神' in couples:
                self.狙神 += 1

            with open('lol.txt', 'a', encoding='utf-8') as f:
                f.write(galaxy + '\n')
                for i in team:
                    f.write(i + ' ')
                f.write('\n')
                for i in couples:
                    f.write(i + ' ')
                f.write('\n\n')

        print(f'源计划：{self.源计划}')
        print(f'重装秘：{self.重装秘}')
        print(f'奥德赛：{self.奥德赛}')
        print(f'机甲：{self.机甲}')
        print(f'斗枪：{self.斗枪}')
        print(f'宇航员：{self.宇航员}')
        print(f'战地：{self.战地}')
        print(f'法师：{self.法师}')
        print(f'剑士：{self.剑士}')
        print(f'狙神：{self.狙神}')
        
if __name__ == "__main__":
    print('开始运行...')
    spider = Spider()
    spider.get_name()