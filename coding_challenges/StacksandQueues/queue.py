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
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 
1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size
​
    def enqueue(self, value):
        # add the new value, to the tail of our list
        self.size += 1
        self.storage.add_to_tail(value)
​
    def dequeue(self):
        if self.size == 0:
            return None
        # remove the value from the head of our list
        self.size -= 1
        value = self.storage.remove_head()
        return value
​
​
import unittest
​
class QueueTests(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
​
    def test_len_returns_0_for_empty_queue(self):
        self.assertEqual(len(self.q), 0)
​
    def test_len_returns_correct_length_after_enqueue(self):
        self.assertEqual(len(self.q), 0)
        self.q.enqueue(2)
        self.assertEqual(len(self.q), 1)
        self.q.enqueue(4)
        self.assertEqual(len(self.q), 2)
        self.q.enqueue(6)
        self.q.enqueue(8)
        self.q.enqueue(10)
        self.q.enqueue(12)
        self.q.enqueue(14)
        self.q.enqueue(16)
        self.q.enqueue(18)
        self.assertEqual(len(self.q), 9)
    
    def test_empty_dequeue(self):
        self.assertIsNone(self.q.dequeue())
        self.assertEqual(len(self.q), 0)
​
    def test_dequeue_respects_order(self):
        self.q.enqueue(100)
        self.q.enqueue(101)
        self.q.enqueue(105)
        self.assertEqual(self.q.dequeue(), 100)
        self.assertEqual(len(self.q), 2)
        self.assertEqual(self.q.dequeue(), 101)
        self.assertEqual(len(self.q), 1)
        self.assertEqual(self.q.dequeue(), 105)
        self.assertEqual(len(self.q), 0)
        self.assertIsNone(self.q.dequeue())
        self.assertEqual(len(self.q), 0)
​
if __name__ == '__main__':
    unittest.main()