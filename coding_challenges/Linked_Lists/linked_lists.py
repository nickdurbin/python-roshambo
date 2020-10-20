class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
  
  
class LinkedList:
  def __init__(self):
    self.head = None # Stores a node, that corresponds to our first node in the list 
    self.tail = None # stores a node that is the end of the list
  
  def add_to_head(self, value):
    # create a node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # new_node should point to current head
      new_node.next_node = self.head
      # move head to new node
      self.head = new_node
​
  def add_to_tail(self, value):
    # create a node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # point the node at the current tail, to the new node
      self.tail.next_node = new_node
      self.tail = new_node
​
  # remove the head and return its value
  def remove_head(self):
    # if list is empty, do nothing
    if not self.head:
      return None
    # if list only has one element, set head and tail to None
    if self.head.next_node is None:
      head_value = self.head.value
      self.head = None
      self.tail = None
      return head_value
    # otherwise we have more elements in the list
    head_value = self.head.value
    self.head = self.head.next_node
    return head_value 
​
  def contains(self, value):
    if self.head is None:
      return False
    
    # Loop through each node, until we see the value, or we cannot go further
    current_node = self.head
​
    while current_node is not None:
      # check if this is the node we are looking for
      if current_node.value == value:
        return True
​
      # otherwise, go to the next node
      current_node = current_node.next_node
    return False 
  
​
# example
# linked_list = LinkedList()
​
# linked_list.add_to_head(0)
# linked_list.add_to_tail(1)
# print(f'does our LL contain 0? {linked_list.contains(0)}')
# print(f'does our LL contain 1? {linked_list.contains(1)}')
# print(f'does our LL contain 2? {linked_list.contains(2)}')
​
# linked_list.add_to_head(2)
# print(f'the start of the list is {linked_list.head.value}')
# linked_list.add_to_head(5)
# print(f'the start of the list is {linked_list.head.value}')
# linked_list.remove_head()
# print(f'the start of the list is {linked_list.head.value}')
Shared in

class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
  
​
# class LinkedList:
#   def __init__(self):
#     # Stores a node, that corresponds to our first node in the list 
#     self.head = None     
#     # stores a node that is the end of the list
#     self.tail = None 
  
#   # return all values in the list a -> b -> c -> d -> None
#   def __str__(self):
#     output = ''
#     current_node = self.head # create a tracker node variable
#     while current_node is not None: # loop until its NONE
# ​
#       output += f'{current_node.value} -> '
# ​
#       current_node = current_node.next_node # update the tracker node to the next node
# ​
#     return output
#   def add_to_head(self, value):
#     # create a node to add
#     new_node = Node(value)
#     # check if list is empty
#     if self.head is None and self.tail is None:
#       self.head = new_node
#       self.tail = new_node
#     else:
#       # new_node should point to current head
#       new_node.next_node = self.head
#       # move head to new node
#       self.head = new_node
# ​
#   def add_to_tail(self, value):
#     # create a node to add
#     new_node = Node(value)
#     # check if list is empty
#     if self.head is None and self.tail is None:
#       self.head = new_node
#       self.tail = new_node
#     else:
#       # point the node at the current tail, to the new node
#       self.tail.next_node = new_node
#       self.tail = new_node
# ​
#   # remove the head and return its value
#   def remove_head(self):
#     # if list is empty, do nothing
#     if not self.head:
#       return None
#     # if list only has one element, set head and tail to None
#     if self.head.next_node is None:
#       head_value = self.head.value
#       self.head = None
#       self.tail = None
#       return head_value
#     # otherwise we have more elements in the list
#     head_value = self.head.value
#     self.head = self.head.next_node
#     return head_value 
# ​
#   def contains(self, value):
#     if self.head is None:
#       return False
    
#     # Loop through each node, until we see the value, or we cannot go further
#     current_node = self.head
# ​
#     while current_node is not None:
#       # check if this is the node we are looking for
#       if current_node.value == value:
#         return True
# ​
#       # otherwise, go to the next node
#       current_node = current_node.next_node
#     return False 
  
# ​
# # example
# linked_list = LinkedList()
# ​
# linked_list.add_to_head(0)
# linked_list.add_to_tail(1)
# linked_list.add_to_tail(2)
# linked_list.add_to_tail(3)
# print(linked_list)
# # print(f'does our LL contain 0? {linked_list.contains(0)}')
# # print(f'does our LL contain 1? {linked_list.contains(1)}')
# # print(f'does our LL contain 2? {linked_list.contains(2)}')
​
# linked_list.add_to_head(2)
# # print(f'the start of the list is {linked_list.head.value}')
# linked_list.add_to_head(5)
# # print(f'the start of the list is {linked_list.head.value}')
# linked_list.remove_head()
# # print(f'the start of the list is {linked_list.head.value}')
​
​
# import unittest
# from linked_list import LinkedList
​
# class LinkedListTests(unittest.TestCase):
#     def setUp(self):
#         self.list = LinkedList()
​
#     def test_add_to_tail(self):
#         self.list.add_to_tail(1)
#         self.assertEqual(self.list.tail.value, 1)
#         self.assertEqual(self.list.head.value, 1)
#         self.list.add_to_tail(2)
#         self.assertEqual(self.list.tail.value, 2)
#         self.assertEqual(self.list.head.value, 1)
​
#     def test_contains(self):
#         self.list.add_to_tail(1)
#         self.list.add_to_tail(2)
#         self.list.add_to_tail(5)
#         self.list.add_to_tail(10)
#         self.assertTrue(self.list.contains(10))
#         self.assertTrue(self.list.contains(2))
#         self.assertFalse(self.list.contains(1000))
​
#     def test_remove_head(self):
#         self.list.add_to_tail(10)
#         self.list.add_to_tail(20)
#         self.assertEqual(self.list.remove_head(), 10)
#         self.assertFalse(self.list.contains(10))
#         self.assertEqual(self.list.remove_head(), 20)
#         self.assertFalse(self.list.contains(20))
​
#         self.list.add_to_tail(10)    
#         self.assertEqual(self.list.remove_head(), 10)    
#         self.assertIsNone(self.list.head)
#         self.assertIsNone(self.list.tail)
#         self.assertIsNone(self.list.remove_head())
​
#     # def test_get_max(self):
#     #     self.assertIsNone(self.list.get_max())
#     #     self.list.add_to_tail(100)
#     #     self.assertEqual(self.list.get_max(), 100)
#     #     self.list.add_to_tail(55)
#     #     self.assertEqual(self.list.get_max(), 100)
#     #     self.list.add_to_tail(101)
#     #     self.assertEqual(self.list.get_max(), 101)
​
# if __name__ == '__main__':
#     unittest.main()