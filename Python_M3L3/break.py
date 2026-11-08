def alpha ():
    a = input("Enter a word: ")
    found = False
    for i in a:
        if i == 'A' or i == 'a':
            found = True
            break
    if found:
        print("The letter 'A' is present in the given word.")
    else:
        print("The letter 'A' isn't present in the given word.")

alpha()