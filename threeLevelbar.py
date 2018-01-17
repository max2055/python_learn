menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

for k, v in menu.items():
    print(k, v)

for i in menu:
    for j in menu[i]:
        print(j)
        for k in menu[i][j]:
            print(k)
            for l in menu[i][j][k]:
                print(l)

for key in menu:
    print(key)

print("1 for next level")
print("2 for last level")
print("3 to exit")

while True:
    for prov in menu:
        option = int(input("please enter your option"))
        if option == 1:
            for key in menu[prov]:
                print(key)

            for county in menu[prov]:
                option = int(input("please enter your option"))
                if option == 1:
                    for key in menu[prov][county]:
                        print(key)

                    for zone in menu[prov][county]:
                        option = int(input("please enter your option"))
                        if option == 1:
                            for key in menu[prov][county][zone]:
                                print(key)

                            option = int(input("please enter your option"))
                            if option == 2:
                                break
