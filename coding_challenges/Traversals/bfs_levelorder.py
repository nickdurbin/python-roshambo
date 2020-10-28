'''
Breadth-First (Level Order) Traversal
In a breadth-first traversal, we visit all the nodes at the same level (same distance from the root node) before going on to the next level.

A breadth-first traversal and a level order traversal are the same things. However, a breadth-first traversal can be done on any hierarchical data structure like trees and graphs. But, a level order traversal refers only to the traversal of a tree. Graphs do not have levels like trees do, so that term would not make sense.

A breadth-first traversal is a little different than the depth-first traversals we've gone over. We cannot merely use the recursive call stack to keep track of where we are in the tree. Instead, we must use a queue to keep track of what nodes we should visit. Remember that a queue data structure follows a first-in-first-out (FIFO) access order.

Below is a visualization for a breadth-first traversal.
'''

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def breadth_first_traversal(root):
  if root is None:
    return []

  result = []
  queue = []
  queue.append(root)

  while len(queue) != 0:
    node = queue.pop(0)
    result.append(node.val)

    if node.left is not None:
      queue.append(node.left)

    if node.right is not None:
      queue.append(node.right)

  return result