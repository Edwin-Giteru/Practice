#!/usr/bin/python3

def missing_numbers(numbers):
    expected_sum = 0
    actual_sum = 0

    for i in range(max(numbers) +1):
        expected_sum += i
    
    for num in numbers:
        actual_sum += num

    missing = expected_sum - actual_sum

    return missing

print("Missing number:", missing_numbers([1, 2, 4, 5]))

