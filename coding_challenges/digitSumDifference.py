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

# def digitSumsDifference(n):
#     digits = list(str(n))
#     odds_list = []
#     even_list = []
#     diff = 0
#     while n > 0 :
#         current = n % 10
#         if current % 2 == 0:
#             even_list.append(current)
#         else:
#             odds_list.append(current)
#             # print(odds_list,even_list)
#         print(n, current, n/10, math.floor(n / 10))
#         n = math.floor(n / 10)
#         # n = int(n / 10)
#         # n = n // 10
#     # sum odds / evens
#     # subtract
#     return sum(even_list) - sum(odds_list)