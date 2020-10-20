import unittest
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
  
​
class LinkedList:
  def __init__(self):
    # Stores a node, that corresponds to our first node in the list 
    self.head = None     
    # stores a node that is the end of the list
    self.tail = None 
  
  # return all values in the list a -> b -> c -> d -> None
  def __str__(self):
    output = ''
    current_node = self.head # create a tracker node variable
    while current_node is not None: # loop until its NONE
​
      output += f'{current_node.value} -> '
​
      current_node = current_node.next_node # update the tracker node to the next node
​
    return output
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
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
​
    def __len__(self):
        return self.size
​
    def push(self, value):
        # add an element to the front of our array
        self.size += 1
        self.storage.add_to_head(value)
​
    def pop(self):
        # check if empty
        if self.size == 0:
            return None
        # remove the first element in storage
        self.size -= 1
        node = self.storage.remove_head()
        return node
​
​
class QueueTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
​
    def test_len_returns_0_for_empty_stack(self):
        self.assertEqual(len(self.stack), 0)
​
    def test_len_returns_correct_length_after_push(self):
        self.assertEqual(len(self.stack), 0)
        self.stack.push(2)
        self.assertEqual(len(self.stack), 1)
        self.stack.push(4)
        self.assertEqual(len(self.stack), 2)
        self.stack.push(6)
        self.stack.push(8)
        self.stack.push(10)
        self.stack.push(12)
        self.stack.push(14)
        self.stack.push(16)
        self.stack.push(18)
        self.assertEqual(len(self.stack), 9)
​
    def test_empty_pop(self):
        self.assertIsNone(self.stack.pop())
        self.assertEqual(len(self.stack), 0)
​
    def test_pop_respects_order(self):
        self.stack.push(100)
        self.stack.push(101)
        self.stack.push(105)
        self.assertEqual(self.stack.pop(), 105)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack.pop(), 101)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.pop(), 100)
        self.assertEqual(len(self.stack), 0)
        self.assertIsNone(self.stack.pop())
        self.assertEqual(len(self.stack), 0)
​
​
if __name__ == '__main__':
    unittest.main()