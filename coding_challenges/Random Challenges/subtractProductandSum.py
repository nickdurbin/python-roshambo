'''
  Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''

def subtractProductAndSum(n):
  product = 1
  sum_of = 0
  lst = [int(i) for i in str(n)]
  
  for i in lst:
    product *= i
    
  for j in lst:
    sum_of += j
  
  return product - sum_of

# One liner with functools
# return functools.reduce(lambda x,y:x*y,list(map(int,str(n))))-sum(list(map(int,str(n))))

print(subtractProductAndSum(234))

# C++ Solution

#class Solution {
# public:
#     int subtractProductAndSum(int n) {
#         int prod = 1;
#         int sum = 0;
#         while (n > 0)
#         {
#             int x =  n % 10;
#             n /= 10;
#             prod *= x;
#             sum += x;
#         }
#         return prod - sum;
#     }
# };