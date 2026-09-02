#!/usr/bin/python3

# A method to find the second largest number in a list
def second_largest(numbers):
    largest = numbers[0]
    sec_largest = numbers[1]

    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
        elif numbers[i] > sec_largest:
            sec_largest = numbers[i]    
            i+=1     

    return sec_largest

print("Second_largest:", second_largest([10, 5, 8, 12]))

