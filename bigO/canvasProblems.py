import time
import random
# why do we have big o notation?
# To evaluate performance
# to find out the time it takes to complete a function (relative to other input sizes)
# different computers run at different speeds
# because we care about efficiency
# O(n) -- linear
# O(n^2) -- quadratic
# O(1) -- constant -- the performance doesn't change regardless of input
# O(log n) -- logarithmic -- every time we double the input size, we only add one extra step
# O(2^n) -- exponential
# factorial
# O(n log n) -- linearithmic
"""
Classify the runtime complexity of the number_of_steps function below using Big O notation.
"""
def number_of_steps(num):
    # overall: O(log n)
    # O(1) + O(log n * c) --> O(c log n + 1) --> O(log n)
    steps = 0                  # constant O(1)
    while num > 0:             # how many times does the loop run? log n times
        if num % 2 == 0:       # code w/in the loop is constant
            num = num // 2
        else:
            num = num - 1
        steps = steps + 1
    return steps
#
# for i in [8, 16, 32, 64]:
#     print(f"number_of_steps | N: {i} \tsteps: {number_of_steps(i)}")
print("-------")
"""
Classify the runtime complexity of the sorted_squares function below using Big O notation.
"""
def sorted_squares(A):
    # overall runtime complexity? O(4N + 5) --> O(N)
    N = len(A)                  # O(1)
    j = 0                       # O(1)
    while j < N and A[j] < 0:   # how many times does this loop run? at most N times -- O(N)
        j += 1                  # O(1)
    i = j - 1                   # O(1)
    ans = []                    # O(1)
    while 0 <= i and j < N:     # how many times does this loop run?  N -- O(N)
        if A[i] ** 2 < A[j] ** 2:  # O(1)
            ans.append(A[i] ** 2)  # appending to end of the list is usually constant
            i -= 1
        else:
            ans.append(A[j] ** 2)
            j += 1
    while i >= 0:                   # how many times does this loop run? at most N
        ans.append(A[i] ** 2)       # O(1)
        i -= 1
    while j < N:
        ans.append(A[j] ** 2)
        j += 1
    return ans
for i in [100, 1000, 10000]:
    a = [j for j in range(-i // 2, i // 2)]
    start = time.time()
    sorted_squares(a)
    end = time.time()
    print(f"Sorted Squares | N: {i} \ttime: {end - start}")
"""
Classify the runtime complexity of the insertion_sort function below using Big O notation.
"""
def insertion_sort(arr):
    # O(n*n) --> O(n^2)
    for i in range(1, len(arr)):    # O(n)
        key = arr[i]                # O(1)
        j = i - 1                   # O(1)
        while j >= 0 and key < arr[j]:  # at most N --> O(n)
            arr[j + 1] = arr[j]     # O(1)
            j -= 1                  # O(1)
            for k in range(len(arr)):
                # this makes it O(n^3)
                # do stuff
        arr[j + 1] = key
print("-------")
for i in [100, 1000, 10000]:
    a = [random.randint(0, j) for j in range(i)]
    start = time.time()
    insertion_sort(a)
    end = time.time()
    print(f"insertion_sort | N: {i} \ttime: {end - start}")

"""
Classify the runtime complexity of the number_of_steps function below using Big O notation.
"""
# O(log n)
def number_of_steps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        steps = steps + 1
    return steps



"""
Classify the runtime complexity of the sorted_squares function below using Big O notation.
"""
def sorted_squares(A):
    # O(4n) which equates to O(n)
    N = len(A)
    j = 0
    while j < N and A[j] < 0:
        j += 1
    i = j - 1

    ans = []
    while 0 <= i and j < N:
        if A[i]**2 < A[j]**2:
            ans.append(A[i]**2)
            i -= 1
        else:
            ans.append(A[j]**2)
            j += 1

    while i >= 0:
        ans.append(A[i]**2)
        i -= 1
    while j < N:
        ans.append(A[j]**2)
        j += 1

    return ans



"""
Classify the runtime complexity of the insertion_sort function below using Big O notation.
"""
def insertion_sort(arr): # O(n * n) => O(n^2)
    for i in range(1, len(arr)): 
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key

# O(log n)
def foo(n):
    i = 1
    while i < n:
        print(i)
        i *= 2

# O(n)
def search_for_thing(items, thing):
    for item in items:
        if item == thing:
            return True

    return False

# O(n^2)
def do_different_things(items): # O(n + n^2)
    for item in items: # O(n)
        print(item)

    for item_one in items: # O(n * n) = O(n^2)
        for item_two in items:
            print(item_one, item_two)


# O(n)
def do_a_bunch_of_stuff(items): # O(1 + n/2 + 2000)
    last_idx = len(items) - 1
    print(items[last_idx]) # O(1)

    middle_idx = len(items) / 2
    idx = 0
    while idx < middle_idx: # O(n/2)
        print(items[idx])
        idx = idx + 1

    for num in range(2000): # O(2000)
        print(num)

# O(n^2)
def print_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)

# O(n)
def print_every_item(items):
    for item in items:
        print(item)

# Constant or O(c) or O(1)
def print_one_item(items):
    print(items[0])