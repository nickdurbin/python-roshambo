'''
Depth-First Inorder Traversal
Let's first look at an inorder depth-first traversal of a binary tree. In this traversal, we start at the tree's root node and complete the following steps recursively:

Go to the left subtree
Visit node
Go to the right subtree
Notice that we don't actually "visit" a node until we've already gone to the left subtree. In the animation below, the "going" is denoted by changing the color to a light grey. The actual visiting is represented when it turns red. The base cases in the recursion are when there is no left or right subtree to visit.
'''

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def helper(root, res):
  if root is None:
      return
  helper(root.left, res)
  res.append(root.val)
  helper(root.right, res)

def inorder_traversal(root):
  result = []
  helper(root, result)
  return result