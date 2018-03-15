def range2(n):
    count = 0
    while count < n:
        print('count', count)
        count += 1
        sign = yield count
        if sign == 'stop':
            print("sign:", sign)
            break
        print("sign:", sign)
    return 0


new_range = range2(5)

n1 = next(new_range)
n2 = next(new_range)
n3 = next(new_range)
n4 = next(new_range)

print(n1)
print(n2)
print(n3)
print(n4)

new_range.send(None)







