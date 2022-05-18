message = "Choose a topping for your pizza ('quit' to quit)> "
topping = input(message)

topping = topping.lower()

while topping != 'quit':
    topping = input(message)
