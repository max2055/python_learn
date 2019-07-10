def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


while True:
    try:
        number = input('Please input an integer（q for exit）: ')
        if number == 'q':
            break
        else:
            number = int(number)
        while True:
            number = collatz(number)
            print(number)
            if number == 1:
                break

    # except Exception as e:
    #     print(e)
    except ValueError:
        print('Invalid number.')
