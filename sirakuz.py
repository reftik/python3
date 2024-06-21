number = int(input("You're number"))
while number != 1:
    if number % 2 == 0:
      number = number //2
    else:
      number = (3*number + 1) // 2
    print (number)