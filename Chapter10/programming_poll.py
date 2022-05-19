filename = 'programing_poll.txt'

with open(filename, 'a') as file_object:
    while True:
        response = input("Why do you like programming ('q' to quit)> ")
        if response == 'q':
            break
        file_object.write(f"{response}\n")
