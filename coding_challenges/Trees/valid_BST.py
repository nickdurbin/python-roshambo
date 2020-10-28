"""
You are given a binary tree. You need to write a function that can determin if
it is a valid binary search tree.

The rules for a valid binary search tree are:

- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.

Example 1:
Input:

    5
   / \
  3   7

Output: True

Example 2:
Input:

    10
   / \
  2   8
     / \
    6  12

Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_BST(self, root):
    # Check to see root exists
    if root is None:
        return -1

    # See if there are any branches if not return True
    if root.left is None and root.right is None:
        return True

    # Short circut the lookup 
    # If left is greater than the root
    # Return False
    if root.left > root:
        return False

    # Same check on the right side (may not be needed)
    if root.right < root:
        return False

    else:

        # Our recursion to check all nodes starting with the left.
        # If left checks out turn to the right nodes.
        left_node = is_valid_BST(root.left)
        right_node = is_valid_BST(root.right)

        # If the left is smaller than the right
        # Return True lese return False
        if left_node < right_node:
            return True
        else:
            return False
