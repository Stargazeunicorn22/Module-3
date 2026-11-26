def words(w):
    ctr = 0
    matched_list = []
    for i in w:
        if len(i) >= 2 and i[0] == i[-1]:
            ctr += 1
            matched_list.append(i)

    print("List of words with first and last character same:")
    print(matched_list)
    return ctr


user = []

while True:
    try:
        n = int(input("Enter the number of words: "))
        if n < 0:
            print("Please enter a positive number.")
        else:
            break  # Exits the loop once a valid number is entered
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except Exception as e:
        print("An error occurred:", e)

for i in range(n):
    w = input(f"Enter word {i + 1}: ")
    user.append(w)

count = words(user)
print("Number of words having first and last character same:", count)
