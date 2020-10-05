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
def insertion_sort(arr): # O(n) + O(n)
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