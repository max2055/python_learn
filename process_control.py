# for-else
for i in range(10):
    if i <= 5:
        print(i)
    else:
        continue
else:
    print("cycle is over")

# while-else
count = 0

while count <= 100:
    print("bye")
    count += 1
    print(count)
else:
    print("cycle is over")

# multi cycle
break_flag = False
for i in range(10000):
    print(i)
    if i == 100:
        for j in range(100):
            print(j)
            if j == 30:
                for k in range(10):
                    print(k)
                    if k == 8:
                        break_flag = True
                        break
            if break_flag:
                break
    if break_flag:
        break_flag = False
        break





