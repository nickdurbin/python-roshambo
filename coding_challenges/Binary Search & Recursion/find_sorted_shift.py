'''
You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) and a target value.

Write a function that returns the target value's index. If the target value is not present in the array, return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums 
'''

def findValueSortedShiftedArray(nums, target):
    min_nums = 0
    max_nums = len(nums) - 1
    mid_nums = (min_nums + max_nums) // 2
    if mid_nums == target:
        return nums.index(target)
    elif target > mid_nums:
        min_nums = mid_nums + 1
    else:
        max_nums = mid_nums - 1
    if target not in nums:
        return -1
    return nums.index(target)
