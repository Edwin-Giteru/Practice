#!/usr/bin/python3

# A method to return the first non-repeating character in a string

def first_unique_char(text):
    char_count = {}
    for i in range(0, len(text)):
        if text[i] not in char_count:
            char_count[text[i]] = 1
        else:
            char_count[text[i]] = char_count[text[i]] + 1


    for char in text:
        if char_count[char] == 1:
            return char



print("Unique char:", first_unique_char("swiss"))       