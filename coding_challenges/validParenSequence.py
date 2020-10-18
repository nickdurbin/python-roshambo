'''
ou are given a parentheses sequence, check if it's regular.

Example

For s = "()()(())", the output should be
validParenthesesSequence(s) = true;
For s = "()()())", the output should be
validParenthesesSequence(s) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string, consisting only of '(' and ')'.

Guaranteed constraints:
0 ≤ s.length ≤ 105.

[output] boolean

true is the sequence is regular and false otherwise.
'''

# class Stack:
# 	def __init__(self):
# 		self.size = 0
# 		self.storage = []

# 	def size(self):
# 		return len(self.storage)
	
# 	def first_el(self, el):
# 		self.storage.startswith(el)
	
# 	def last_el(self, el):
# 		self.storage.endswith(el)

# 	def push(self, value):
# 		self.storage.insert(0, value)

# 	def pop(self):
# 		if len(self.storage) >= 1:
# 			val = self.storage[0]
# 			self.storage.pop(0)
# 			return val
# 		else:
# 			return None
        

def validParenthesesSequence(s):
  # Create a stack for LIFO
  stack = []
  
  # Iterate over the string to check for paren characters
  for char in s:
    if char == "(": 
      stack.append(char) 
    else: 
      if not stack: 
        return False
      current_char = stack.pop() 
      if current_char == '(': 
        if char != ")": 
          return False
    
  if len(s) <= 0:
    return True
      
  if "(" not in s and ")" not in s:
    return False
      
  if s.startswith(")") or s.endswith("("):
    return False
  
  if len(s) % 2 != 0:
    return False
  else:
    return True

# def validParenthesesSequence(s):
#     # what are the rules? 
#     # Every open parenthesis needs a close
#     # number of open == number of closed
#     # number of unclosed open parenthesis needs to be 0 by the end of s
#     # you can't have a close before a corresponding open
#     # iterate through s
#     # keep track of the number of dangling open parens
#     num_open = 0
#     for c in s:
#     # if the character is an open paren: increase dangling open parens
#         if c == "(":
#             num_open = num_open + 1
#     # if it's a closed paren: decrease dangling open parens
#         elif c == ")": 
#             num_open = num_open - 1
#     # if at any point we have a close before an open, we can return false
#         if num_open < 0: 
#             return False
#     return num_open == 0