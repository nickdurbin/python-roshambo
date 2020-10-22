# What is recursion?
# When a function calls itself
​
# needs a base case: the condition where you don't need to recurse
# changes state to move towards the base case
# the function needs to call itself
​
def countdown(n):
    if n == 0:   # base case
        return
​
    print(n)
    countdown(n - 1)   # call itself and move towards the base case
​
​
# countdown(5)
​
def countdown_for_loop(n):
    for i in range(n, 0, -1):
        print(i)
​
​
def countdown_while(n):
    while n > 0:  # the base case is when n <= 0, we stop looping
        print(n)
        n = n - 1  # moving closer the base case
​
​
# Write a recursive search function that receives as input an array of integers and a target integer value.
# This function should return True if the target element exists in the array, and False otherwise.
​
# 1. What would be the base case(s) we'd have to consider for implementing this function?
# 2. How should our recursive solution converge on our base case(s)?
​
# how would we do this iteratively? a linear search using a for or while loop
​
def search_iterative(nums, target):
    for num in nums:
        if num == target:  # base case
            return True
​
    return False
​
​
# we're going to call search_recursion n times
def search_recursion(nums, target, start_index):
    # What are the base cases?
    if start_index == len(nums):
        return False
​
    if nums[start_index] == target:  # need to define num
        return True
​
    search_recursion(nums, target, start_index + 1)  # move closer to base case by removing the first element that we just checked
​
​
# Binary Search:
# If you have a sorted array, you can split it in half and based on if the value is greater or less than, you know which half to search through
# Log n because we cut the search space in half with each iteration
​
def binary_search(array, target):
    # 1. Declare min = 0 and max = length of array - 1
    min = 0
    max = len(array) - 1
    while not max < min:  # BASE CASE -- when max < min, that means there's no more array to search and we return -1
        # 2. Figure out the guess value by getting the middle integer between min and max
        guess = (max + min) // 2
        # 3. if array[guess] equals the target, we found the element, return the index
        if array[guess] == target:  # BASE CASE
            return guess
        # 4. if the guess was too low, reset min to be one more than the guess
        elif array[guess] < target:
            min = guess + 1
        # 5. if the guess was too high, reset max to be one less than the guess
        else:
            max = guess - 1
    # no match was found
    return -1
​
​
def binary_search_recursive(array, target, min, max):
    # Base cases:
    if max < min:   # nothing left to search
        return -1
​
    guess = (max + min) // 2
    # if array[guess] equals the target, we found the element, return the index
    if array[guess] == target:  # BASE CASE
        return guess
​
    # move closer to the base case
    # if the guess was too low, reset min to be one more than the guess
    elif array[guess] < target:
        min = guess + 1
    #if the guess was too high, reset max to be one less than the guess
    else:
        max = guess - 1
​
    return binary_search_recursive(array, target, min, max)
​
​
nums = [1, 4, 6, 14, 19, 22, 35, 39, 40]
target = 50
print(binary_search(nums, target))
print(binary_search_recursive(nums, target, 0, len(nums) - 1))
