# Print out all of the numbers in the following array that are divisible by 3:
# [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
# 27
# 81
# 9
# 27
# 99
# 63
# 42
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible 
# before writing any code. Run through the UPER problem 
# solving framework while going through your thought process.

values =[85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

def divisible_by_three(list):
  # loop over the given array
  # divide each number by 3
  # print out each number individually
  for i in list:
    if i % 3 == 0:
      print(i)

print(divisible_by_three(values))

def divisible_by_two(list):
  for i in list:
    if i % 2 == 0:
      print(i)

print(divisible_by_two(values))