def weather():
    x = input("What is the weather there? Type a for autumn, s for spring, sum for summer, and win for winter:")
    if x == "a":
        print("Oh nice! It gets a little cold in autumn!")
    elif x== "s":
        print("Ooo my favorite; Spring!")
    elif x == "sum":
        print("Wow u must be on a school break cause its summer!")
    else:
        print("Ok time to stay safe and wear warm clothes! Cause winter is here.")

weather()