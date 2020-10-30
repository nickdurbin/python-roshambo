# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
​
​
def helper(root, res):
    if root is None:
        return
    res.append(root.val)
    helper(root.left, res)
    helper(root.right, res)
​
​
def preorder_traversal(root):
    result = []
    helper(root, result)
    return result
​
​
def breadth_first_traversal(root):
    if root is None:
        return []
​
    result = []
    queue = []
    queue.append(root)
​
    while len(queue) != 0:
        node = queue.pop(0)  # remove from the front of the array (to keep FIFO order)
        result.append(node.val)
​
        if node.left is not None:
            queue.append(node.left)
​
        if node.right is not None:
            queue.append(node.right)
​
    return result
​
​
def iterative_pre_order(root):
    # Understand -
    # do a pre_order traversal, return the order in an array
​
    # PLAN
    # an array to store the result
    result = []
    # a stack to store the nodes we need to process
    stack = []  # we have to maintain LIFO by only appending to the end and popping from the end
    # process self, then left, then right
    # we know we need to process the root, add it to the stack
    stack.append(root)
    # while stack is not empty (that means we still need to process nodes)
    while len(stack) > 0:
        # current = pop off the top of the stack
        current = stack.pop()  # remove the last item from stack
        # process it
        result.append(current.val)
            # we know have to handle the left subtree and the right subtree
            # can we just do current = current.left ?
            # we can’t lose the right subtree yet
        # push it (current.right) (if it exists) onto the stack for safe keeping
        if current.right is not None:
            stack.append(current.right)
        # push current.left (if it exists) onto the stack, and we’ll handle it on the next loop
        if current.left is not None:
            stack.append(current.left)
    # return the result
    return result
​
​
root = TreeNode(22,
                left=TreeNode(5,
                              left=None,
                              right=TreeNode(18, left=None, right=None)),
                right=TreeNode(54,
                               left=TreeNode(32,
                                             left=TreeNode(28, left=None, right=None),
                                             right=TreeNode(42, left=None, right=None)),
                               right=None)
                )
​
​
print(preorder_traversal(root))
print(iterative_pre_order(root))