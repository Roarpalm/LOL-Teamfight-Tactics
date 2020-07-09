f = open('lol9.txt', 'r', encoding='utf-8')
num = 0
for line in f:
    num += 1
    print(num)
    if '慎' in line:
        if '亚索' in line:
            if '易' in line:
                if '劫' in line:
                    if '菲奥娜' in line:
                        if '锐雯' in line:
                            if '艾瑞莉娅' in line:
                                if '艾克' in line:
                                    if '锤石' in line:
                                        print(line)
                                        break
f.close()