## chess.py【已过时】
爬取 [https://lolchess.gg](https://lolchess.gg/statistics/meta/deck/MA) 的吃鸡阵容，并稍作统计

推荐使用模拟器：https://lolchess.gg/builder/
## S3.5.py【已过时】
## S5.py
穷举法统计各人口的组合种类

运行速度有点慢

计算在M个选项中选N个不重复的选项有多少种组合方式的公式为

```python
M! / [(M-N)! * N!]
```

也可使用代码

```python
len(list(itertools.combinations(all_heroes, people)))
```

- - - -

算羁绊组合有什么用呢？通过穷举法得到在各人口能凑出来最多羁绊的阵容，羁绊多的“拼多多”阵容就一定强吗？不一定，但很有意思

4人口有且仅有一种组合可以达到4人口4羁绊：

[弗拉基米尔, 索拉卡, 锐雯, 亚索]

5人口想达成5羁绊需要4费棋子，共33种

6人口有83种组合可达成6羁绊

7人口有4种组合可达成8羁绊，得益于许多4费5费棋子有双种族或双职业

[弗拉基米尔, 古拉加斯, 魔腾, 卡尔玛, 黛安娜, 艾翁, 沃利贝尔]

[弗拉基米尔, 魔腾, 锐雯, 卡尔玛, 莫德凯撒, 黛安娜, 艾翁]

[古拉加斯, 卡兹克, 索拉卡, 魔腾, 卡尔玛, 艾翁, 沃利贝尔]

[索拉卡, 魔腾, 亚索, 卡尔玛, 莫德凯撒, 黛安娜, 艾翁]

8人口有8种组合可达成9羁绊，重点依赖黛安娜、艾翁、沃利贝尔这三个棋子

[弗拉基米尔, 古拉加斯, 特朗德尔, 魔腾, 卡尔玛, 黛安娜, 艾翁, 沃利贝尔]

[弗拉基米尔, 古拉加斯, 魔腾, 潘森, 卡尔玛, 黛安娜, 艾翁, 沃利贝尔]

[弗拉基米尔, 古拉加斯, 魔腾, 锐雯, 莫德凯撒, 黛安娜, 艾翁, 沃利贝尔]

[弗拉基米尔, 古拉加斯, 魔腾, 卡尔玛, 莫德凯撒, 黛安娜, 艾翁, 沃利贝尔]

[弗拉基米尔, 魔腾, 锐雯, 卡尔玛, 莫德凯撒, 黛安娜, 艾翁, 沃利贝尔]

[古拉加斯, 索拉卡, 魔腾, 亚索, 莫德凯撒, 黛安娜, 艾翁, 沃利贝尔]

[古拉加斯, 魔腾, 亚索, 卡尔玛, 莫德凯撒, 黛安娜, 艾翁, 沃利贝尔]

[索拉卡, 魔腾, 亚索, 卡尔玛, 莫德凯撒, 黛安娜, 艾翁, 沃利贝尔]

通过对各人口的分别穷举，最多羁绊阵容出现了难得的统一性、传承性和可成长性，所需要的全部棋子都在这个范围内：

[弗拉基米尔, 古拉加斯，索拉卡, 锐雯, 亚索，魔腾，卡尔玛, 莫德凯撒, 黛安娜, 艾翁, 沃利贝尔]

后3只是必备，铁男如此强势的版本可以让铁男当主C所以也是必备，配合后3只的魔腾也是必备，剩下的3个摇摆位，亚索or锐雯出征服者，选亚索就补2个黎明，选锐雯就补黑夜+黎明

## 事实证明，这套“拼多多”就是纯垃圾阵容，看似羁绊很多，但多数羁绊是服务自身的而不是团队的，索拉卡魔腾亚索卡尔玛没有装备屁用没有，搭出来一堆羁绊也无法提升强度，到底是要靠铁男C，那为什么不玩征服者呢

- - - -

# 写在11.9版本的吐槽

新赛季新主题新羁绊新组合总是令人兴奋，但很快就被屎一样的平衡浇灭热情

什么样的版本是糟糕的版本呢？任何有赌狗阵容的版本，任何某套阵容成型既吃鸡的版本

为何我如此痛恨低费赌狗阵容？因为这是没有技术含量把胜负完全交给发牌员的打法，因为他完全没有运营和转型变阵的乐趣。目前的赌狗阵容就是魔女刺，带黑蓝buff的妖姬技能释放无CD无间隔无需平A控到死。成型快强度高，前期走连败速7D到死就完事了

我在5月2号到5月3号的24小时之内，把一个完全没打过云顶排位的号从定级赛直接打到白金4，16把吃了11把鸡，只用一套征服者铁男，任何开局都能硬玩。上白金后就玩不动了，因为同行太多

![Instructions](征服者铁男.jpg?raw=true)

说一下前期，狼人这1费棋子强度爆表，前期拿到2星狼人就稳住连胜；丧尸打工强度爆表，拿到努努就起飞。3龙族强度一般但越早来吃的经济越多，这3套可完全看发牌员脸色，前期全交给运气

下棋的乐趣就这么被平衡破坏了，8家里2家魔女3家铁男，剩下3家游侠或龙族或小恶魔。变阵？运营？见招拆招？不存在的，谁先拿到2星铁男谁锁血，谁先成型谁吃分。

让我觉得过分的是，8人口升9人口需要80块钱，太贵了，9人口完全就是给胡得不得了的人更胡的机会，而不是给后期阵容一个质变的救命稻草。现版本节奏很快，7人口不能提升质量就要被血入，8人口就决定谁吃分谁掉分了。我上面说的那些强势阵容，没有一个是冲着9人口做规划，而是8人口全员2星足矣。

- - - -

# 以下为S3赛季结论

##### 4人口特殊，有134种3羁绊和2种4羁绊，分别是：

['魔腾', '萨科', '卡尔玛', '卡西奥佩娅']

['俄洛伊', '布里茨', '克格莫', '伊泽瑞尔']

##### 5人口最多4羁绊，2121种
##### 6人口最多6羁绊，25种
##### 7人口最多6羁绊，32210种
##### 8人口最多8羁绊，320种
##### 9人口最多8羁绊，137924种
（算9人口的代码跑了快一个星期的上班时间）

- - - -

# 写在 10.11 版本的吐槽

先说结论：这是一个不好玩的版本，这是一个僵化的版本，这是一个运气大于操作的版本。

前期一费牌概率大增，于是出现了许多以3星1费牌为核心的阵容：赌女警、赌霞、虚空斗刺法。

这些阵容的特点在于，打完石头人3-1那里一波梭哈，追出3星1费牌，追到了，在其他阵容3阶段4阶段还在打工转型期的时候已经开始发力狠狠地下别人血线

而新加入的小小小小英雄星系的高概率（12.5%）出现又通通在支持这些前期阵容。

但是如果追不到的话，到5级以后就很难继续追一费牌，而此时既没有存款也没有人口，很容易就开始连败。

上面是说以赌狗阵容为主的前期阵容，下面说后期阵容。

后期阵容大概有：以天使为核心的6剑或拼多多、6源计划、6暗星、6奥德赛、爆破4海盗、斗枪等。

这些阵容的问题在于，极度依赖4费和5费牌。

上7人口搜不到天使，6剑根本锁不住血

上8人口搜不到艾克，6源计划都凑不起来

上8人口搜不到泽拉斯，暗星就是废物

上8人口搜不到船长，奥德赛和4海盗也很艰难

反之呢？如果在5人口6人口就白嫖到核心4费牌，在7人口8人口轻易就搜到2星5费牌，这些阵容又过于强力。

这种强度因一张牌（泽拉斯）而两极分化严重的阵容我点名批评暗星

分析完前期阵容和后期阵容，问题很明显了：打得再好不如来牌来的好。

现在下棋基本上都是2阶段选定一个阵容然后死追到底，因为前期升一次人口便失去了玩赌狗阵容的资格。

赌狗在3阶段收获3个3星一费，便笑眯眯连胜到吃鸡，反之大骂发牌员然后出去下一把。

玩后期阵容的在4阶段搜不到核心4费牌，又因为赌狗过于强力而血线危险，越D越没钱升人口；又或者认准连败，速8搜牌结果搜不到，大骂发牌员然后出去下一把。

我还没说这些单核后期阵容被刺客克制得多惨，这也是机甲刺和虚空斗刺盛行的原因。

上述都是我在钻3-钻1段的感想，也许低分段会好玩些。

我很怀念以前的云顶之弈，那时候阵容丰富，那时候见招拆招，那时候可能到3阶段4阶段还在思考转型成什么阵容，那时候我还能5黑下棋，特别欢乐。

自从大家发现打不过只能加入、打不过就是运气不好之后，我的朋友们不下棋了，我现在也觉得很没意思。

等一个季中大改真香。

# 写在 10.14 版本的吐槽

拳头的平衡师真是狗改不了吃屎

现在不是暗星就是女团，不玩暗星和女团的不是因为不想玩而是因为抢不过牌

40蓝辛德拉能活着走出测试服，上线正式服之后才紧急削弱就离谱

加强暗星可以，但是把每个暗星棋子都加强一遍就你妈个臭逼的离谱

当初暗星刺小丑1v9的时候，连续几刀把小丑砍废的是你，现在让它重新回来的也是你

皇子插个旗加的群体攻速比未来叠半天给的都高，这是一个一费棋子该有的质量吗

10.7的易剑莲 10.11的虚空斗法刺 我已经喷过一遍了，没想到现在又出现了打不过只能加入的环境

把输赢全压在抽牌的游戏可能还好玩，但是你付出许多努力苦心经营到头来因为抽牌而比不过别人的游戏绝对他妈的不好玩