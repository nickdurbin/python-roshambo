def addTwoDigits(n):
    digits = [int(digit) for digit in str(n)]
    
    sum = 0
    for i in digits:
        print(i)
        sum += i
    
    return sum