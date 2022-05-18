# Define a function that accepts two parameters.
def make_shirt(size, text):
    print(f'T-Shirt of size {size.upper()} with text: "{text}".')


# Call funtion with positional arguments.
make_shirt('l', 'Say my Name')
# Call the function in keyword arguments.
make_shirt(size='s', text='Make my Day')
make_shirt(text='Audentis Fortuna Iuvat', size='xl')
