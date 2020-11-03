def countPairs(numbers, k):
    # Write your code here
    pairs = {item: 1 for index, item in enumerate(numbers)}
    pairCount = 0
    for num in pairs:
        if num + k in pairs:
            pairCount += 1
    return pairCount


def maximum_xor(a, b):    
    sums = max(x^y for x in range(a, b) for y in range(a + 1, b + 1))
    return sums