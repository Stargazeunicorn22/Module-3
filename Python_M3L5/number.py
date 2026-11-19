import random
num = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == num:
    print("Congrats! You guessed it right!")
else:
    print(f"Sorry, the correct number was {num}. Try again.")