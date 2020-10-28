'''
Depth-First Preorder Traversal
This type of traversal is very similar to an inorder traversal except that the three steps' order is slightly different. Notice that in this traversal, we "visit" the node (denoted in the visualization below by the node turning red) before we recurse to the left subtree (we represent the recursive call by the turning the node grey in the visualization below). In the inorder traversal above, we recursed to the left subtree before visiting the node.

Visit node
Go to the left subtree
Go to the right subtree
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
  res.append(root.val)
  helper(root.left, res)
  helper(root.right, res)

def preorder_traversal(root):
  result = []
  helper(root, result)
  return result