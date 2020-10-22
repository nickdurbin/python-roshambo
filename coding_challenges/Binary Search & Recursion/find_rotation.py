"""
I was bored one day and decided to look at last names in the phonebook for my
area.
​
I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.
​
When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somewhere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."
​
Example:
​
surnames = [
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
    'liu',
    'mcdowell',
    'nixon',
]
​
[ 6, 7, 8, 15, 30, 0, 1, 2, 3, 4, 5]
​
Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.
​
*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""
def find_rotation_point(surnames):
    # Your code here
​
    # UNDERSTAND
​
    # [ 6,   7, 8, 0, 1, 2, 3, 4, 5]
    #           min max
    #           mid
​
    # [ 7, 0, 1,  2, 3, 4, 5, 6]
         #  min
         # max
         # mid
    # Plan:
    # we should use some kind of a binary search
​
    # max and min indices
    min = 0
    max = len(surnames) - 1
    # find the middle index
    mid = (min + max) // 2
​
    # if the middle surname is the rotation point:  (base case)
        # middle surname is rotation if prev element is > than current
        # return the index
    # otherwise:
    # have we rotated yet?
    # we can tell that by comparing to the first element in the array
    first_element = surnames[0]
​
    while not max <= min:
        current_element = surnames[mid]
        # if current element >= first element: we haven't rotated yet, rotation point is "still ahead of us"
        if current_element >= first_element:
            # search right
            # move the min index to middle + 1
            min = mid + 1
        # else if current element < first element: we have rotated
        else:
            # current_element < first_element
            # search left:
            # move the max index to middle index
            max = mid
​
    # keep going until max and min cross
    return min