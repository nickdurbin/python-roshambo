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

print(subtractProductAndSum(234))