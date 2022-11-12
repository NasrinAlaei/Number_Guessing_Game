import random

# Selection of a random number between 0 and 100 by the system
sys_num = random.randint(1, 100)
print(sys_num)

user_num = input("Is the system guessing right?\nif guss is high: h\nif guss is low: l\nif guss is true: y")

correct_guess = 0
while correct_guess < 10:
    if user_num == 'l':
        print("guess is low")
        sys_num = (random.randint(sys_num, 99))

    elif user_num == 'h':
        print('guess is high')
        sys_num = (random.randint(1, sys_num))

    elif user_num == 'y':
        print(f"wooow!! it's true , num was {sys_num}")
        break

    else:
        print("invalid error!")

    print(sys_num)
    user_num = input("Is the system guessing right?")
    correct_guess +=1


if correct_guess == 10 and user_num != 'y':
    print(f"oops!! :( ")