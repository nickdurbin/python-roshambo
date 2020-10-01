def digitsManipulations(n):
    digits = [int(digit) for digit in str(n)]
    
    sum_add = 0
    sum_product = 1
    for i in digits:
        sum_add += i
        print(sum_add)
    
    for j in digits:
        sum_product *= j
        print(sum_product)
    
    
    sum_diff = sum_product - sum_add
    print(sum_diff)
        
    return sum_diff