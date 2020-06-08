运行速度有点慢，双核老古董电脑在算7人口的时候跑了32分钟

计算在M个选项中选N个不重复的选项有多少种组合方式的公式为

```python
M! / [(M-N)! * N!]
```

也可使用代码

```python
len(list(itertools.combinations(all_heroes, people)))
```

目前（S3 10.11版本）有52个英雄，4人口有270,725种组合，5人口有2,598,960种组合，6人口有20,358,520种组合，7人口有133,784,560种组合，8人口有752,538,150种组合，9人口有3,679,075,400种组合。

结论：

#### 4人口时最多3羁绊，156种

#### 5人口时最多4羁绊，640种

#### 6人口特殊，有300种5羁绊和3种6羁绊，分别是：

['凯特琳', '格雷福斯', '德莱厄斯', '艾希', '卡萨丁', '伊泽瑞尔']

['凯特琳', '德莱厄斯', '艾希', '卡萨丁', '杰斯', '孙悟空']

['格雷福斯', '赵信', '洛', '伊泽瑞尔', '杰斯', '孙悟空']

#### 7人口最多6羁绊，3354种

#### 8人口特殊，有2471种7羁绊和3种8羁绊，分别是：

['凯特琳', '格雷福斯', '赵信', '德莱厄斯', '洛', '艾希', '卡萨丁', '伊泽瑞尔']

['凯特琳', '格雷福斯', '艾希', '卡萨丁', '伊泽瑞尔', '杰斯', '孙悟空', '锤石']

['凯特琳', '赵信', '德莱厄斯', '洛', '艾希', '卡萨丁', '杰斯', '孙悟空']

#### 9人口最多8羁绊，5854种

（算9人口的代码连续跑了50个小时）

- - - -

#### 写在版本（10.11）的吐槽

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