def common_words(filename, word):
    """Function to count the number of times a given word appears in a file."""
    try:
        with open(filename, 'r') as file_object:
            # Load the entire file in a variable. Cast to lowercas.
            content = file_object.read().lower()
            # Strip whitespaces in the file content.
            content = content.strip()
            # Cast target word to lowercase.
            word = word.lower()
            # Strip whitespaces.
            word = word.strip()

            # Count number of word ocurrences.
            return content.count(word)

    except FileNotFoundError:
        return f"File {filename} not found."


print(common_words('newton_principia_lt.txt', 'motus'))
