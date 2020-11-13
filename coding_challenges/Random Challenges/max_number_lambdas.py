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

# the_string = "lambda"
# text_list = []
# for i in the_string:
#     text_list.append(text.count(i))
# return(min(text_list))

# def csMaxNumberOfLambdas(text):
#     # UNDERSTAND
#     # return an int
#     # all we care about is the number of times the characters "l", "a" (x 2 or divided by 2), "m", "b", "d" appear in text
#     # build a dictionary with "l"/"a"/ etc... as the keys, and their frequency in text as the values
#     lambda_counts = {}
#     for char in text: 
#         if char not in "lambda": 
#             continue
#         if char in lambda_counts: 
#             lambda_counts[char] += 1
#         else: 
#             lambda_counts[char] = 1
#     # look at the values for each char and return the minimum ( divide by 2 for a)
#     min_value = None
#     for char, count in lambda_counts.items(): 
#         if char == "a": 
#             count = count // 2 # integer division, if there are 3 a's, can only make 1 lambda
#         if min_value is None or count < min_value: 
#             min_value = count
#     return min_value    
# def csMaxNumberOfLambdas_original(text):
#     lambda_counts = {}
#     for char in text: 
#         if char not in "lambda": 
#             continue
#         if char in lambda_counts: 
#             lambda_counts[char] += 1
#         else: 
#             lambda_counts[char] = 1
#     num_lambdas = 0
#     while True: 
#         made_lambda = True
#         for char in "lambda": 
#             if char not in lambda_counts: 
#                 made_lambda = False
#                 break
#             lambda_counts[char] -= 1
#             if lambda_counts[char] < 0:
#                 made_lambda = False
#                 break
#         if made_lambda: 
#             num_lambdas += 1
#         else: 
#             break
#     return num_lambdas