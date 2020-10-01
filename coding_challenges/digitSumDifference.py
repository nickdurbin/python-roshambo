def digitSumsDifference(n):
    digits = [int(digit) for digit in str(n)]
    
    sum_even = 0
    sum_odd = 0
    for i in digits:
        if i % 2 == 0:
            sum_even += i
        elif i % 2 == 1:
            sum_odd += i
    
    sum_diff = sum_even - sum_odd
        
    
    return sum_diff