# exit the loop using break.
while True:
    age = input("How old are you? 'quit' for quitting> ")
    if age == 'quit':
        break
    elif int(age) < 3:
        print(f"You do not have to pay for a ticket.")
    elif int(age) <= 12:
        print(f"The price of your ticket is 10$.")
    else:
        print(f"The price of your ticket is 15$.")
