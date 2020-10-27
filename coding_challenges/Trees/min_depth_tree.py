'''
You are given a binary tree and you are asked to write a function that finds its minimum depth. The minimum depth can be defined as the number of nodes along the shortest path from the root down to the nearest leaf node. As a reminder, a leaf node is a node with no children.

Example:
Given the binary tree [5,7,22,None,None,17,9],

    5
   / \
  7  22
    /  \
   17   9
your function should return its minimum depth = 2.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] integer
'''

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def minimumDepthBinaryTree(root):
    # If there is no root, then the depth should be 0
    if root == None:
        return 0
    
    # When we reach None on left and right just add the row we are on
    if root.left == None and root.right == None:
        return 1
    
    # If the left does return None we need to evaluate
    # The right and return its depth + 1
    if root.left == None:
        return minimumDepthBinaryTree(root.right) + 1
    
    # If the right does return None we need to evaluate
    # The left and return its depth + 1 
    if root.right == None:
        return minimumDepthBinaryTree(root.left) + 1
    
    # Recursively call left till we hit None
    # Then recursively call right till we hit None
    else:
        left_d = minimumDepthBinaryTree(root.left)
        right_d = minimumDepthBinaryTree(root.right)
        print(right_d)
        
        # If left is less than right return it and ADD 1 to the depth total
        # Else return right plus one to the depth total
        if left_d < right_d:
            return left_d + 1
        else: 
            return right_d + 1