def prefixFreePhones(numbers):
    numbers.sort()
    print(numbers)
    for i in range(len(numbers)): 
        for j in range(i+1, len(numbers)):
            if numbers[j].startswith(numbers[i]):
                return False
                break
            if numbers[i].startswith(numbers[j]):
                return False
                break
                
    return True 


# Solution needs work