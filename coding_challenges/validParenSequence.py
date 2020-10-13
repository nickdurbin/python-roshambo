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