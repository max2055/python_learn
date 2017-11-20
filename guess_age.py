import random
random_bit = random.random()
print(random_bit)

age = int(random_bit*100)
print(age)

count = 0
continue_flag = ""

while count <= 3:
    count += 1
    guess = int(input("please enter your guess:"))
    if guess > age:
        print("Please try smaller!")
    elif guess < age:
        print("please try bigger!")
    else:
        print("You got it!")
        while continue_flag != "y" and continue_flag != "n":
            continue_flag = input("Do you want next round?y or n")
        if continue_flag == "y":
            count = 0
            continue_flag = ""
            continue
        elif continue_flag == "n":
            break

    if count == 3:
        print("You have played 3 times.This round is over.")
        while continue_flag != "y" and continue_flag != "n":
            continue_flag = input("Do you want next round?y or n")
        if continue_flag == "y":
            count = 0
            continue_flag = ""
            continue
        elif continue_flag == "n":
            break






