# 有多种属性（本案例中有5种），每个对象的每个属性对应一个值；有多个对象（本案例中有6个），每个对象需求如下：
# 1、选择与属性数量相同的对象
# 2、每个对象选择一个属性，同一种属性只能选择一次
# 3、对所选对象的属性值求和并选出最大值
# 4、记录得出最大值的对象和对应的属性

import itertools

powerList = {
    'p1': [87812, 23234, 31213, 32412, 24415],
    'p2': [113223, 21345, 31328, 26734, 29645],
    'p3': [123351, 25952, 31044, 44262, 45231],
    'p4': [91432, 21236, 23895, 30154, 28515],
    'p5': [102791, 41212, 32153, 34634, 38005],
    'p6': [121791, 41682, 35153, 38634, 34005],
}
maxValue = 0
maxList = ()
currentValue = 0
for i in itertools.permutations(['p1', 'p2', 'p3', 'p4', 'p5', 'p6'], 5):
    # print(i)
    currentValue = powerList[i[0]][0] + powerList[i[1]][1] + powerList[
        i[2]][2] + powerList[i[3]][3] + powerList[i[4]][4]
    if maxValue < currentValue:
        maxValue = currentValue
        maxList = i
print(maxList)
print(maxValue)
