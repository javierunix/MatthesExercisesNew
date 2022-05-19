def open_file(filename):
    """Function that opens a file and can handle FileNotFound error."""
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
            return f"\n{contents.strip()}"
    except FileNotFoundError:
        return f"\n'{filename}' not in the specified path."


print(open_file('cats.txt'))
print(open_file('dogs.txt'))
print(open_file('cats2.txt'))
