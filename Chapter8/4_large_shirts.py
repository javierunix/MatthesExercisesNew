# Define a function that accepts two parameters.
#   We define default values for both parameters.
def make_shirt(size='L', text='I love Python'):
    print(f'T-Shirt of size {size.upper()} with text: "{text}".')


# Large shirt with default text.
make_shirt()
# Medium shirt with default text.
make_shirt('s')
# Shirt with any text and size
make_shirt('xl', 'Audentis Fortuna Iuvat')
