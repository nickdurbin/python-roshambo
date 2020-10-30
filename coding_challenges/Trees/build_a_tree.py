"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and output a binary tree.
​
*Note: assume that there will not be any duplicates in the tree.*
​
Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]
​
Output:
    5
   / \
  7  22
    /  \
   13   9
​
​
preorder = [5,7,22,13,9]  --> root = 5
inorder =  [22,7,5,9,13]
​
     5
   /  \
  7   13
 /    /
22   9
​
1) root = 5
2) if i = idx of root in inorder; inorder_left = [22, 7] and inorder_right = [9, 13]
3) preorder_left = [1: 1 + len(inorder_left) ], preorder_right = [len(preorder) - len(inorder_right) : len(preorder)]
4) recurse on (preorder_left, inorder_left) and recurse on (preorder_right, inorder_right)
​
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
​
def build_tree(preorder, inorder):
    # UPER
    #
    # Plan
​
    # if list(s) are empty, there's no tree, None
    if len(preorder) == 0:
        return None
    # 0) create a root node
    root = TreeNode()
    # 1) the first in the preorder is the root of the tree
    root.value = preorder[0]
​
    # 2) if i = index of the root in inorder, everything to the left of i is the left subtree and everything right of i is the right subtree
    # loop through inorder to find i
    root_index = 0
    while inorder[root_index] != root.value:
        root_index += 1
    # inorder_left = inorder[(beginning):root_index]
    inorder_left = inorder[:root_index]
​
    # inorder_right = inorder[root_index + 1:(end)]
    inorder_right = inorder[root_index + 1:]
​
    # How can we use ^^ to find the left/right subtress in the preorder?
    # 3) we can use the lengths of the inorder left/right subtrees to find the preorder left/right subtrees
    # preorder_left = [1: 1 + len(inorder_left) ],  (chop off the root), go for up to len(inorder_left)
    preorder_left = preorder[1:1 + len(inorder_left)]
    # preorder_right = [len(preorder) - len(inorder_right) : len(preorder)]
    preorder_right = preorder[-len(inorder_right):]
    # 4) recurse
    root.left = build_tree(preorder_left, inorder_left)
    root.right = build_tree(preorder_right, inorder_right)
​
    # return root
    return root
​
    # what do we need in order to be able to recurse?
    # subarrays -- inorder subarray and preorder subarray representing left / right subtrees
