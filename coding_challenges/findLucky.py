"""
Given a list of integers `lst`, any integer with a frequency that is equal to its value is considered a **lucky integer**.

Write a function that returns the lucky integer from the array. If the array contains multiple lucky integers, return the largest one. If there are no lucky integers return -1.

**Example 1**:

Input: arr = [2,3,3,3,4]
Output: 3

**Example 2**:

Input: arr = [1,2,2,3,3,3,4,4,4,4]
Output: 4

**Example 3**:

Input: arr = [1,1,2,2,2]
Output: -1
"""
def find_lucky(lst):
    # Your code here
    #Understand

    # We are given an array of integers and we need to see if there is one "Licky" number
    # sort reversed list .sort()
    lst.sort(reverse=True)
    print(lst)
    # create a counter
    counter = 1 
    # for loop to iterate and see what is in the list
    for c in range(len(lst)):
        # compare the integer with the next integer in the list
        c
        # if they are the same we can create counter += 1
            # if counter is == to current integer return magic number
        # else move to next integer

        # if no magic number return -1

    # return result

# def find_lucky(lst):
#     lucky = []
#     string = ''.join(map(str, lst))
#     for char in string:
#         if int(char) == string.count(char):
#             lucky.append(char)
#     if not lucky:
#         return -1
#     return max(lucky)
# print(find_lucky(lst))

# def find_lucky(lst):
#     lucky = []
    
#     for num in lst:
#         if num == lst.count(num):
#             lucky.append(num)
    
#     if lucky:
#         lucky.sort()
#         return lucky[len(lucky) - 1]
    
#     return -1

# def find_lucky(lst):
#     # Your code here
#     # holder variable for the lucky number
#       # -1
#   lucky_number = -1
#   # iterate through
#   for num in lst:
#     # identify frequency in the array of the current item
#         #  if the frequency == value of the current item (lucky)
#     if lst.count(num) == num:
#         #  if this lucky number is greater than the current lucky number (or -1) current item becomes the new lucky number 
#         if( num > lucky_number ): lucky_number = num
#   return lucky_number



# Overall run time of this solution 
# constant + n log n (for the sort) + n * n ==> O(n^2)
# O(n) Space Complexity

# IF using dictionary then time complexity goes to O(n log n)

# def find_lucky(lst):
#     # UNDERSTAND
#     # if the count = value, return the value
#     # PLAN
#     # Define an output variable
#     output = -1     
#     # Sort the list from largest to smallest
#     lst.sort(reverse=True)

        # counts = {}                    USING DICTIONARY

        # if number not in counts:
        #     counts[number] = 0
        # counts[number] += 1

#     # Make a set
#     set_list = set(lst)
#     # Iterate through the set, counting the # of times each value shows up
#     for number in set_list:
#         # Make a count variable
#         count = lst.count(number)
            # count = counts[number]   USING DICTIONARY
#         # Check if the count == the value
#         if number == count:
#             # If it does, add it to output variable
#             output = number
#     # If nothing matches, return -1
#     return output