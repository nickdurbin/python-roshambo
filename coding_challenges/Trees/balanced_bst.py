'''
You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.

Example 1:
Given the following tree [5,10,25,None,None,12,3]:

    5
   / \
 10  25
    /  \
   12   3
return True.

Example 2:
Given the following tree [5,6,6,7,7,None,None,8,8]:

       5
      / \
     6   6
    / \
   7   7
  / \
 8   8
return False.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] boolean

'''

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def balancedBinaryTree(root):
  
  # Check for an empty tree and return True
  # As it would be balanced
  if root is None:
    return True
  
  # Start our recursive call to our height function 
  left_h = height(root.left)
  right_h = height(root.right)
  
  # No need to check right if our tree is unbalanced
  # From the left side.
  if balancedBinaryTree(root.left) == False:
    return False
  
  # We do check to make sure the absolute difference 
  # Between our left height and right height is less
  # Than or equal to 1 
  # Also, to see if our right and left heights are returning
  # As true as being balanced
  if (abs(left_h - right_h) <= 1) and balancedBinaryTree( 
  root.left) is True and balancedBinaryTree( root.right) is True: 
    return True
  
  # return False because our tree is not balanced
  return False
    
def height(root):
    
  # Our base case is to see if our root is None
  # And return a 0
  if root is None:
      return 0
  # Recursively call height to drill down to our base case
  # When we reach we evaluate left and right
  # Take the max of those 2 values and ADD 1
  return max(height(root.left), height(root.right)) + 1