import math 
from math import sqrt
​
# Constant time == O(1)
def mult_2(n): # O(1) + O(1) + O(1) + O(1) = O(4) => O(1)
  print(n) # O(1)
  if n == 5: # O(1)
    print("horray") #(1)
  return n * 2  # O(1)
​
​
# Linear time 
def foo(n): # O(n)
  for i in range(0, n): # O( n ) 
    # the total runtime of the code in the loop is O(1)
    print(i) # O(1)
    print(i) # O(1)
​
# Quadratic time (Polynomial Time)
def bar(n):  # O(1) + O(n^2) + O(1) ==> O(n^2) 
  s = 0 # O(1)
​
  # O(n) * O(n) = O(n^2)
  for i in range(0, n): # O(n)
    for j in range(0, n): # O(n) * O(1) = O(n) this loop runs in linear time
      s += i * j # O( 1 )
  
  return s # O(1)
​
# O(n) * O( sqrt(n) ) == O(n * sqrt n) === O(n ^ 1.5)
# also a variant of O(n) * log(n)
def baz(n):
  s = 0
​
  for i in range(n): # O(n)
    for j in range(int(sqrt(n))): # O( sqrt(n) )  (  or O( n^0.5 ) )
      s += i * j # O(1)
  
  return s
​
​
# When the input is halved (or another division) every step of the loop
# Think logarithmic! 
# log(n)
def divider(n):
  while n >= 1: # O( log(n)) 
    print(n) # O(1)
    n = n // 2 # O(1)
  