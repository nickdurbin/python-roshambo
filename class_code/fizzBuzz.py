def fizzBuzz(n):
    arr = [i+1 for i in range(n)]
    new_arr = []
    for i in arr:
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
            new_arr.append(i)
        elif i % 3 == 0:
            i = "Fizz"
            new_arr.append(i)
        elif i % 5 == 0:
            i = "Buzz"
            new_arr.append(i)
        else:
            i = str(i)
            new_arr.append(i)
    return new_arr