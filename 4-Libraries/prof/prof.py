import random

def main():
    get_level()

def get_level():
    while True:
        try:
            level = int(input("Level 1, 2, or 3? "))
            if 1 <= level <= 3:
                print("Level is", level)
                generate_integer(level)
                break
        except ValueError:
            continue


def generate_integer(level):
    score = 0
    while True:
        if level == 1:
            for i in range(10):
                x = random.randint(1, 9)
                y = random.randint(1, 9) 
                z = x + y
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == z:
                    score += 1
                    continue
                elif user_answer != z:
                    print("EEE")
                    user_answer2 = int(input(f"{x} + {y} = "))
                    if user_answer2 == z:
                        score += 1
                        continue
                    elif user_answer2 != z:
                        print("EEE")
                        user_answer3 = int(input(f"{x} + {y} = "))
                        if user_answer3 == z:
                            score += 1
                        elif user_answer3 != z:
                            print(f"{x} + {y} = {z}")
                            continue
            print("Your score is", score,"/10")
            break
        elif level == 2:
            for i in range(10):
                x = random.randint(10, 99)
                y = random.randint(10, 99)
                z = x + y
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == z:
                    score += 1
                    continue
                elif user_answer != z:
                    print("EEE")
                    user_answer2 = int(input(f"{x} + {y} = "))
                    if user_answer2 == z:
                        score += 1
                        continue
                    elif user_answer2 != z:
                        print("EEE")
                        user_answer3 = int(input(f"{x} + {y} = "))
                        if user_answer3 == z:
                            score += 1
                        elif user_answer3 != z:
                            print(f"{x} + {y} = {z}")
                            continue
            print("Your score is", score,"/10")
            break
        elif level == 3:
            for i in range(10):
                x = random.randint(100, 999)
                y = random.randint(100, 999)
                z = x + y
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == z:
                    score += 1
                    continue
                elif user_answer != z:
                    print("EEE")
                    user_answer2 = int(input(f"{x} + {y} = "))
                    if user_answer2 == z:
                        score += 1
                        continue
                    elif user_answer2 != z:
                        print("EEE")
                        user_answer3 = int(input(f"{x} + {y} = "))
                        if user_answer3 == z:
                            score += 1
                        elif user_answer3 != z:
                            print(f"{x} + {y} = {z}")
                            continue
            print("Your score is", score,"/10")
            break

if __name__ == "__main__":
    main()