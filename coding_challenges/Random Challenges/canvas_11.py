"""
Use a list comprehension to create a new list called new_list out of the numbers list. Use the list comprehension to make sure that the new_list only contains positive numbers and make sure they are cast as integers into the new_list.
"""

numbers = [22.3, -184.4, 57.8, 99.6, -18.2, 84.2, 71.3]

new_list = [int(number) for number in numbers if number > 0]
print(new_list)