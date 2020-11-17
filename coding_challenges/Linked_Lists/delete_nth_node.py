# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # One pass solution: 
        # We want to keep three pointers: 
        # first one goes all the way to the end (its "looking ahead" by n)
        # the second one is N behind. so that onces first is None, second is at the node we want to remove. Start it once first has advanced N times
        # the third one just tracks the node previous to the second so that we can remove it
        # keep track of the current index 
        current_index = 0
        first = head
        second = head
        previous = None
        # O(N)
        while first is not None: 
            if current_index < n: 
        #       only move first
                first = first.next
        #   else if index > N:   (check the conditions)
            elif current_index >= n: 
        #       move all 3 pointers
                previous = second
                second = second.next
                first = first.next
            current_index += 1
        # remove second by setting previous.next = second.next
        if previous is None: 
            return second.next
        previous.next = second.next
        return head
        # First approach: two passes
        # 1: we need to find the node we want to remove
            # How do we know we've hit the nth from the end node? 
            # we can keep track of our current index as we iterate through, but that doesn't tell us
            # how far we are from the end
            # knowing the length would be helpful 
                # then target index = len - n
                # we could just traverse the whole list to get the length
            # then traverse a second time len - n times
        # 2: once we find that node, remove it
            # keep track of the previous node
            # set previous.next = current.next
#         # Plan: 
#         # Overall: O(N)
#         # traverse through the linked list to get the length: 
#         # keep track of number of nodes we've seen
#         # O(N)
#         length = 0
#         # set the current to head
#         current = head
#         while current is not None:
#             # we increment the number of nodes we've seen
#             length += 1
#             # move current forward (current = current.next)
#             current = current.next
#         # Find the target index: length - n
#         # O(1)
#         target_index = length - n
#         # traverse to the target index
#         current = head
#         # keep track of the previous node
#         previous = None
#         # O(len - n) --> O(N)
#         for i in range(target_index): 
#             previous = current
#             current = current.next
#         # if head.next is None:  # single node
#         #     return None
#         if previous is None:  # trying to remove the head
#             return current.next 
#         # remove the node at the target index by setting previous.next = current.next
#         previous.next = current.next
#         return head