# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?

# Input:
# [4,3,2,7,8,2,3,1]

input = [4,3,2,7,8,2,3,1]

# Output: 
# [2,3]

def find_duplicates(list):
  y = len(list)
  new_list = []
  for x in list:
    i = x + 1
    if x == i:
      new_list.append(i)
  return new_list

print(find_duplicates(input))


# y = 
# no_duplicates = list(filter(lambda x: (x != y), input)) 

