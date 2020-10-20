# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

'''
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, since this is what you will be asked to accomplish in an interview.

You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. Add value to the list l, preserving its original sorting.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [1, 3, 4, 6] and value = 5, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 5, 6];
For l = [1, 3, 4, 6] and value = 10, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 6, 10];
For l = [1, 3, 4, 6] and value = 0, the output should be
insertValueIntoSortedLinkedList(l, value) = [0, 1, 3, 4, 6].
'''

def insertValueIntoSortedLinkedList(l, value):
    if l is None: 
        return ListNode(value)
    # Iterate to the spot in the list where we want to insert the new value
    #   we're at the right spot when the next node is greater than the current value (and the previous is less than)
    prev_node = None
    next_node = l
    while next_node is not None and value > next_node.value: 
        prev_node = next_node
        next_node = next_node.next
    # insert the new value
    #   create a new node
    new_node = ListNode(value)
    #   set new node.next to next node
    new_node.next = next_node
    #   set previous node.next to new node
    if prev_node is not None: 
        prev_node.next = new_node
    else: # we're trying to insert at the beginning of the list
        l = new_node
    return l 