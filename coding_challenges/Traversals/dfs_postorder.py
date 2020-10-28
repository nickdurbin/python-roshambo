'''
Depth-First Postorder Traversal
This traversal type is very similar to our other traversals except that the three steps' order is slightly different. Notice that in this traversal, we "visit" the node (denoted in the visualization below by the node turning red) after we recurse to the left subtree (we represent the recursive call by turning the node grey in the visualization below) and the right subtree.

Go to the left subtree
Go to the right subtree
Visit node
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
  helper(root.right, res)
  res.append(root.val)

def postorder_traversal(root):
  result = []
  helper(root, result)
  return result