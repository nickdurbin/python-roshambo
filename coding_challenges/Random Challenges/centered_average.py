def centered_average(nums):
  if len(nums) < 3:
    return "List is not long enough to run code."
  else:
    #find the max num
    max_num = max(nums)
    #find the min num
    min_num = min(nums)
    #get the sum of nums
    current_sum = sum(nums)
    #subtract the max and min from sum
    final_sum = current_sum - max_num - min_num
    #divide the value by len(nums) -2
    return final_sum // (len(nums) - 2)

print(centered_average([1,2]))

print(centered_average([1,2,3,4,100])) # result is 3

print(centered_average([1,1,5,5,10,8,7])) # result is 5

print(centered_average([-10, -4, -2, -4, -2, 0])) # result is -3
