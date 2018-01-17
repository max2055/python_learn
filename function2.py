def sayhi():
    print("hello world")

sayhi()

age = 19

def func1():
    print('Wu')
    age = 73
    print(age)
    def func2():
        age = 84
        print(age)
        print('Chenlong')

    func2()

func1()
print(age)

def calc(x,y):
    return x*y

func=lambda x,y:x*y

print(calc(2,4))

print(func(3,9))


def func(n):
    n = int(n/2)
    print(n)

    if n > 0:
        func(n)

    print(n)

func(16836538451)

