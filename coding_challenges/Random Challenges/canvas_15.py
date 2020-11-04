"""
Import the "math" module. Then, print an alphabetically sorted list of all the functions available in the "math" module that start with the letters "is".
"""
# YOUR CODE HERE
import math

for func in dir(math):
  if func.startswith("is"):
    print(func)