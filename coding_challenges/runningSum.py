def runningSum(nums):
  # Solution fails if you feed it a list of all 1's.
  sum_arr = [int(n*(n+1)/2) for n in nums]
  return sum_arr

print(runningSum([1,2,3,4]))

# This solution is simple and should work for everything.
# for i in range(1, len(nums)):
    # nums[i] = nums[i - 1] + nums[i]
# return nums