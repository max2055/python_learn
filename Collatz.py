def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


number = int(input('Please input an integer: '))

while True:
    number = collatz(number)
    print(number)
    if number == 1:
        break
