#!/usr/bin/python3

# A method to find the smallest umber in a lsit
def find_smallest(numbers):
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]

    return smallest

numbers = [3, 7, 2, 9, 4]
print(find_smallest(numbers))