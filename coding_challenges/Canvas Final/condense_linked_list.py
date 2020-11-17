'''
Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. Your function should return a reference to the head of the updated linked list.

Example:
Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer node

The head node of the linked list.

[output] linkedlist.integer

The head node of the updated linked list.
'''

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
  current = node
  print(current)
  
  previous = None
  
  if current == None:
    return
      
  our_arr = []
  
  while current is not None:
    previous = current
    print(current.value)
    current = current.next
    our_arr.append(previous.value)
  
  final_list = []  
  for i in our_arr:
    if i not in final_list:
      final_list.append(i)
  
  return final_list