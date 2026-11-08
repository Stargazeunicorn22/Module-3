def fizzbuzz():
  x = 1
  while True:
    if x % 3 == 0 and x % 5 == 0:
      y = "fizz buzz"
    elif x % 3 == 0:
      y = "fizz"
    elif x % 5 == 0:
      y = "buzz"
    else:
      y = str(x)
    print("Computer:", y)
    x = x + 1

    if x == 20:
      print("Computer: 20 is passed")
      x = x + 1
      pass
      continue

    if x % 3 == 0 and x % 5 == 0:
      y = "fizz buzz"
    elif x % 3 == 0:
      y = "fizz"
    elif x % 5 == 0:
      y = "buzz"
    else:
      y = str(x)
    z = input("Your turn: ")

    if z != y:
      print("Wrong! Computer expected:", y)
      print("Breaking program...")
      break
    x = x + 1

fizzbuzz()
