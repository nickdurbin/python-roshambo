"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.
​
You already have a `Stack` class that you've implemented using a dynamic array.
​
Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.
​
*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*
"""
class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
​
    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)
​
    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
​
        return self.items.pop()
​
    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]
​
class MaxStack1:
    def __init__(self):
        # Your code here
        self.stack = Stack()
        # more stuff here ?
​
    def push(self, item):
        # O(1)
        """Add a new item onto the top of our stack."""
        # Your code here
        self.stack.push(item)
        # more stuff here ?
​
    def pop(self):
        # O(1)
        """Remove and return the top item from our stack."""
        # Your code here
        return self.stack.pop()
        # more stuff here ?
​
    def get_max(self):
        # O(n)
        """The last item in maxes_stack is the max item in our stack."""
        # Your code here
        # approach 1: pop everything off, find the max, and push it back on
        # trick: when we push it back on, we want everything to stay in the same order
        values = []
        element = self.stack.pop()
        cur_max = None
        while element is not None:
            values.append(element)
            if cur_max is None or cur_max < element:
                cur_max = element
            element = self.stack.pop()
​
        # loop:
        for i in range(len(values) - 1, -1, -1):
            # start with i = len(values - 1), go up to (but not including) i = -1, decrement i by -1 on each loop
            # for (int i = len(values) - 1; i > -1; i--)
            element = values[i]
            self.push(element)
​
        return cur_max
​
        # stack: 1, 2, 3
        # values = [3, 2, 1], stack = []
​
class MaxStack2:
    def __init__(self):
        # Your code here
        self.stack = Stack()
        self.max = None
        # more stuff here ?
​
    def push(self, item):
        # O(1)
        """Add a new item onto the top of our stack."""
        # Your code here
        self.stack.push(item)
        # update max is necessary
        if self.max is None or self.max < item:
            self.max = item
​
    def pop(self):
        #
        """Remove and return the top item from our stack."""
        # Your code here
        item = self.stack.pop()     # O(1)
        # check if we're removing the max
        if item == max:             # O(1)
            # if so, we need to update self.max
            new_max = self.find_max()  # O(n)
            self.max = new_max      # O(1)
        return item
        # more stuff here ?
​
    def get_max(self):
        # O(1)
        """The last item in maxes_stack is the max item in our stack."""
        # Your code here
        return self.max
​
    def find_max(self):
        values = []
        element = self.stack.pop()
        cur_max = None
        while element is not None:
            values.append(element)
            if cur_max is None or cur_max < element:
                cur_max = element
            element = self.stack.pop()
​
        # loop:
        for i in range(len(values) - 1, -1, -1):
            # start with i = len(values - 1), go up to (but not including) i = -1, decrement i by -1 on each loop
            # for (int i = len(values) - 1; i > -1; i--)
            element = values[i]
            self.push(element)
        return cur_max
​
class MaxStack:
    def __init__(self):
        # Your code here
        self.stack = Stack()
        self.max_stack = Stack()
​
    def push(self, item):
        # O(1)
        """Add a new item onto the top of our stack."""
        # Your code here
        self.stack.push(item)
        # update max is necessary
        # get the current max, compare it to item, and if current max < item, current max = item
        current_max = self.get_max()
        if current_max is None or current_max < item:
            current_max = item
        # push the max onto max_stack
        self.max_stack.push(current_max)
​
    def pop(self):
        #
        """Remove and return the top item from our stack."""
        # Your code here
        item = self.stack.pop()     # O(1)
        self.max_stack.pop()
        return item
        # more stuff here ?
​
    def get_max(self):
        # O(1)
        """The last item in maxes_stack is the max item in our stack."""
        # Your code here
        return self.max_stack.peek()
​
​
max_stack = MaxStack()
max_stack.push(1)           # stack: 1, max_stack =  1
max_stack.push(2)           # stack: 1, 2, max_stack =  1, 2
max_stack.push(3)           # stack: 1, 2, 3, max_stack =  1, 2, 3
max = max_stack.get_max()
print(max == 3)
​
max_stack.pop()             # stack: 1, 2, max_stack =  1, 2, 3
print(max_stack.get_max() == 2)
​
max_stack.push(0)           # stack: 1, 2, 0, max_stack = 1, 2, 2
print(max_stack.get_max() == 2)
max_stack.pop()             # stack: 1, 2, max_stack: 1, 2