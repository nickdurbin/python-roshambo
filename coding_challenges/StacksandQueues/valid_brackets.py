'''
  Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
Example

For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
'''

def validBracketSequence(sequence):
# type_brackets = ['()', '{}', '[]']
  
  # while any(x in sequence for x in type_brackets):
  #     for br in type_brackets:
  #         sequence = sequence.replace(br, '')
  # return not sequence
  
  open_list = ["[","{","("] 
  close_list = ["]","}",")"] 

  stack = [] 
  for i in sequence: 
    if i in open_list: 
      stack.append(i) 
    elif i in close_list: 
      pos = close_list.index(i) 
      if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])): 
        stack.pop() 
      else: 
        return False
  if len(stack) == 0: 
    return True
  else: 
    return False