# write an if-elif-else chain that determine a person's stage of life

age = 65 # person age
stage = "" # stage of life

# determine the stage using if-elif-else change
if age < 2:
    stage = "baby"
elif age < 4:
    stage = "toddler"
elif age < 13:
    stage = "kid"
elif age < 20:
    stage = "teenager"
elif age < 65:
    stage = "adult"
else:
    stage = "elder"

print(f'This person is a {stage}.') # ouput message)