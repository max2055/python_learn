# 有多种属性（本案例中有5种），每个对象的每个属性对应一个值；有多个对象（本案例中有6个），每个对象需求如下：
# 1、选择与属性数量相同的对象
# 2、每个对象选择一个属性，同一种属性只能选择一次
# 3、对所选对象的属性值求和并选出最大值
# 4、记录得出最大值的对象和对应的属性

import itertools

powerList = {
    'p1': [739077, 27309, 21007, 25208, 25208],
    'p2': [751516, 35266, 28213, 32915, 32915],
    'p3': [773303, 38633, 30907, 36058, 36058],
    'p4': [778900, 42099, 33679, 39292, 39292],
    'p5': [748222, 43752, 35002, 40836, 40836],
    'p6': [722534, 32141, 25713, 29998, 29998],
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
