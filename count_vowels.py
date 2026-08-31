#!/usr/bin/python3

# A method to count the number of vowels on a string
def count_vowels(text):
    count = 0
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for char in text:
        if char in vowels:
            count += 1

    return count

print("No of vowels:", count_vowels("Software Engineering"))
