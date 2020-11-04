'''
Write a function for doing an in-place ↴ shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.


Breakdown
It helps to start by ignoring the in-place ↴ requirement, then adapt the approach to work in place.

Also, the name "shuffle" can be slightly misleading—the point is to arrive at a random ordering of the items from the original list. Don't fixate too much on preconceived notions of how you would "shuffle" e.g. a deck of cards.

How might we do this by hand?

We can simply choose a random item to be the first item in the resulting list, then choose another random item (from the items remaining) to be the second item in the resulting list, etc.

Assuming these choices were in fact random, this would give us a uniform shuffle. To prove it rigorously, we can show any given item aa has the same probability (\frac{1}{n} 
n
1
​	
 ) of ending up in any given spot.

First, some stats review: to get the probability of an outcome, you need to multiply the probabilities of all the steps required for that outcome. Like so:

Outcome	Steps	Probability
item #1 is a	a is picked first	\frac{1}{n} 
n
1
​	
 
item #2 is a	a not picked first, a picked second	\frac{(n-1)}{n} * \frac{1}{(n-1)} = 
n
(n−1)
​	
 ∗ 
(n−1)
1
​	
 = \frac{1}{n} 
n
1
​	
 
item #3 is a	a not picked first, a not picked second, a picked third	\frac{(n-1)}{n} * \frac{(n-2)}{(n-1)} * \frac{1}{(n-2)} = 
n
(n−1)
​	
 ∗ 
(n−1)
(n−2)
​	
 ∗ 
(n−2)
1
​	
 = \frac{1}{n} 
n
1
​	
 
item #4 is a	a not picked first, a not picked second, a not picked third, a picked fourth	\frac{(n-1)}{n} * \frac{(n-2)}{(n-1)} * \frac{(n-3)}{(n-2)} * \frac{1}{(n-3)} = 
n
(n−1)
​	
 ∗ 
(n−1)
(n−2)
​	
 ∗ 
(n−2)
(n−3)
​	
 ∗ 
(n−3)
1
​	
 = \frac{1}{n} 
n
1
​	
 
So, how do we implement this in code?

So, how do we implement this in code?

If we didn't have the "in-place" requirement, we could allocate a new list, then one-by-one take a random item from the input list, remove it, put it in the first position in the new list, and keep going until the input list is empty (well, probably a copy of the input list—best not to destroy the input)

How can we adapt this to be in place?

What if we make our new "random" list simply be the front of our input list?

Solution
We choose a random item to move to the first index, then we choose a random other item to move to the second index, etc. We "place" an item in an index by swapping it with the item currently at that index.

Crucially, once an item is placed at an index it can't be moved. So for the first index, we choose from nn items, for the second index we choose from n-1n−1 items, etc.

This is a semi-famous algorithm known as the Fisher-Yates shuffle (sometimes called the Knuth shuffle).

Complexity
O(n)O(n) time and O(1)O(1) space.

What We Learned
Don't worry, most interviewers won't expect a candidate to know the Fisher-Yates shuffle algorithm. Instead, they'll be looking for the problem-solving skills to derive the algorithm, perhaps with a couple hints along the way.

They may also be looking for an understanding of why the naive solution is non-uniform (some outcomes are more likely than others). If you had trouble with that part, try walking through it again.
'''

import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list):
  # If it's 1 or 0 items, just return
  if len(the_list) <= 1:
    return the_list

  last_index_in_the_list = len(the_list) - 1

  # Walk through from beginning to end
  for index_we_are_choosing_for in range(0, len(the_list) - 1):

    # Choose a random not-yet-placed item to place there
    # (could also be the item currently in that spot)
    # Must be an item AFTER the current item, because the stuff
    # before has all already been placed
    random_choice_index = get_random(index_we_are_choosing_for,last_index_in_the_list)

    # Place our random choice in the spot by swapping
    if random_choice_index != index_we_are_choosing_for:
      the_list[index_we_are_choosing_for], the_list[random_choice_index] = \
      the_list[random_choice_index], the_list[index_we_are_choosing_for]