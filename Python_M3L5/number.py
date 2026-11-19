import random

num = random.randint(1, 10)
max_attempts = 5

print("Welcome to the Number Game! Guess a number between 1 and 10.")

for attempt in range(1, max_attempts + 1):
    try:
        user_guess = int(input(f"\nAttempt {attempt}/{max_attempts} - Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")
        continue

    if user_guess == num:
        print(f"Congratulations! You guessed the right number in {attempt} attempt(s).")
        break
    else:
        difference = abs(num - user_guess)
        
        if difference <= 2:
            hint = "Almost close! You're very near."
        elif user_guess < num:
            hint = "Too low!"
        else:
            hint = "Too high!"
            
        if attempt < max_attempts:
            print(f"Wrong guess. {hint} Try again!")
        else:
            print(f"\nGame over! You've used all {max_attempts} attempts. The number was {num}.")
