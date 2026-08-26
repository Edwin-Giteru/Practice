#!/usr/bin/env python3

# A method to find the occurence of a target in a list
def count_occurrences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count

numbers=[1,2,4,6,2,9,2,5,3,2]
print("Number of Occurences:", count_occurrences(numbers, 2))

