'''
Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively (noden representing the leaf).

Example

For

t = {
    "value": 5,
    "left": {
        "value": 2,
        "left": {
            "value": 10,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": -3,
        "left": null,
        "right": null
    }
}
the output should be
treePaths(t) = ["5->2->10", "5->2->4", "5->-3"].

The given tree looks like this:

    5
   / \
  2  -3
 / \
10  4
Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 710,
-1000 ≤ node value ≤ 1000.

[output] array.string

The root-to-leaf paths, sorted by the leaves in the order that they appear in the pre-order traversal (i.e. from the leftmost leaf to the rightmost).
'''

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treePaths(t):
    paths = helper(t, [], [])
    return paths
# current_path: []
# paths: ["5->2->10", "5->2->4", "5->-3"]
# t = 5
def helper(t, current_path, paths): 
    if not t: 
        return []
    current_path.append(str(t.value))
    if not t.left and not t.right: 
        path = "->".join(current_path)
        paths.append(path)
    if t.left: 
        helper(t.left, current_path, paths)
    if t.right: 
        helper(t.right, current_path, paths)    
    current_path.pop()
    return paths
    # # we want an array of paths
    # paths = []
    # # paths from roots --> leaves means Depth First
    # if t is None: 
    #     return paths
    # stack = []
    # # add the current node to our stack 
    # stack.append((t, [str(t.value)]))
    # # while the stack is not empty: 
    # while len(stack) > 0: 
    #     # node = pop off the top of the stack
    #     node, current_path = stack.pop()  # pop off the end
    #     # "process" it --> add it to the current path we're on
    #     # current_path.append(str(node.value))
    #     # add it's children to the stack  
    #     if node.right:
    #         current_path.append(str(node.right.value))
    #         stack.append((node.right, current_path))
    #         current_path.pop()
    #     if node.left: 
    #         current_path.append(str(node.left.value))
    #         stack.append((node.left, current_path))
    #         current_path.pop()
    #     # if node is a leaf: we're done with the current path
    #     if not node.left and not node.right: 
    #         # we can add it to our array of paths  
    #         path = "->".join(current_path)
    #         paths.append(path)
    #     # how do we "backtrack" the current path? 
    #     # hacky way is to store the current path up to the node in the stack
    # return paths