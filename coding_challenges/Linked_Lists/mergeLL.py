# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

'''
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
'''

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    # A dummy node to store the result
    dummyNode = ListNode(0)
 
    # Tail stores the last node
    tail = dummyNode
    while True:
 
        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if l1 is None:
            tail.next = l2
            break
        if l2 is None:
            tail.next = l1
            break
 
        # Compare the data of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
 
        # Advance the tail
        tail = tail.next
 
    # Returns the head of the merged list
    return dummyNode.next
