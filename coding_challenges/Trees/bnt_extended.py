"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    # O(log n)
    def insert(self, value):
        # take the current value of our node (self.value)    
        # compare to the new value we want to insert

        if value < self.value:
            # IF self.left is already taken by a node
                # make that (left) node, call insert 
            # set the left to the new node with the new value
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            # IF self.right is already taken by a node
                # make that (right) node call insert 
            # set the right child to the new node with new value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value is greater than target
        found = False
        if self.value >= target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)
            
        # if current value less than target
        if self.value < target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, lets find the largest number there by calling get_max on the right subtree
        # if we cannot go right, return the current value
        if self.right is None:
            return self.value
        max_val = self.right.get_max()
        return max_val

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on the current value fn(self.value)
        # if you can go left, call for_each on the left tree
        # if you can go right, call for_each on the right tree
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)

        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        queue = []
        # add the first node to the queue
        queue.append(node)
        # while queue is not empty
        while len(queue) > 0:
            # remove the first node from the queue
            first_node = queue.pop(0)
            # print the removed node 
            print(first_node.value)
            # add all children into the queue
            if first_node.left:
                queue.append(first_node.left)
            if first_node.right:
                queue.append(first_node.right)
        return queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        stack = []
        # add the first node to the stack
        stack.append(node)
        # while the stack is not empty
        while len(stack) > 0:
            # get the current node from the top of the stack
            last_node = stack.pop()
            # print that node
            print(last_node.value)
            # add all children to the stack
            if last_node.left:
                stack.append(last_node.left)
            if last_node.right:
                stack.append(last_node.right)
        return stack

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(node)
        if self.right:
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(node)
        if self.right:
            self.right.post_order_dft(node)
        print(self.value)

print(BSTNode([5,9,3,6,7,8,4,12,20]))