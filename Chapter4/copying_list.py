# original list
pizzas = ['napolitana', 'de atún y cebolla', 'kebab']

# copying the content of the list in a new list
friends_pizzas = pizzas[:]

# append diferent pizzas to each list to check that they are different

pizzas.append('infierno')
friends_pizzas.append('merkel')

print('Original list of pizzas: ')
for pizza in pizzas:
    print(pizza.title())

print('\nCopied list of pizzas: ')
for pizza in friends_pizzas:
    print(pizza.title())