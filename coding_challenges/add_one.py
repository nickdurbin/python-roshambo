"""
You are given a non-empty array that represents the digits of a non-negative integer.
Write a function that increments the number by 1.
The digits are stored so that the digit representing the most significant place value is at the beginning of the array.
Each element in the array only contains a single digit.
You will not receive a leading 0 in your input array (except for the number 0 itself).
Example 1:
Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.
Example 2:
Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.
Example 3:
Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
def plus_one(digits):
    # Your code here
    index = len(digits) - 1
    # loop until: until the current number is not 9 --> loop while the current number (digits[index]) is 9
    while index >= 0:
        # if the current number is 9:
        if digits[index] == 9:
            # set digits[index] = 0
            digits[index] = 0
            # repeat with the previous number
            index = index - 1
        # if it's not 9:
        else:
            # add 1 to digits[index]
            digits[index] += 1
            break
    # if we get to the beginning and it's 9 (index at 0): make it 10 (insert 1 at the beginning)
    if index == -1:
        digits.insert(0, 1)
    return digits
def plus_one_v2(digits):
    # Your code here
    index = len(digits) - 1
    # loop until: until the current number is not 9 --> while the current number is 9
    while index >= 0 and digits[index] == 9:
        # if the number is a 9:
        #   make it zero, and repeat w/ previous number
        #   set digits[i] to 0
        digits[index] = 0
        # decrement index
        index = index - 1
    # if we get to the first number (index == 0) and it's a 9, make it a 10 (insert 1 at the 0th index)
    if index == -1:
        digits.insert(0, 1)
    else:
        # else if it's not a 9:
        #   add 1 to digits[i]
        digits[index] += 1
    return digits
# print(plus_one([1,3,2]))
# print(plus_one([3, 2, 1, 9]))
print(plus_one([9, 9, 9]))