#!/usr/bin/python3

# A method to return indices of numbers whose sum equals target

def two_sum(numbers, target):
    sum_dict = {}

    for i, number in enumerate(numbers):
        diff = target - number
        if diff in sum_dict:
           return [sum_dict[diff], i]
        sum_dict[number] = i
    return None

print("Indices:", two_sum([2,  11, 15], 9))