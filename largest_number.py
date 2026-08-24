# A function to find the largest number in a list
def find_largest(numbers):
    largest = numbers[0]

    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest

numbers = [3, 7, 2, 9, 4]
print(find_largest(numbers))