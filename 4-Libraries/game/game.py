import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    if level > 0:
        break
    else:
        continue

gen = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess:" ))
    except ValueError:
        continue
    if guess > 0:
        if guess < gen:
            print("Too small!")
        elif guess > gen:
            print("Too big!")
        elif guess == gen:
            print("Just right!")
            break
