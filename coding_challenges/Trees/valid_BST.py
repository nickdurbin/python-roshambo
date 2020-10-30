"""
You are given a binary tree. You need to write a function that can determine if
it is a valid binary search tree.
​
The rules for a valid binary search tree are:
​
- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.
​
Example 1:
Input:
​
    5
   / \
  3   7
​
Output: True
​
Example 2:
Input:
​
    10
   / \
  2   11
     / \
    6  12
​
Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
​
def is_valid_BST(root):
    # Your code here
    # Plan
    # is root.left.value < root.value
    # is root.right.value > root.value
    # need to also check min and max bounds using a helper method
    # is root.left valid
    # is root.right valid
    return is_valid_BST_with_bounds(root)
​
​
def is_valid_BST_with_bounds(root, min=None, max=None):
    if not root:
        return True
    # the bst is valid if:
    # min < root.value and root.value < max
    if min is not None and root.value < min:
        return False
    if max is not None and root.value > max:
        return False
​
    # left: min < left < root.value
    left_valid = is_valid_BST_with_bounds(root.left, min, root.value)
    # right: root.value < right < max
    right_valid = is_valid_BST_with_bounds(root.right, root.value, max)
    return left_valid and right_valid
​
​
#
#     10
#    / \
#   2   11
#      / \
#     6  12
​
root = TreeNode(10,
                TreeNode(2, None, None),
                TreeNode(11,
                         TreeNode(10.5),
                         TreeNode(12)))
​
