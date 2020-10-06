# def prefixFreePhones(numbers):
#     numbers.sort()
#     print(numbers)
#     for i in range(len(numbers)): 
#         for j in range(i+1, len(numbers)):
#             if numbers[j].startswith(numbers[i]):
#                 return False
#             if numbers[i].startswith(numbers[j]):
#                 return False

#     return True 

# Solution needs work
# Time Complexity == O(n log n) 
# Space Complexity ==  O(1)
def prefixFreePhones(numbers):

    numbers.sort()  # O(n log n)

    for n in range(len(numbers) -1):
        if numbers[n+1].startswith(numbers[n]):
            print(numbers[n+1], numbers[n])
            return False
        

    return True

numbers = ["69297543", 
 "692975867", 
 "692975799", 
 "69297578",
 "692975222", 
 "692975380", 
 "692975279", 
 "69297547",
 "692975884",
 "69297502", 
 "69297525"]

print(prefixFreePhones(numbers))