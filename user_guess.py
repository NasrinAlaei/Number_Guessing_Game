import random

sys_num = random.randint(1, 100)

user_num = int(input("whats your guess?\n"))

curr_num = 0
while curr_num < 10:
    curr_num += 1

    if user_num < sys_num:
        print("your guss is low")

    elif user_num > sys_num:
        print("your guess is high")

    elif user_num == sys_num:
        break

    user_num = int(input("whats your guess?\n"))


if user_num == sys_num:
    print(f"woow!! your guess is true!\n'You guessed the number in ' {curr_num} ' tries!'")
else:
    print(f"oops! it's false , num was {sys_num}")
