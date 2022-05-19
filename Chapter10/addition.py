def addition(*nums):
    """
    Add the value of a arbitrary number of numbers.
    Can handle ValueErrorExceptions
    """
    addition = 0
    for num in nums:
        try:
            addition += int(num)
        except ValueError:
            return f"Sorry, '{num}' is a non-numerical value."
    return f"Result: {addition}"


print(addition(1, 3, 's', 78, 101, 45))
