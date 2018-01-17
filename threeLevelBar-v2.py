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

current_layer = menu
last_layer = menu

while True:
    for key in current_layer:
        print(key)

    print("b to return")
    print("q to exit")

    choice = input("Enter your choice").strip()
    if not choice:
        continue

    if choice in current_layer:
        current_layer = current_layer[choice]



