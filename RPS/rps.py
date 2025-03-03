Player_name = input("Enter your name: ") 
score = [0, 0]

def main():
    for i in range(3):
        player = Pchoices()
        computer = Rchoices()
        print(f"{Player_name}'s {player}", "vs", f"computer's {computer}")
        win(player, computer)
    if score[0] > score[1]:
        print(f"{Player_name} wins!")
    elif score[0] < score[1]:
        print("Computer wins!")
    else:
        print("It's a tie! Well played!")

def Pchoices():
    choices = ["rock", "paper", "scissors"]
    while True:
        choice = input("Enter your choice: ")
        if choice in choices:
            return choice
        else:
            print("Invalid choice, please try again")

def Rchoices():
    import random
    choices = ["rock", "paper", "scissors"]
    random_choice = random.choice(choices)
    return random_choice

def win(P, C):
    if P == "rock" and C == "scissors" or P == "scissors" and C == "paper" or P == "paper" and C == "rock":
        print(f"You win!") 
        score[0] += 1
        print(score)
    elif P == C:
        print("It's a tie!")
        print(score)
    else:
        print("You lose!")
        score[1] += 1
        print(score)

main()