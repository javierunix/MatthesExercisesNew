# 1. Print the content from a file reading the entire file.
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    contents = contents.replace('Python', 'C')
print('\nReading the entire file:')
print(contents)

# 2. Print looping over lines.
print('\nReading the file line by line:')
with open('learning_python.txt') as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())

# 3. Store the contents in a list. Print the list.
print("\nStoring contents in a list:")
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('Python', 'C')
    print(line.rstrip())
