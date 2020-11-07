#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBinaryTreeInvert(root):
    stack = [root]    
    
    while stack:        
        node = stack.pop(-1)        
        if node:            
            node.left, node.right = node.right, node.left            
            stack.append(node.left)            
            stack.append(node.right)    
    return root

#     result = []
#     reverse(root, result)
#     rev_tree = Tree(result[0])
#     for ele in result[1:]:
#         rev_tree.push(ele)
#     return rev_tree

# def reverse(root, res):
#     if root is None:
#       return
#     res.append(root.value)
#     reverse(root.right, res)
#     reverse(root.left, res)
