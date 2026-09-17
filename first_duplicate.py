#!/usr/bin/python3

# A method to find the first number that appears more than once in a list
def first_duplicate(numbers):
    num_dict = {}

    for i in range(0, len(numbers)):
        if numbers[i] in num_dict:
            return numbers[i]
        else:
            num_dict[numbers[i]] = 1

    return None

print("First Duplicate:", first_duplicate([2, 1, 5, 3]))       