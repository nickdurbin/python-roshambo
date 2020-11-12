'''
Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda" that can be formed.

Example 1:

Input: text = "mbxcdatlas"
Output: 1
Example 2:

Input: text = "lalaaxcmbdtsumbdav"
Output: 2
Example 3:

Input: text = "sctlamb"
Output: 0
Notes:

text consists of lowercase English characters only
'''

def csMaxNumberOfLambdas(text):
  num_of_times = 0
  num_l = text.count("l")
  num_a = text.count("a")
  num_m = text.count("m")
  num_b = text.count("b")
  num_d = text.count("d")
  
  are_equal = False
  if num_m and num_b and num_d == num_l:
    are_equal = True
  
  if are_equal == True:
    if num_a == num_l * 2:
        num_of_times = num_l
  
  return num_of_times