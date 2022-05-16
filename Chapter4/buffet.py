print("Original tuple: ")
foods = ('hamburguer', 'hot dog', 'chop suey', 'pizza', 'spaghetti')
for food in foods:
    print(food)

# tuples are inmutable and they not support changing a element, so the next code will raise an error
# foods[0] = 'stew'
# foods[1] = 'chicken burger'

# however we can reassing a new tuple to the variable
print("\nNew tuple: ")
foods = ('stew', 'chicken burger', 'chop suey', 'pizza', 'spaghetti')
for food in foods:
    print(food)
