#!/usr/bin/python3

# A method to reverse a list
def reverse_list(numbers):
   new_list = []
   for i in range(len(numbers) -1):      
       new_list.append(numbers[-i])
   return new_list
     
   
numbers=[1,2,4,6,2,9,2,5,3,2]
print("Reversed is:", reverse_list(numbers))
