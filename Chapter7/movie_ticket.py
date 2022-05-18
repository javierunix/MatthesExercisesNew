while True:
    age = int(input("How old are you?"))
    if age < 3:
        print(f"You do not have to pay for a ticket.")
    elif age <= 12:
        print(f"The price of your ticket is 10$.")
    else:
        print(f"The price of your ticket is 15$.")
