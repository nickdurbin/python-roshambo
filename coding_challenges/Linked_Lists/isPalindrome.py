# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    node = l
  
    # Append all nodes to form a string  
    temp = [] 
    while node is not None:
        temp.append(node.value) 
        node = node.next
    string = ""
    for el in temp:
        string += str(el)

    return string == string[::-1]