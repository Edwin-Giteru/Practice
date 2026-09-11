# A method to remove duplicate in a list without using set() method


def remove_duplicate(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers
