import random

print("Hello welcome to guess game number")
print("By Justo")
bot_guess = random.randint(0, 10)

user_points = 0
bot_points = 0
while True:
    user_points += 1
    user_guess = input("Enter guess (0 to 10) number or q to quit: ")
    if user_guess.isdigit():
        if bot_guess == int(user_guess):
            print("Found!")
            print(f"score is {user_points}")
            break
        elif int(user_guess) > bot_guess:
            print("Your guess is greater than bot guess")
            continue
        else:
            print("Your guess is less than bot guess")
            continue

    elif user_guess.lower() == 'q':
        print("Thank you  for playing")
        break
    else:
        print("Enter a number ")
        continue

