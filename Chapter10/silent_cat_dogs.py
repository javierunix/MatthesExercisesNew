def open_file(filename):
    """
    Function that opens a file.
    Handle FileNotFound error silently.
    """
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
            return f"\n{contents.strip()}"
    except FileNotFoundError:
        pass


print(open_file('cats.txt'))
print(open_file('cats2.txt'))
print(open_file('dogs.txt'))

