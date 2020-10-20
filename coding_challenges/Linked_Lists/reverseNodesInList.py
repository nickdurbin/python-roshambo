# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

'''
  Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example

For l = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
'''

def reverseNodesInKGroups(l, k):
    # go in groups of k
    # check if we need to reverse the next k nodes -- 
    # if we're at the end and we have fewer than k nodes left, then we don't need to reverse
    current_node = l
    prev_group_tail = None  # This is the tail of the previous group, we'll need it to connect it to the next group
    while True:   
        if should_reverse(current_node, k):
            # reverse k nodes
            # The first node of the original group becomes the tail of the reversed group; 
            # save it so that we have access to it later since we'll need it to connect to the next group
            cur_group_tail = current_node  
            prev = None
            for i in range(k): 
                next_node = current_node.next
                # set current.next = prev
                current_node.next = prev
                # update prev = current
                prev = current_node
                # set current = next
                current_node = next_node
            # link the previous group to the current reversed group
            # At this point, prev is the head of the reversed group
            if prev_group_tail: 
                prev_group_tail.next = prev
            else: 
                # if there is no previous group, set the head (l) to the new head of the reversed group
                l = prev
            prev_group_tail = cur_group_tail  # save the tail 
        else: 
            # There are fewer than k nodes left; they should remain as-is. 
            # Connect the previous group to the rest of the list
            prev_group_tail.next = current_node
            break
    return l
def should_reverse(current_node, k): 
    # check if there are at least k nodes left in the list
    count = 0
    while current_node is not None: 
        count += 1
        current_node = current_node.next
        if count == k: 
            return True
    return False