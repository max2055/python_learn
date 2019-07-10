while True:
    print('who are you?')
    name=input()
    if name != 'Joe':
        continue
    print('Hello, Joe. ')
    print('What is the password?')
    while True:
        password = input()
        if password == '123456':
            print('Access Accepted')
            break
        else:
            print('Password is not correct, please input again:')
    break

