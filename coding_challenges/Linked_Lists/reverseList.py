def reverse_list(l):
  # create a previous node and set value to None
  previous_node = None
  # create a variable to store the current node
  # set it to the current head
  current_node = l
  # create a while loop that runs while the list
  # is not empty or the value of None
  while current_node is not None:
    # set the next node to the currents next 
    # which is technically the head's next node
    next_node = current_node.next
    # reset the value of the current next node to
    # the previous node
    current_node.next = previous_node
    # the previous node becomes the next node 
    previous_node = current_node
    # the current node then becomes the next node
    current_node = next_node
  # the new head becomes the previous node
  # thus reversing the order of the linked list
  l = previous_node

  return l