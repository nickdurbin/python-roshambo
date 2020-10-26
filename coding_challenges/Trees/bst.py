class BSTNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BSTNode(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
          self.right = BSTNode(value)
      else:
        self.right.insert(value)

  def search(self, target):
    if self.value == target:
      return self
    elif target < self.value:
      if self.left is None:
        return False
      else:
        return self.left.search(target)
    else:
      if self.right is None:
        return False
      else:
        return self.right.search(target)

class BST:
  def __init__(self, value):
    self.root = BSTNode(value)

  def insert(self, value):
    self.root.insert(value)

  def search(self, value):
    self.root.search(value)