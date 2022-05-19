filename = 'message.txt'

with open(filename, 'w') as file_object:
    file_object.write(input("What do you want to say?> "))
