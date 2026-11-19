import random

while True:
    action = input("Enter ur choice (rock, paper, scissors): ")
    possible = ["rock", "paper", "scissors"]
    computer = random.choice(possible)
    print(f"\nYou chose {action}, computer chose {computer}.\n")

    if action == computer:
        print(f"Both players selected {action}. It's a tie!🙂")
    elif action == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif action == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif action == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    if (action == "rock" and computer == "scissors") or (action == "paper" and computer == "rock") or (action == "scissors" and computer == "paper"):
        break