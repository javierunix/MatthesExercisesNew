filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while True:
        guest_name = input("Write your name ('q' to quit)> ")
        if guest_name == 'q':
            break
        file_object.write(f"{guest_name.title()}\n")
