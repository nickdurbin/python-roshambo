'''
You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of values of all the nodes with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.

Example 1:

Input:
root = [10, 5, 15, 3, 7, null, 18]
lower = 7
upper = 15

         10
         / \
        5  15
       / \    \
      3   7    18

Output:
32
Example 2:

Input:
root = [10,5,15,3,7,13,18,1,null,6]
lower = 6
upper = 10

           10
          /  \
       5       15
     / \     /   \ 
    3   7  13   18
   /   /
  1   6

Output:
23
'''
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBSTRangeSum(root, lower, upper):
  if root == None:
    return 0
  
  if root.value < lower:
    return csBSTRangeSum(root.right, lower, upper)
  if root.value > upper:
    return csBSTRangeSum(root.left, lower, upper);
      
  return root.value + csBSTRangeSum(root.right, lower, upper) + csBSTRangeSum(root.left, lower, upper)