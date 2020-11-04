# Steps in Polya's Problem Solving
# UPER
# Understand the problem
# Devise a plan
# Implement it
# Reflect

# First Pass Solution
# Produces an infinite loop

def feed_philosophers(num):
  eating = [True, False, True, False, False]
  i=0
  while i < len(eating):
    if i == 0:
      if eating[4]:
        eating[4] = False
        eating[i] = True
    else:
      if eating[i-1]:
        eating[i-1] = False
        eating[i] = True
    i = (i+1) % 5

# Second Pass Solution Thoughts
# Linear data structures are not 
# ideal for circular construct
# doubly linked list?
# circular linked list?
# Could we generalize solution to work 
# with AND number of philosophers